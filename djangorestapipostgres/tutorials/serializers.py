from rest_framework import  serializers
from tutorials.models import  Tutorial

class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id','title','description','published')
        model=Tutorial
