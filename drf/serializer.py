from rest_framework import serializers

from student.models import Student, Level


class StudentSerializer(serializers.ModelSerializer):
    # Поле для отображения уровня доступа.
    level_name = serializers.CharField(source='level.name', read_only=True)
    # Поле для выбора уровня доступа при регистрации.
    level = serializers.PrimaryKeyRelatedField(queryset=Level.objects.all(),
                                               write_only=True)

    # Отображение данных.
    class Meta:
        model = Student
        # Отображение выборочно.
        fields = ['id', 'name', 'password', 'level', 'level_name']
        # Поле только для записи данных, но не для отображения через API.
        extra_kwargs = {
            'level': {'write_only': True}
        }
        # Отображение всех данных.
        # fields = '__all__'


class StudentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # Поля для редактирования.
        fields = ['password', 'nickname_tg', 'nickname_inst', 'status']
