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
    field = serializers.PrimaryKeyRelatedField(queryset=Field.objects.all())

    costs = CostSerializer(read_only=True, many=True)
    cost_ids = serializers.PrimaryKeyRelatedField(
        queryset=Cost.objects.all(), many=True, write_only=True, required=False
    )

    notes = NoteSerializer(read_only=True, many=True)
    note_ids = serializers.PrimaryKeyRelatedField(
        queryset=Note.objects.all(), many=True, write_only=True, required=False
    )

    images = ImageSerializer(read_only=True, many=True)
    image_ids = serializers.PrimaryKeyRelatedField(
        queryset=Image.objects.all(), many=True, write_only=True, required=False
    )

    class Meta:
        model = Job
        fields = "__all__"

    def create(self, validated_data):
        print("validated_data:", validated_data)
        note_ids = validated_data.pop("note_ids", [])
        cost_ids = validated_data.pop("cost_ids", [])
        image_ids = validated_data.pop("image_ids", [])
        note_ids = [n.id if hasattr(n, "id") else n for n in note_ids]
        cost_ids = [c.id if hasattr(c, "id") else c for c in cost_ids]
        image_ids = [i.id if hasattr(i, "id") else i for i in image_ids]

        job = Job.objects.create(**validated_data)

        if note_ids:
            notes = Note.objects.filter(id__in=note_ids)
            job.notes.add(*notes)

        if cost_ids:
            costs = Cost.objects.filter(id__in=cost_ids)
            job.costs.add(*costs)

        if image_ids:
            images = Image.objects.filter(id__in=image_ids)
            job.images.add(*images)

        return job

    def update(self, instance, validated_data):
        note_ids = validated_data.pop("note_ids", None)
        cost_ids = validated_data.pop("cost_ids", None)
        image_ids = validated_data.pop("image_ids", None)

        if note_ids is not None:
            note_ids = [n.id if hasattr(n, "id") else n for n in note_ids]

        if cost_ids is not None:
            cost_ids = [c.id if hasattr(c, "id") else c for c in cost_ids]

        if image_ids is not None:
            image_ids = [i.id if hasattr(i, "id") else i for i in image_ids]

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if note_ids is not None:
            notes = Note.objects.filter(id__in=note_ids)
            instance.notes.set(notes)

        if cost_ids is not None:
            costs = Cost.objects.filter(id__in=cost_ids)
            instance.costs.set(costs)

        if image_ids is not None:
            images = Image.objects.filter(id__in=image_ids)
            instance.images.set(images)

        return instance


# class JobSerializer(serializers.ModelSerializer):
#     # field = serializers.PrimaryKeyRelatedField(queryset=Field.objects.all())
#     field = FieldSerializer(read_only=True)
#     # costs = serializers.PrimaryKeyRelatedField(
#     #     queryset=Cost.objects.all(), required=False, allow_null=True
#     # )
#     costs = CostSerializer(read_only=True, many=True)
#     # notes = serializers.PrimaryKeyRelatedField(
#     #     queryset=Note.objects.all(), required=False, many=True
#     # )
#     notes = NoteSerializer(read_only=True, many=True)
#     # images = serializers.PrimaryKeyRelatedField(
#     #     queryset=Image.objects.all(), required=False, many=True
#     # )
#     images = ImageSerializer(read_only=True, many=True)

#     class Meta:
#         model = Job
#         fields = "__all__"


class CultivationCalenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cultivation_calender
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    cultivation_calender = CultivationCalenderSerializer()

    class Meta:
        model = Product
        fields = "__all__"
