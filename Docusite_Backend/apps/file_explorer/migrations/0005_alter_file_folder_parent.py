# Generated by Django 4.2.1 on 2023-06-04 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('file_explorer', '0004_alter_file_url_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='folder_parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='file_explorer.file'),
        ),
    ]
