
from rest_framework import serializers
from django.contrib.auth import get_user_model

User= get_user_model()

class SingUpSerializer(serializers.ModelSerializer):

    password=serializers.CharField(write_only=True)

    class Meta:
      model = User
      fields = ('username' , 'phone','email' , 'password','bank_name','account_number','account_type')

    def create(self ,validated_data):
     
     is_valid=self.validate_bank_details(
     validated_data.get('bank_name'),
     validated_data.get('account_number')
     )
     
     if not is_valid:
        raise serializers.validationErorr ("please check your account details and try again")



     user= User.objects.create_user(
        username= validated_data['username'],
        phone= validated_data['phone'],
        email= validated_data['email'],
        password= validated_data['password'],
        bank_name= validated_data['bank_name'],
        account_number= validated_data['account_number'],
        account_type= validated_data['account_type'],
        is_verified=True
    )
     return user 
