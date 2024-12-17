from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from .models import Parents, Student, ParentKYC, ParentCreditCapacityScore


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


class ChildrenView(views.APIView):
    serializer_class = serializers.ChildrenSerializer

    def get(self, request, parent_id):
        parent = Parents.objects.get(id=parent_id)
        children = Student.objects.filter(parent=parent)
        if not children:
            return Response(
                {"message": "No children found."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.serializer_class(children, many=True)
        return Response(serializer.data)

    def post(self, request, parent_id):
        parent = Parents.objects.get(id=parent_id)
        serializer = self.serializer_class(
            data=request.data, context={"request": request, "parent": parent}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ParentCreditAndCapacityScoreView(views.APIView):
    serializer_class = serializers.ParentCreditAndCapacityScoreSerializer

    def get(self, request, parent_id):
        parent = Parents.objects.get(id=parent_id)
        credit_capacity_score = ParentCreditCapacityScore.objects.get(parent=parent)

        serializer = self.serializer_class(credit_capacity_score)
        return Response(serializer.data)
