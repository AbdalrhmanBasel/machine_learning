from rest_framework import serializers

class TrainSerializer(serializers.Serializer):
    x_values = serializers.ListField(
        child=serializers.FloatField(), allow_empty=False)
    y_values = serializers.ListField(
        child=serializers.FloatField(), allow_empty=False)


    def validate(self, data):
        if len(data['x_values']) != len(data['y_values']):
            raise serializers.ValidationError("X values and Y values must have the same length.")
        return data
    
class PredictSerializer(serializers.Serializer):
    x_value = serializers.FloatField()