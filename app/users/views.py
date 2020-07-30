
from django.shortcuts import get_object_or_404
from users.serializers import CandidateSerializer
from users.models import Candidate
from rest_framework import viewsets


class CandidateViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Candidate instances.
    """
    serializer_class = CandidateSerializer
    queryset = Candidate.objects.all()
