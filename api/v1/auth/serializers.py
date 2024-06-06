from rest_framework import serializers
from authuser.models import User , Customer


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","username","role","is_superuser","email",)


# for all content
class UserAllDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ['username', 'email', 'role', 'password']
    extra_kwargs = {'password': {'write_only': True}}


    
    def create(self, validate_data):
        role = validate_data.get('role',User.Role.ADMIN)
        print(role)
        if(role=="ADMIN"):
            user = User(
                username=validate_data['username'],
                email=validate_data['email'],
                role=validate_data.get('role', User.Role.CUSTOMER)
            )
            # print(user.role)
            user.set_password(validate_data['password'])
            user.save()
            return user
        if(role=="CUSTOMER"):
            user = Customer(
                username=validate_data['username'],
                email=validate_data['email'],
                role=validate_data.get('role', User.Role.CUSTOMER)
            )
            # print(user.role)
            user.set_password(validate_data['password'])
            user.save()
            return user