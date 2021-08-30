from rest_framework import mixins, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Report
from .report_builder import ReportBuilder
from .serializers import (ReportCreateSerializer, ReportSerializer,
                          StatsDailySerializer, StatsHourlySerializer,
                          StatsSerializer)


class ReportViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin
):
    queryset = Report.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return user.reports.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ReportSerializer
        return ReportCreateSerializer


class ReportStats(APIView):
    report_type = None
    serializer = StatsSerializer
    many = False

    def get(self, request):
        user = request.user
        statsreport = ReportBuilder(user, self.report_type).get_statsreport()
        serializer = self.serializer(statsreport, many=self.many)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ReportStatsHourly(ReportStats):
    report_type = 'hourly'
    serializer = StatsHourlySerializer
    many = True


class ReportStatsDaily(ReportStats):
    report_type = 'daily'
    serializer = StatsDailySerializer
    many = True
