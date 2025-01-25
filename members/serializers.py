from rest_framework import serializers
from .models import Member, Role

class RoleSerializer(serializers.ModelSerializer):
    members = serializers.StringRelatedField(many=True)

    class Meta:
        model = Role
        fields = ['id', 'name', 'description', 'members']

class MemberSerializer(serializers.ModelSerializer):
    role = RoleSerializer()

    class Meta:
        model = Member
        fields = [
            'id', 'first_name', 'last_name', 'email', 'phone_number',
            'membership_date', 'role'
        ]
