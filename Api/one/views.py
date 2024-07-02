from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Api
from .serializers import Details

# Create your views here.
class Fly(APIView):
    def get(self,r):
        fdetails = Api.objects.all()
        obj = Details(fdetails, many=True)
        return Response(obj.data)

    def post(self,r):
        serobj = Details(data = r.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data,status=status.HTTP_201_CREATED)
        return Response(serobj.errors, status=status.HTTP_400_BAD_REQUEST)

class FlightUpdate(APIView):
     def put(self, r, pk):
         fdetails = Api.objects.get(pk=pk)
         serobj = Details(fdetails, data=r.data)
         if serobj.is_valid():
             serobj.save()
             return Response(serobj.data, status=status.HTTP_201_CREATED)
         return Response(serobj.errors, status=status.HTTP_400_BAD_REQUEST)


     def delete(self, r, pk):
         fdetails = Api.objects.get(pk=pk)
         fdetails.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)




