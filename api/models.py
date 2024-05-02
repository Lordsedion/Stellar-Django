from django.db import models
import string, random
from djongo import models as mod

def generate_id():
    length = 20
    while True:
        id = "".join(random.choices(string.ascii_uppercase + string.ascii_lowercase +string.digits, k=length))
        if TextDefault.objects.filter(rec=id).count() == 0:
            break
    return id

def user_directory_path(instance, file_name):
    return f"user_{instance.user.id}_{file_name}"


class TextDefault(models.Model):
    rec =models.CharField(max_length=20, default=generate_id, primary_key=True)
    name = models.CharField(max_length=25)
    text = models.CharField(max_length=5000)
    speaker = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)


class FileDefault(models.Model):
    rec =models.CharField(max_length=20, default=generate_id, primary_key=True)
    name = models.CharField(max_length=25)
    text_file = mod.FileField(upload_to="api/")
    speaker = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

class AudioModel(models.Model):
    audio_id = models.CharField(max_length=20)
    # file = models.FileField()
