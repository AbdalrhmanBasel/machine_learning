from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import torch

from .models.linear_regression import LinearRegressionModel, criterion, optimizer, model
from .serializers import TrainSerializer, PredictSerializer

class TrainModelView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TrainSerializer(data=request.data)
        if serializer.is_valid():
            x_values = serializer.validated_data['x_values']
            y_values = serializer.validated_data['y_values']
            
            inputs = torch.tensor(x_values, dtype=torch.float32).view(-1, 1)
            labels = torch.tensor(y_values, dtype=torch.float32).view(-1, 1)

            model.train()
            for epoch in range(100):
                optimizer.zero_grad()
                outputs = model(inputs)
                loss = criterion(outputs, labels)
                loss.backward()
                optimizer.step()

            return Response({'status': 'Model trained'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PredictView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PredictSerializer(data=request.data)
        if serializer.is_valid():
            x_value = serializer.validated_data['x_value']
            model.eval()
            with torch.no_grad():
                x_tensor = torch.tensor([[x_value]], dtype=torch.float32)
                y_pred = model(x_tensor).item()
            return Response({'prediction': y_pred}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
