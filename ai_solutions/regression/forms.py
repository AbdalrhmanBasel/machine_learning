from django import forms

class LinearRegressionForm(forms.Form):
    x_value = forms.FloatField(label='X Value')
