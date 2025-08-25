from django import forms

class TriangleForm(forms.Form):
    x1 = forms.FloatField(label="X1")
    y1 = forms.FloatField(label="Y1")
    x2 = forms.FloatField(label="X2")
    y2 = forms.FloatField(label="Y2")
    x3 = forms.FloatField(label="X3")
    y3 = forms.FloatField(label="Y3")
