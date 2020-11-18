from django.db import models
from django.conf import settings
from django.utils import timezone
from administration_app.models import Subjects
from users_app.models import MyUser

# Create your models here.


def upload_folder(instance, filename):
    return settings.MEDIA_ROOT + str(instance.subject.subject) + "/" + filename


class Files(models.Model):
    owner = models.ForeignKey(MyUser, on_delete=models.PROTECT)
    title = models.CharField(max_length=50, default="", null=True, blank=True)
    file = models.FileField(
        upload_to=upload_folder,
    )
    subject = models.ForeignKey(Subjects, on_delete=models.PROTECT)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.subject} {self.title}"
