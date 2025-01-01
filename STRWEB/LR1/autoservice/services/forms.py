from django import forms



class SearchForm(forms.Form):
    text = forms.CharField(max_length=100, required=False)
    sorting = forms.ChoiceField(choices=((1, "Сначала дешевые"), (2, "Сначала дорогие")))