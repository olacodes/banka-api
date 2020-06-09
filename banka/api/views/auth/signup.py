import bcrypt
import uuid

from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status

from ...models.user import User
from ...validations.user.user_validation import validate_user
from ...utils.helper import Helper


class SignUp(APIView):
    def post(self, request):
        data = request.data

        # validate input data
        validate_user_field = validate_user(data)
        if (validate_user_field) != True:
            return validate_user_field;

        # check if user already exist
        is_user_exist = User.objects.filter(email=data['email'].strip())
        if is_user_exist:
            return Response({
                'status': 400,
                'message': "Email already exist",
                'error': 'Email already exist'
            })

        # Hash password
        hashed = bcrypt.hashpw(
                data['password'].encode('utf-8'), 
                bcrypt.gensalt()
            )

        # convert is_admin to boolean value
        admin_status = Helper.string_bool_to_bool(data['is_admin'])

        # create user object
        user = User.objects.create(
            id = uuid.uuid4(),
            firstname=data['firstname'].strip(),
            lastname=data['lastname'].strip(),
            email=data['email'].strip(),
            password=hashed,
            user_type=data['user_type'],
            is_admin=admin_status
        )

        # save user in db
        user.save()   

        # create the return object
        user = User.objects.filter(email=data['email'].strip())[0]

        # generate token with user firstname as payload
        token = RefreshToken.for_user(user)

        return Response({
            'status': 201,
            'message': "user successfully created",
            'data':{
                'token' : str(token.access_token),
                'id': user.id,
                'firstname':user.firstname,
                'lastname': user.lastname,
                'email': user.email,
            }
        }, status=status.HTTP_201_CREATED)

        
