from rest_framework.response import Response

def successfull_response(data, message="success"):
    return Response(
        {
            'result': {
                "data": data,
                "message": message,
                "error": False}
        }
    )


def errored_response(message):
    return Response(
        {
            'result': {
                "data": {},
                "message": message,
                "error": True}
        }
    )