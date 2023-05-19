from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from api.retirement.models import Retirement
from api.retirement.serializers import RetirementSerializer


# /api/v1/retirement/set/<uuid>
class RetirementCreate(APIView):
    """
    Create or update a user
    """

    serializer_class = RetirementSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, *args, **kwargs):
        uuid = self.kwargs["pk"]
        retirement = self.request.query_params["retirement"]
        choice = int(self.request.query_params["choice"])

        user, created = Retirement.objects.update_or_create(pk=uuid)

        serializer = RetirementSerializer(
            user,
            data={"uuid": uuid, "retirement": retirement},
            context={"request": self.request},
        )

        if serializer.is_valid():
            serializer.save()

            if created:
                return Response(serializer.data, status.HTTP_201_CREATED)
            return Response(serializer.data, status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# /api/v1/retirement/get/<uuid>
class RetirementRetrieve(generics.RetrieveAPIView):
    """
    Retrieve a user
    """

    serializer_class = RetirementSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Retirement.objects.all().filter(pk=self.kwargs["pk"])
