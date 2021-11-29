import traceback

from django.shortcuts import render

# Create your views here.
from django.views import View
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from contacts.models import Contact,ContactPhone,ContactEmail
from contacts.serializer import ContactSerializer, NewContactSerializer,NewEmailSerializer,NewPhoneSerializer, PhoneSerializer, EmailSerializer

# View for showing contact pages
class ViewList(View):
    template_name = 'contacts/MyContacts.html'

    def get(self, request):
        contacts = Contact.objects.filter(user=request.user)
        return render(request, self.template_name, {"no_data":"no_data" })


# View for Reatrieving use contacts
class ViewContacts(APIView):
    def get(self,request):
        try:
            contacts=Contact.objects.filter(user=request.user)
            return Response(data=ContactSerializer(contacts,many=True).data, status=status.HTTP_200_OK)
        except Exception as e:
            print(traceback.format_exc())
            return Response(data={"erro occurred try again"}, status=status.HTTP_400_BAD_REQUEST)

# View for deleting and creating contact
class CreateContact(APIView):
    def post(self,request):
        try:
            serialized_data=NewContactSerializer(data=request.data)
            if serialized_data.is_valid():
                contact=Contact()
                contact.user=request.user
                contact.firstName=serialized_data.validated_data.get("firstName")
                contact.lastName=serialized_data.validated_data.get("lastName")
                contact.save()
                return Response(data={"msg":"Success"},status=status.HTTP_200_OK)
            else:
                return Response(data=serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(data={"msg","error"}, status=status.HTTP_400_BAD_REQUEST)
    def put(self,request):

        try:

            serialized_data = NewContactSerializer(data=request.data)
            if serialized_data.is_valid():

                contact=Contact.objects.get(uuid=serialized_data.validated_data.get("uuid"))
                contact.firstName = serialized_data.validated_data.get("firstName")
                contact.lastName = serialized_data.validated_data.get("lastName")
                contact.save()
                return Response(data={"msg": "Success"}, status=status.HTTP_200_OK)
            else:
                return Response(data=serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:

            return Response(data={"msg", "error"}, status=status.HTTP_400_BAD_REQUEST)

# View for deleting contacts
class DeleteContact(APIView):
    def get(self,*args, **kwargs):
        try:
            contact = Contact.objects.get(uuid=kwargs["uuid"])
            contact.delete()
            return Response(data={"msg": "Success"}, status=status.HTTP_200_OK)
        except Exception as e:

            return Response(data={"msg", "error"}, status=status.HTTP_400_BAD_REQUEST)


# Save contact numbers
class HandlePhone(APIView):
    def post(self,request,**kwargs):
        try:
            serialized_data = NewPhoneSerializer(data=request.data)
            if serialized_data.is_valid():

                phone=ContactPhone()
                contact = Contact.objects.get(uuid=serialized_data.validated_data.get("contact_uuid"))
                if ContactPhone.objects.filter(contact=contact,phone=serialized_data.validated_data.get("phone")).exists():
                    return Response(data={"msg": "The phone (" +serialized_data.validated_data.get("phone")+ ") already exist on selected contact"}, status=status.HTTP_400_BAD_REQUEST)
                phone.contact=contact
                phone.phone=serialized_data.validated_data.get("phone")
                phone.save()
                return Response(data={"msg": "Success"}, status=status.HTTP_200_OK)
            else:
                return Response(data=serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(str(e))
            return Response(data={"msg": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    def get(self,*args,**kwargs):
        try:
            contact = Contact.objects.get(uuid=kwargs["contact_uuid"])
            emails=ContactPhone.objects.filter(contact=contact);
            return Response(data=PhoneSerializer(emails,many=True).data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data=[], status=status.HTTP_400_BAD_REQUEST)


# Save contact emails
class HandleEmail(APIView):
    def post(self,request,**kwargs):
        try:
            serialized_data = NewEmailSerializer(data=request.data)
            if serialized_data.is_valid():
                email=ContactEmail()
                contact = Contact.objects.get(uuid=serialized_data.validated_data.get("contact_uuid"))
                if ContactEmail.objects.filter(contact=contact,email=serialized_data.validated_data.get("email")).exists():
                    return Response(data={"msg": "The Email (" +serialized_data.validated_data.get("email")+ ") already exist on selected contact"}, status=status.HTTP_400_BAD_REQUEST)
                email.contact=contact
                email.email=serialized_data.validated_data.get("email")
                email.save()
                return Response(data={"msg": "Success"}, status=status.HTTP_200_OK)

            else:
                return Response(data=serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(str(e))
            return Response(data={"msg": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    def get(self,*args,**kwargs):
        try:
            contact = Contact.objects.get(uuid=kwargs["contact_uuid"])
            emails=ContactEmail.objects.filter(contact=contact);
            return Response(data=EmailSerializer(emails,many=True).data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data=[], status=status.HTTP_400_BAD_REQUEST)

























