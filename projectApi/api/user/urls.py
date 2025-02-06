from django.urls import path,include
from .views import UserCustomerCreateView,UserCustomerListView,UserCustomerDetailView,UserCustomerUpdateView,UserCustomerDeleteView
urlpatterns = [
    
    path('user-create/', UserCustomerCreateView.as_view()),
    path('user-list',UserCustomerListView.as_view(), name="list user"),
    path('user-detail/<int:pk>/',UserCustomerDetailView.as_view(),name="user-detail"),
    path('use-update/<int:pk>/',UserCustomerUpdateView.as_view(),name="user-update"),
    path('use-delete/<int:pk>/',UserCustomerDeleteView.as_view(),name="userdelete"),
    ]