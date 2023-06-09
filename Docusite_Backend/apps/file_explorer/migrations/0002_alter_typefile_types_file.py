# Generated by Django 4.2.1 on 2023-06-04 18:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('file_explorer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typefile',
            name='types',
            field=models.CharField(choices=[('VID', 'Video'), ('AUD', 'Audio'), ('COD', 'Plain text'), ('IMA', 'Image'), ('DOC', 'Documents'), ('FOL', 'Folder')], max_length=4, verbose_name='types of file'),
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100, verbose_name='File name')),
                ('url_file', models.URLField(verbose_name='File URL')),
                ('size_mb', models.FloatField(verbose_name='Size MB')),
                ('is_active', models.BooleanField(default=True)),
                ('folder_parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='file_explorer.file')),
                ('type_file', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='file_explorer.typefile', verbose_name='Type File')),
            ],
            options={
                'indexes': [models.Index(fields=['type_file', 'folder_parent', 'size_mb'], name='file_explor_type_fi_8e2077_idx')],
            },
        ),
    ]
