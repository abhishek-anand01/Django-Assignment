from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    """
    Serializer for the Person model.

    This serializer is used to convert Person model instances to JSON
    representations and vice versa. It includes all fields from the Person
    model.

    Attributes:
        model: The Person model class that this serializer is associated with.
        fields: A special attribute that indicates all fields from the model
            should be included in the serialized representation.

    Note:
        This serializer inherits from the rest_framework.serializers.ModelSerializer
        class and is automatically generated based on the Person model.
    """

    class Meta:
        model = Person
        fields = '__all__'