from django.contrib import admin
from django.urls import path
from testapp.views import *

urlpatterns = [
    path("Dropdown1InfoGetApi/", Dropdown1InfoGetApi.as_view(), name="Dropdown1InfoGetApi"),
    path("Dropdown2InfoGetApi/", Dropdown2InfoGetApi.as_view(), name="Dropdown2InfoGetApi"),
    path("Dropdown3InfoGetApi/", Dropdown3InfoGetApi.as_view(), name="Dropdown3InfoGetApi")
    # path('admin/', admin.site.urls),
    # path('testapp/', include("testapp.urls")),

]