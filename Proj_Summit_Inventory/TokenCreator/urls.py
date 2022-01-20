from rest_framework.authtoken import views
from django.urls import path
from . import views



# This service should have 4 endpoint(s) to generate a JWT token using a Secret Key
# Endpoint A - token with read_product permission
# Endpoint B - token with manage_product permission
# Endpoint C - token with both: read_product and manage_product permission
# Endpoint D - token with admin permission
# Token should be valid for 10 mins only  #####Trying as model method.
# The token should be stored in the DB  Cache
# Only one token should be valid at any point of time



#python manage.py createsuperuser --username Annias --email a@b.com
#python manage.py drf_create_token Annias
#http://127.0.0.1:8000/api/user_auth/read_product/ -H 'Authorization: Token 3c32af34607b9f02a0871ac222e16fd70d5947c9'
#token    3c32af34607b9f02a0871ac222e16fd70d5947c9

urlpatterns = [
    path('read_product/', views.ReadProductView.as_view(), name='read'), #ListView
    path('create/', views.CreateProduct.as_view(), name='create'),
    path('manage_product/<int:pk>/', views.UpdateProduct.as_view(), name='mang'),
    path('cr_admin/', views.CreateReadAdmin.as_view(), name='rest_adm'),
    path('ud_admin/<int:pk>/', views.DeleteProductAdmin.as_view())

]