from django.urls import path
from .views import TrainModelView, PredictView

app_name = "regression"

urlpatterns = [
    path('train/', TrainModelView.as_view(), name='train_model'),
    path('predict/', PredictView.as_view(), name='predict'),
]
