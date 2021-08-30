from django.core.exceptions import ValidationError
from rest_framework import serializers

from .models import Report


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = [
            'user',
            'start_datetime',
            'end_datetime',
            'activity_type',
            'distance',
            'calories'
        ]


class ReportCreateSerializer(ReportSerializer):

    def validate(self, attrs):
        if attrs['end_datetime'] <= attrs['start_datetime']:
            raise ValidationError(
                'Окончание активности не может наступить раньше начала'
            )
        if attrs['distance'] <= 0:
            raise ValidationError(
                'Дистанция должна быть больше 0'
            )
        if attrs['calories'] <= 0:
            raise ValidationError(
                'Кол-во калорий должно быть больше 0'
            )
        return super().validate(attrs)

    def create(self, validated_data):
        user = self.context.get('request').user
        report = Report.objects.create(
            user=user, **validated_data)
        report.save()
        return report

    class Meta(ReportSerializer.Meta):
        fields = [
            'start_datetime',
            'end_datetime',
            'activity_type',
            'distance',
            'calories'
        ]


class StatsSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    total_calories = serializers.IntegerField()
    total_distance = serializers.IntegerField()
    total_duration = serializers.DurationField()


class StatsHourlySerializer(StatsSerializer):
    hour = serializers.IntegerField()


class StatsDailySerializer(StatsSerializer):
    day = serializers.IntegerField()
