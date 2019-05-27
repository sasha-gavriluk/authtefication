from django.urls import path

from .views import *

urlpatterns = [
    path('', ArticleList.as_view(), name = 'list'),
    path('<int:pk>/', ArticleDetail.as_view(), name = "detail"),
    path('<int:pk>/edit/', ArticleUpdate.as_view(), name = "edit"),
    path('<int:pk>/delete/', ArticleDelete.as_view(), name = "delete"),
    path('new/', ArticleCreate.as_view(), name = "new")
]
