from rest_framework import serializers
from .models import *

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','user','profile_picture','bio','name','location','contact')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model= Post
        fields =('id','title','project_link', 'description','profile','image','user','created_date')
