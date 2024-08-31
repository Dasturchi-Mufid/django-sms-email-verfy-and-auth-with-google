from django.urls import path
from . import views

urlpatterns = [
    #sms verification
    path('send-sms-verification/', views.send_sms_verification, name='send_sms_verification'),
    path('verify-sms-code/', views.verify_sms_code, name='verify_sms_code'),
    #company
    path('company/create/',views.create_company),
    path('company/last/',views.get_company),
    path('company/update/<str:code>/',views.update_company),
    #client
    path('client/create/',views.create_client),
    path('client/list/',views.get_clients),
    path('client/update/<str:code>/',views.update_client),
    path('client/<str:code>/projects/',views.get_client_projects),
    #contact
    path('contact/create/',views.create_contact),
    
    #employee
    # path('employee/create/',views.create_employee),
    # path('employee/last/',views.get_employee),
    # path('employee/update/<str:code>/',views.update_employee),
    # #invoice
    # path('invoice/create/',views.create_invoice),
    # path('invoice/last/',views.get_invoice),
    # path('invoice/update/<str:code>/',views.update_invoice),
    # #product
    # path('product/create/',views.create_product),
    # path('product/last/',views.get_product),
    # path('product/update/<str:code>/',views.update_product),
    # #purchase
    # path('purchase/create/',views.create_purchase),
]
