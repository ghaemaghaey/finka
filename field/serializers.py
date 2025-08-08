from rest_framework import serializers
from .models import Field, Note, Cost, Image, Job, Cultivation_calender, Product

from jalali_date import datetime2jalali


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
    image = serializers.ImageField(use_url=True)
    uploaded_at = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = "__all__"

    def get_uploaded_at(self, obj):
        return datetime2jalali(obj.uploaded_at).strftime("%Y/%m/%d %H:%M:%S")


class JobSerializer(serializers.ModelSerializer):
    # field = serializers.PrimaryKeyRelatedField(queryset=Field.objects.all())
    field = FieldSerializer(read_only=True)
    # costs = serializers.PrimaryKeyRelatedField(
    #     queryset=Cost.objects.all(), required=False, allow_null=True
    # )
    costs = CostSerializer(read_only=True, many=True)
    # notes = serializers.PrimaryKeyRelatedField(
    #     queryset=Note.objects.all(), required=False, many=True
    # )
    notes = NoteSerializer(read_only=True, many=True)
    # images = serializers.PrimaryKeyRelatedField(
    #     queryset=Image.objects.all(), required=False, many=True
    # )
    images = ImageSerializer(read_only=True, many=True)

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
