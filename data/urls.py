from django.urls import path,include
from . import views

urlpatterns = [
    path('insert/', views.employee_form,name='employee_insert'), # get and post req. for insert operation
    path('<int:id>/', views.employee_form,name='employee_update'), # get and post req. for update operation
    path('delete/<int:id>/',views.employee_delete,name='employee_delete'),
    path('employeelist/',views.employee_list,name='employee_list'), # get req. to retrieve and display all records
    path('assetslist/',views.assets_list,name='assets_list'),
    # ,
    path('',views.employee_list,name='employee_list'),
    path('assets/list/<int:id>',views.assets_delete,name='assets_delete'),
    path('assets/insert', views.assets_form,name='table_insert'), # get and post req. for insert operation
    path('<int:id>/update', views.assets_form,name='table_update')

]
