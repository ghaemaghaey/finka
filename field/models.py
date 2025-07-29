from django.db import models


# Create your models here.
class Field(models.Model):
    name = models.CharField(max_length=255)
    geography = models.JSONField(default=dict)

    def __str__(self):
        return self.name


class Note(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content[:60]


class Cost(models.Model):
    name = models.CharField(max_length=255)
    amount = models.BigIntegerField(default=0)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to="images/")
    comment = models.TextField(default="")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.name


class Voice(models.Model):
    voice = models.FileField(upload_to="audios/", null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.voice.name:
            return self.voice.name
        else:
            return "null"


class Job(models.Model):
    TYPE_CHOICES = [
        ("Irrigating", "IRRIGATING"),
        ("Planting", "PLANTING"),
        ("PrePlanting", "PREPLANTING"),
        ("Fertilizing", "FERTILIZING"),
        ("Pruning", "PRUNING"),
        ("Harvesting", "HARVESTING"),
    ]
    type = models.CharField(max_length=15, choices=TYPE_CHOICES, default="Irrigating")
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    made_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    status = models.BooleanField()
    costs = models.ForeignKey(Cost, on_delete=models.SET_NULL, null=True, blank=True)
    notes = models.ForeignKey(Note, on_delete=models.SET_NULL, null=True, blank=True)
    voices = models.ForeignKey(Voice, on_delete=models.SET_NULL, null=True, blank=True)
    images = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.type


class Cultivation_calender(models.Model):
    calender = models.JSONField(default=dict)


class Product(models.Model):
    name = models.CharField(max_length=255)
    cultivation_days = models.IntegerField()
    cultivation_calender = models.OneToOneField(
        Cultivation_calender, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
