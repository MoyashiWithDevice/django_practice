from django.urls import path
from . import views

urlpatterns = [
    path("equips/", views.equip_list, name="equip_list"),
    path("add/", views.equip_create, name="equip_create"),
    path("edit/<int:equip_id>/", views.equip_update, name="equip_update"),
    path("delete/<int:equip_id>/", views.equip_delete, name="equip_delete"),
    path("restore/<int:equip_id>/", views.equip_restore, name="equip_restore")
]