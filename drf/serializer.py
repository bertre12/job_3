from rest_framework import serializers

from student.models import Student


class StudentSerializer(serializers.ModelSerializer):
    level = serializers.CharField(source='level.name', read_only=True)

    # Отображение данных.
    class Meta:
        model = Student
        fields = ['id', 'name', 'password', 'level']  # Отображение
        # выборочно.
        # fields = '__all__'  # Отображение всех данных.

