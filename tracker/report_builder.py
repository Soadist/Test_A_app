import datetime as dt

from django.db.models import F
from django.db.models.aggregates import Count, Sum


class Stats:
    def __init__(self, **kwargs):
        self.count = kwargs['count']
        self.total_calories = kwargs['total_calories']
        self.total_distance = kwargs['total_distance']
        self.total_duration = kwargs['total_duration']
        self.hour = kwargs.pop('hour', None)
        self.day = kwargs.pop('day', None)


class ReportBuilder:
    def __init__(self, user, report_type=None):
        self.user = user
        self.report_type = report_type

    def get_statsreport(self):
        if self.report_type == 'hourly':
            return self.hourly_statsreport()
        if self.report_type == 'daily':
            return self.daily_statsreport()
        return self.simple_statsreport()

    def simple_statsreport(self):
        queryset = self.user.reports.all().aggregate(
            count=Count('id'),
            total_calories=Sum('calories'),
            total_distance=Sum('distance'),
            total_duration=Sum(F('end_datetime') - F('start_datetime'))
        )
        return Stats(**queryset)

    def hourly_statsreport(self):
        queryset = self.user.reports.filter(
            start_datetime__gte=dt.date.today()
        ).extra(
            {'hour': 'extract(hour from start_datetime)'}
        ).values(
            'hour'
        ).annotate(
            count=Count('id'),
            total_calories=Sum('calories'),
            total_distance=Sum('distance'),
            total_duration=Sum(F('end_datetime') - F('start_datetime'))
        )
        statsreport = []
        for result in queryset:
            statsreport.append(
                Stats(**result)
            )
        return statsreport

    def daily_statsreport(self):
        queryset = self.user.reports.filter(
            start_datetime__gte=dt.date.today().replace(day=1)
        ).extra(
            {'day': 'extract(day from start_datetime)'}
        ).values(
            'day'
        ).annotate(
            count=Count('id'),
            total_calories=Sum('calories'),
            total_distance=Sum('distance'),
            total_duration=Sum(F('end_datetime') - F('start_datetime'))
        )
        statsreport = []
        for result in queryset:
            statsreport.append(
                Stats(**result)
            )
        return statsreport
