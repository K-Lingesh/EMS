from django.urls import path # type: ignore
from .views import *

urlpatterns =[
    path('home/' , HomePage),
    path('add/' , Addpage),
    path('edit/' , Editpage),
    path('view/' , Viewpage),
    path('edit/delete/<int:id>/' , DeleteEmployee, name='employee_del'),
    path('edit/update/<int:id>/' , UpdateEmployee, name='employee_upd'),

]