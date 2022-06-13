from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import EmployeeModel
from .serializers import GetEmployeeSerializer,  PostEmployeeSerializer



# Create your views here.
class GetEmployeesView(APIView):

     permission_classes = []

     def get(self, request, format=None):
        employees = EmployeeModel.objects.all()
        serializer = GetEmployeeSerializer
        if serializer.is_valid:
            data = serializer(employees, many=True).data
            return Response(
                data=sorted(data, key=lambda d: d['reg_number'], reverse=False),
                status=200
            )
        return Response(serializer.errors, status=400)
        


class GetEmployeeView(APIView):

    permission_classes = []

    def get(self, request, pk, format=None):
        employee = EmployeeModel.objects.get(id=pk)
        serializer = GetEmployeeSerializer
        if serializer.is_valid:
            data = serializer(employee, many=False).data
            if data:
                return Response(data, status=200)
        return Response(serializer.errors, status=400)



class PostEmployeeView(APIView):

     permission_classes = []

     def post(self, request, format=None):
        serializer = PostEmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data=dict(
                    status='success',
                    message='Employee is successfully created.'
                ),
                status=200)
        return Response(data=dict(status='error', message=serializer.errors), status=400)



class UpdateEmployeeView(APIView):

     permission_classes = []

     def put(self, request, pk, *args, **kwargs):
        comment = EmployeeModel.objects.get(pk=pk)
        data = request.data
        serializer = PostEmployeeSerializer
        serializer = serializer(instance=comment, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                data=dict(
                    status="success",
                    message=f"Employee with id {pk} is successfully updated!"
                ),
                status=200)
        return Response(
            data=dict(
                status="Failed",
                message=f"Employee with id {pk} is not successfully updated!"
            ),
            status=400)





class DeleteEmployeeView(APIView):

     permission_classes = []

     def delete(self, request, pk, *args, **kwargs):
        comment = EmployeeModel.objects.get(pk=pk)
        comment.delete()
        return Response(
            data=dict(
                status="success",
                message=f"Employee with id {pk} is successfully deleted!"
            ),
            status=200)