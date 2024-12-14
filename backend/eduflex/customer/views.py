from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from .models import Parents, Student, ParentKYC


class ParentOnboardingView(views.APIView):
    serializer_class = serializers.ParentOnboardingSerializer

    def post(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
