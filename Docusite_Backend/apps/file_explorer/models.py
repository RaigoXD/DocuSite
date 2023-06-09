from django.db import models
from model_utils.models import TimeStampedModel
import uuid
# Create your models here.


class TypeFile(TimeStampedModel):
    VIDEO = "VID"
    AUDIO = "AUD"
    CODE = "COD"
    IMAGE = "IMA"
    DOCUMENTS = "DOC"
    FOLDER = "FOL"
    TYPES = [
        (VIDEO, "Video"),
        (AUDIO, "Audio"),
        (CODE, "Plain text"),
        (IMAGE, "Image"),
        (DOCUMENTS, "Documents"),
        (FOLDER, "Folder"),
    ]

    types = models.CharField(
        max_length=4,
        choices=TYPES,
        verbose_name="types of file",
        null=False
    )

    allow_formats = models.CharField(
        max_length=100,
        null=False,
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="active",
    )

    description = models.CharField(
        max_length=100,
        verbose_name="description",
        null=False
    )

    def __str__(self) -> str:
        return f"{self.types} --- {self.allow_formats[:10]}..."


class File(TimeStampedModel):
    uuid = models.UUIDField(
        db_index = True,
        default = uuid.uuid4,
        editable = False,
        unique = True,
        primary_key = True
    )

    folder_parent = models.ForeignKey(
        'self',
        on_delete = models.CASCADE,
        null = True,
        blank = True
    )

    type_file = models.ForeignKey(
        TypeFile,
        null = False,
        on_delete = models.PROTECT,
        verbose_name = "Type File"
    )

    name = models.CharField(
        max_length = 100,
        null=False,
        verbose_name="File name"
    )

    url_file = models.FileField(
        upload_to='files',
        verbose_name = "File URL",
        null = True,
        blank = True
    )

    size_mb = models.FloatField(
        verbose_name = "Size MB",
        null = True,
        blank= True
    )
    
    owner = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        verbose_name="Owner",
        null= False,
        blank=True
    )

    is_active = models.BooleanField(default = True)

    class Meta:
        indexes = [
            models.Index(fields=["type_file", "folder_parent", "size_mb"]),
        ]
        
    def __str__(self) -> str:
        return f"{self.name} {self.type_file.types}"