from rest_framework import serializers
from .models import User,Profile



class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        exclude = ['id','user']





class UserSerializer(serializers.ModelSerializer):

    profile = ProfileSerializer(read_only=True)


    class Meta:
        model = User
        fields = ['id','email','phone','nickname','selected_car','balance','is_offer_active','overall_score','can_reserve','profile']



