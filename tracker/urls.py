from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (ReportStats, ReportStatsDaily, ReportStatsHourly,
                    ReportViewSet)

router = DefaultRouter()
router.register('reports', ReportViewSet, basename='reports')

urlpatterns = [
    path('reports/stats/',
         ReportStats.as_view(), name='report_stats'),
    path('reports/stats/hourly/',
         ReportStatsHourly.as_view(), name='report_stats_hourly'),
    path('reports/stats/daily/',
         ReportStatsDaily.as_view(), name='report_stats_daily'),
    path('', include(router.urls))
]
