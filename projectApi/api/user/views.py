from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserCustomerSerializer
from .models import UserCustomer
class UserCustomerCreateView(APIView):
   def post(self, request):
       serializer = UserCustomerSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           """ 
           save on database
           """
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       else:
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserCustomerListView(APIView):
    def get(self, request):
        userList=UserCustomer.objects.all()
        serializer = UserCustomerSerializer(userList, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class UserCustomerDetailView(APIView):
    def get(self, request, pk):
        user=UserCustomer.objects.get(id=pk)
        serializer=UserCustomerSerializer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class UserCustomerUpdateView(APIView):
    def put(self, request, pk):
        user=UserCustomer.objects.get(id=pk)#rechercher l'objet dans le base 
        serializer=UserCustomerSerializer(user, data=request.data)#updatte 
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self ,request ,pk):
        user=UserCustomer.objects.get(id=pk)#rechercher l'objet dans le base
        serializer=UserCustomerSerializer(user, data=request.data,partial=True)#updatte
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class UserCustomerDeleteView(APIView):
    def delete(self, request, pk):
        user=UserCustomer.objects.get(id=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    