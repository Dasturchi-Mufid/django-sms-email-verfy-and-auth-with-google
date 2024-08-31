from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from . import models
from . import serializers
from .send_sms import send_verification_code 




@api_view(['POST'])
def send_sms_verification(request):
    phone_number = request.data.get('phone_number')
    
    if not phone_number:
        return Response({'error': 'Phone number is required'}, status=status.HTTP_400_BAD_REQUEST)
    
    verification_code = send_verification_code(phone_number)
    
    # Store the verification code and phone number in the session or database
    request.session['verification_code'] = verification_code
    request.session['phone_number'] = phone_number
    
    return Response({'message': 'Verification code sent'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def verify_sms_code(request):
    entered_code = request.data.get('verification_code')
    
    if str(request.session.get('verification_code')) == entered_code:
        # Verification successful, handle post-verification logic here
        return Response({'message': 'Verification successful'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid verification code'}, status=status.HTTP_400_BAD_REQUEST)


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def create_company(request):
    serializer = serializers.CompanySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def get_company(request):
    company = models.Company.objects.last()
    if company:
        serializer = serializers.CompanySerializer(company)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT','PATCH'])
def update_company(request,code):
    try:
        company = models.Company.objects.get(code=code)
    except models.Company.DoesNotExist:
        return Response({"error": "Company not found"}, status=status.HTTP_404_NOT_FOUND)

    partial = request.method == 'PATCH'
    serializer = serializers.CompanySerializer(company, data=request.data, partial=partial)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


@api_view(['POST'])
def create_client(request):
    serializer = serializers.ClientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_clients(request,code=None):
    clients = models.Client.objects.all()
    if code:
        try:
            clients = models.Client.objects.get(code=code)
        except models.Client.DoesNotExist:
            return Response({"error": "Company not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = serializers.ClientSerializer(clients,many=True)
    return Response(serializer.data)

@api_view(['PUT','PATCH'])
def update_client(request,code):
    try:
        client = models.Client.objects.get(code=code)
    except models.Client.DoesNotExist:
        return Response({"error": "Client not found"}, status=status.HTTP_404_NOT_FOUND)
    
    partial = request.method == 'PATCH'
    serializer = serializers.ClientSerializer(client, data=request.data, partial=partial)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_client_projects(request, code):
    try:
        client = models.Client.objects.get(code=code)
    except models.Client.DoesNotExist:
        return Response({"error": "Client not found"}, status=status.HTTP_404_NOT_FOUND)
    
    projects = client.projects
    serializer = serializers.ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_contact(request):
    serializer = serializers.ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_contacts(request, code=None):
    contacts = models.Contact.objects.all()
    if code:
        contacts = contacts.get(code=code)
        contacts.is_show = True
        contacts.save()
    serializer = serializers.ContactSerializer(contacts, many=True)
    return Response(serializer.data)





