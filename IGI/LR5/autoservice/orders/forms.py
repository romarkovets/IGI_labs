from django import forms
from .models import Order


class ReviewForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Содержание'
            }
        )
    )
    score = forms.IntegerField(
        min_value=1,
        max_value=10,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Оценка'
            }
        )
    )

    class Meta:
        model = Order
        fields = ('description', 'score')

