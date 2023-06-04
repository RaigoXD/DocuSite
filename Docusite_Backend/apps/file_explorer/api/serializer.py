from rest_framework import serializers
from ..models import TypeFile, File


class TypeFileSerializer(serializers.ModelSerializer):

    types = serializers.SerializerMethodField()

    class Meta:
        model = TypeFile
        fields = ('id','types','allow_formats','description', 'is_active')
    
    def get_types(self, obj):
        return {
            'codigo': obj.types,
            'descripcion': obj.get_types_display()
        }


class FileListSerializer(serializers.ModelSerializer):
    
    type_file = serializers.SerializerMethodField()
    
    class Meta:
        model = File
        fields = ('uuid', 'name', 'url_file', 'size_mb', 'created', 'type_file')
        
    def get_type_file(self, obj):
        return obj.type_file.types


class FileCreateUpdateSerializer(serializers.ModelSerializer):
    
    folder_parent = serializers.SlugRelatedField(
        slug_field = 'uuid',
        queryset = File.objects.all(),
        allow_null = True
    )

    type_file = serializers.PrimaryKeyRelatedField(
        queryset = TypeFile.objects.all()
    )

    class Meta:
        model = File
        fields = ('folder_parent','type_file','name','url_file','size_mb')


class FileRetriveDeleteSerializer(serializers.ModelSerializer):

    type_file = TypeFileSerializer()

    class Meta:
        model = File
        fields = '__all__'
