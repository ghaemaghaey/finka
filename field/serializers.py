from rest_framework import serializers
from .models import Field, Note, Cost, Image, Voice, Job, Cultivation_calender, Product


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = "__all__"


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"


class CostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cost
        fields = "__all__"


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class VoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voice
        fields = "__all__"


class JobSerializer(serializers.ModelSerializer):
    field = FieldSerializer()
    costs = CostSerializer()
    notes = NoteSerializer()
    voices = VoiceSerializer()
    images = ImageSerializer()

    class Meta:
        model = Job
        fields = "__all__"


class CultivationCalenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cultivation_calender
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    cultivation_calender = CultivationCalenderSerializer()

    class Meta:
        model = Product
        fields = "__all__"
