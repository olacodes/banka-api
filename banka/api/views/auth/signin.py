import bcrypt

from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status

from ...models.user import User
from ...utils.helper import Helper


class SignIn(APIView):
    def post(self, request):
        data = request.data

        user_email = Helper.get_field(data, 'email')
        user_password = Helper.get_field(data, 'password')

        if not user_email or not user_password:
            return Response({
                'status': 400,
                'message': 'email or password field must not be blank',
                'error': 'Invalid login credentials'
            }, status=status.HTTP_400_BAD_REQUEST)
        

        user = User.objects.filter(email=user_email)[0]

        # check if user exist
        if not user:
            return Response({
                'status': 400,
                'message': 'Unregistered user',
                'error': 'Invalid login credentials'
            })

        # check if password is match
        is_valid_password = bcrypt.checkpw(
                data['password'].encode('utf-8'), user.password.split("'")[1].encode('utf-8'))
        
        if not is_valid_password:
            return Response({
                'status': 400,
                'message': 'Password do not match',
                'error': 'Invalid login credentials'
            }, status=status.HTTP_400_BAD_REQUEST)

        # genrate token
        token = RefreshToken.for_user(user)

        # create the respond object and send
        return Response({
            'status': 200,
            'data': {
                'token': str(token.access_token),
                'id': user.id,
                'firstname': user.firstname,
                'lastname': user.lastname,
                'email': user.email,
            }

        }, status=status.HTTP_200_OK)

