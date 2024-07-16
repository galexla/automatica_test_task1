from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Branch, Visit
from .serializers import BranchSerializer, VisitSerializer


class BranchListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        worker = request.user
        branch = Branch.objects.filter(worker=worker)
        if not branch:
            return Response({"detail": "Нет привязанных филиалов"}, status=status.HTTP_404_NOT_FOUND)
        serializer = BranchSerializer(branch, many=True)
        return Response(serializer.data)


class VisitCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        worker = request.user
        branch_id = request.data.get('branch')
        latitude = request.data.get('latitude')
        longitude = request.data.get('longitude')

        try:
            branch = Branch.objects.get(id=branch_id, worker=worker)
        except Branch.DoesNotExist:
            return Response({"detail": "Несуществующий филиал или работник"},
                            status=status.HTTP_400_BAD_REQUEST)

        visit = Visit.objects.create(branch=branch, worker=worker, latitude=latitude, longitude=longitude)
        serializer = VisitSerializer(visit)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
