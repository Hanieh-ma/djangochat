import hashlib
from django.contrib.auth.models import User
from rest_framework import serializers



class ShortUserProfileSerializer(serializers.ModelSerializer):
    
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        return obj.first_name + ' ' + obj.last_name


    class Meta:
        model = User
        fields = ('id', 'username', 'full_name')


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('password',)



class RequestSignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

    def create(self, data):
        u = User(
            first_name=data['first_name'],
            last_name=data['last_name'],
            username=data['username'],
        )
        u.set_password(data['password'])
        u.save()
        return u
        

class RequestLoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        required=True, max_length=30, allow_blank=False,
    )
    password = serializers.CharField(
        required=True, max_length=128, allow_blank=False 
    )


class RequestGetSerializer(serializers.Serializer):
    first_name = serializers.CharField(
        required=False, allow_blank=False, max_length=100)
    last_name = serializers.CharField(
        required=False, allow_blank=False, max_length=100
    )

    def validate(self, data):
        if 'first_name' not in data and 'last_name' not in data:
            raise serializer.ValidationError(
                'At least one of firstname or lastname parameters are required'
            ) 
        return data


# class UsersSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Users
#         fields = ['first_name', 'last_name']

#     def validate_number_of_friends(self, data):
#         if data == 5:
#             raise serializers.ValidationError(
#                 'In this country, you cant have 5 friends')
#         return data

class UsersSerializer(serializers.Serializer):
    first_name = serializers.CharField(
        required=True, allow_blank=False, max_length=100)
    last_name = serializers.CharField(
        required=True, allow_blank=False, max_length=100
    )
    birthday = serializers.DateField()
    number_of_friends = serializers.IntegerField(
        default=10, min_value=0
    )

    def validate_number_of_friends(self, data):
        if data == 5:
            raise serializers.ValidationError(
                'In this country, you cant have 5 friends')
        return data

    def create(self, validated_data):
        print("I'm in the create function")
        u = User(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            birthday=validated_data['birthday'],
            number_of_friends=validated_data['number_of_friends']
        )
        u.save()
        return u
        
