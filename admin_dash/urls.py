from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.admin_home,name="admin_home"),
    path('admin_car/', views.admin_car, name="admin_car"),
    path('admin_add_carmodel/', views.admin_add_carmodel, name='admin_add_carmodel'),
    path("admin_add_carmodel_validation/", views.admin_add_carmodel_validation, name = "admin_add_carmodel_validation"),
    path("add_car/", views.add_car, name = "add_car"),
    path("admin_add_car_validation/", views.admin_add_car_validation, name = "admin_add_car_validation"),
    path('admin_account/',views.admin_account,name="admin_account"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
    path('delete-selected-cars/', views.delete_selected_cars, name='delete_selected_cars'),
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

