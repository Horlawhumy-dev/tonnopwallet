from rest_framework import serializers
from django.core.validators import MinLengthValidator
from .models import EmployeeModel
from .validators import validate_email, validate_reg_number


class GetEmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmployeeModel
        fields = "__all__"



class PostEmployeeSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True,  validators=[MinLengthValidator(
                limit_value=3,
                message="First name must be longer than 3 characters"
            )
        ],)
    last_name = serializers.CharField(required=True,
        validators=[MinLengthValidator(
                    limit_value=3,
                    message="Last name must be longer than 3 characters"
                )
            ])
    email = serializers.EmailField(required=True, validators=[validate_email])
    reg_number = serializers.CharField(required=True, validators=[validate_reg_number, MinLengthValidator(
                limit_value=5,
                message="Registration keys must be longer than 5 characters"
            )
        ])
    department = serializers.CharField(required=True, 
    validators=[MinLengthValidator(
                limit_value=2,
                message="Department must be longer than 2 characters."
            )
        ])

    class Meta:
        model = EmployeeModel
        exclude = ['joined_at']

    def create(self, validated_data):
        return EmployeeModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name) 
        instance.last_name = validated_data.get('last_name', instance.last_name) 
        instance.email = validated_data.get('email', instance.email) 
        instance.reg_number = validated_data.get('reg_number', instance.reg_number) 
        instance.department = validated_data.get('department', instance.department) 

        instance.save()
        return instance