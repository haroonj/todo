from rest_framework import serializers
from todos import models

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'des',
            "done",
            "date_created",

        )
        model = models.Todo