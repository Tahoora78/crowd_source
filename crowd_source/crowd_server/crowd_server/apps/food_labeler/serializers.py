from rest_framework import serializers
from .models import Question

class FoodLabelerSerializer(serializers.ModelSerializer):

    question_id = serializers.IntegerField()
    label = serializers.IntegerField()
    token = serializers.CharField()

    class Meta:
        model = Question
        fields = ('question_id', 'label')
