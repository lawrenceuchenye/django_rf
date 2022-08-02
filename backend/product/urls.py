

from django.urls import path
from .views import ProductDetailAPIView,ProductCreateAPIView,ProductUpdateAPIView,ProductDeleteAPIView,ProductMixinView

urlpatterns=[
   path("<int:pk>/",ProductDetailAPIView.as_view()),
   path("<int:pk>/update/",ProductUpdateAPIView.as_view()),
   path("<int:pk>/delete/",ProductDeleteAPIView.as_view()),
   path("",ProductMixinView.as_view())
]
