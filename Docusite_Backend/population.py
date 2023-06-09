import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Docusite.settings.local")
django.setup()

from apps.file_explorer.models import TypeFile

def populate_types_file():
    object1 = TypeFile(types= TypeFile.VIDEO,allow_formats= 'mp4',is_active= True,description= 'Type and format to video files')
    object1.save()
    object2 = TypeFile(types= TypeFile.AUDIO,allow_formats= 'mp3',is_active= True,description= 'Type and format to audio files')
    object2.save()
    object3 = TypeFile(types= TypeFile.CODE,allow_formats= 'py,txt',is_active= True,description= 'Type and format to text plain files')
    object3.save()
    object4 = TypeFile(types= TypeFile.IMAGE,allow_formats= 'png,jpeg,jpg',is_active= True,description= 'Type and format to image files')
    object4.save()
    object5 = TypeFile(types= TypeFile.DOCUMENTS,allow_formats= 'pdf',is_active= True,description= 'Type and format to document files')
    object5.save()
    object6 = TypeFile(types= TypeFile.FOLDER,allow_formats= 'folder',is_active= True,description= 'Type to folder')
    object6.save()

if __name__ == '__main__':
    populate_types_file()