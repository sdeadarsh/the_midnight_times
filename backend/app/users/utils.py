from .models import User

def check_if_admin(id):
    check_admin_data = User.objects.filter(id=id).values('is_admin')
    if check_admin_data and check_admin_data[0]['is_admin']:
        return True
    return False
    