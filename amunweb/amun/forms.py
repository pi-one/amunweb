from django import forms

class SearchForm(forms.Form):
	query = forms.CharField(label="Search for IP address:")
	query.widget.attrs['class'] = 'form-control'
	query.widget.attrs['size'] = 25
