
from django.urls import path
from . import views
from .views import ViewList, ViewContacts, CreateContact, DeleteContact, HandleEmail,HandlePhone

app_name = 'contacts'
urlpatterns = [
    path('',ViewList.as_view() , name='contacts'),
    path("all",ViewContacts.as_view(),name="view_contacts"),
    path("create/",CreateContact.as_view(), name="create_contact"),
    path("delete/<str:uuid>",DeleteContact.as_view(),name="delete_contact"),
    path("phones/<str:contact_uuid>",HandlePhone.as_view(),name="handle_phone"),
    path("emails/<str:contact_uuid>",HandleEmail.as_view(),name="handle_email")

]