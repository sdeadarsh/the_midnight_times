from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import User
from.searializers import UserSerializer
from rest_framework import viewsets, permissions, status, views
from rest_framework.parsers import MultiPartParser, JSONParser
from django.core import paginator
from rest_framework.response import Response
from rest_framework.decorators import action
from the_midnight_times.utils import successfull_response, errored_response



class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'post', 'patch', 'delete']
    serializer_class = UserSerializer
    queryset = User.objects.filter(is_active=1)

    def add_pagination(self, dict_data, page, count):
        if page and count:
            p = paginator.Paginator(dict_data, count)
            return p.page(page).object_list
        return dict_data

    def list(self, request, *args, **kwargs):
        data = User.objects.filter(is_admin=False)
        serialized = UserSerializer(data, many=True)
        return successfull_response(serialized.data)

    def retrieve(self, request, *args, **kwargs):
        response = super(UserViewSet, self).retrieve(request, *args, **kwargs)
        return successfull_response(response.data)

    def create(self, request, *args, **kwargs):
        try:
            user_name = request.data.get('user_name', None)
            password = request.data.get('password', None)
            if not user_name or not password:
                return successfull_response({}, "Please pass the valid user is ad password")
            user_data = User.objects.filter(user_name=user_name, password=password)
            if user_data:
                return successfull_response({}, "This user already exists")
            response = super(UserViewSet, self).create(request, *args, **kwargs)
            return successfull_response(response.data, "Added Successfully")
        except Exception as e:
            print('error', str(e))
            return errored_response("error in creating user")

    def update(self, request, *args, **kwargs):
        response = super(UserViewSet, self).update(request, partial=True)
        return successfull_response(response.data, "Updated Successfully")

    def destroy(self, request, *args, **kwargs):
        User.objects.filter(pk=kwargs['pk']).update(is_active=0)
        return successfull_response({}, "Deleted Successfully")

    # @action(methods=['POST'], detail=False)
    # def register(self, request):
    #     print('in register')
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data.get('username')
    #         messages.success(request, f'Account created for {username}!')
    #         return redirect('login')
    #     else:
    #         form = UserCreationForm()
    #     return render(request, 'users/register.html', {'form': form})

    @action(methods=['POST'], detail=False)
    def login(self, request):
        form = AuthenticationForm(request, data=request.data)
        if form.is_valid():
            user_name = form.cleaned_data.get('user_name')
            password = form.cleaned_data.get('password')
            user = User.objects.filter(user_name=user_name, password=password)
            if user :
                return successfull_response({}, "Valid User")
            else:
                return errored_response("Invalid User")
        else:
            return errored_response("Invalid User")
