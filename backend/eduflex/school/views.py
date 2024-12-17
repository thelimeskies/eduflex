from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from .models import School, SchoolClass, SchoolCategory, SchoolFee


class SchoolOnboardingView(views.APIView):
    serializer_class = serializers.SchoolOnboardingSerializer

    def post(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SchoolListView(views.APIView):
    serializer_class = serializers.SchoolSerializer

    def get(self, request):
        schools = School.objects.all()
        serializer = self.serializer_class(schools, many=True)
        return Response(serializer.data)


class SchoolClassView(views.APIView):
    serializer_class = serializers.SchoolClassSerializer

    def get(self, request, school_id):
        school = School.objects.get(id=school_id)
        classes = SchoolClass.objects.filter(school=school)
        if not classes:
            return Response(
                {"message": "No classes found."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.serializer_class(classes, many=True)
        return Response(serializer.data)

    def post(self, request, school_id):
        school = School.objects.get(id=school_id)
        serializer = self.serializer_class(
            data=request.data, context={"request": request, "school": school}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SchoolFeeView(views.APIView):
    serializer_class = serializers.SchoolFeeSerializer

    def get(self, request, school_id):
        school = School.objects.get(id=school_id)
        classes = SchoolClass.objects.filter(school=school)
        fees = SchoolFee.objects.filter(school_class__in=classes)
        if not fees:
            return Response(
                {"message": "No fees found."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.serializer_class(fees, many=True)
        return Response(serializer.data)

    def post(self, request, school_id):
        school = School.objects.get(id=school_id)
        classes = SchoolClass.objects.filter(school=school)
        fees = SchoolFee.objects.filter(school_class__in=classes)
        if fees:
            return Response(
                {"message": "Fees already exist."}, status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
