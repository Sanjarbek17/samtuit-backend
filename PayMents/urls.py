from .views import PaymentView, Delet_Payment
from django.urls import path

urlpatterns = [
    path('payment/', PaymentView.as_view()),
    path('payment/<int:fk>/', PaymentView.as_view()),
    path('payment/delete/<int:pk>/', Delet_Payment.as_view()),
]
