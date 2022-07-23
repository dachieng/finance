from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
from users.models import User
from users.serializers import UserRegistraionSerializer, MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView



class UserRegistration(ListCreateAPIView):
    serializer_class = UserRegistraionSerializer
    queryset = User.objects.all()

    def list(self, request, *args, **kwargs):
        users = self.get_queryset()
        serilizer = self.get_serializer(users, many=True)
        return Response(serilizer.data, status=status.HTTP_200_OK)


    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# customizing token obtain vit
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
