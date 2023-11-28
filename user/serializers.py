# yourapp/serializers.py
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth.models import Group
from django.db import transaction

class CustomRegisterSerializer(RegisterSerializer):
    user_type = serializers.ChoiceField(choices=[('admin', 'Admin'), ('author', 'Author'), ('reader', 'Reader')])

    @transaction.atomic
    def custom_signup(self, request, user):
        user_type = self.validated_data.get('user_type')
        
        # Add custom logic based on user_type
        if user_type == 'admin':
            group_name = 'AdminGroup'
        elif user_type == 'author':
            group_name = 'AuthorGroup'
        else:
            group_name = 'ReaderGroup'

        # Assign the user to the corresponding group
        group, created = Group.objects.get_or_create(name=group_name)
        user.groups.add(group)

    def save(self, request):
        user = super().save(request)
        self.custom_signup(request, user)
        return user
