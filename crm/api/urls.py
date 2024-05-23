from django.urls import include, path
from .views import GreetingsCreate, GreetingsList


urlpatterns = [
    path('create/', GreetingsCreate.as_view(), name='create-customer'),
    path('greetings/', GreetingsList.as_view()),
    # path('<int:pk>/', CustomerDetail.as_view(), name='retrieve-customer'),
    # path('update/<int:pk>/', CustomerUpdate.as_view(), name='update-customer'),
    # path('delete/<int:pk>/', CustomerDelete.as_view(), name='delete-customer')
]
