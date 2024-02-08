from django import forms


class newEntryForm(forms.Form):
    title = forms.CharField(max_length=50)
    subtitle = forms.CharField(max_length=200)
    introduction = forms.CharField(widget=forms.Textarea)
    imgUrl = forms.ImageField()
    imgLogo= forms.ImageField()
    content_list_1 = forms.CharField(widget=forms.Textarea,required=False)
    content_list_2 = forms.CharField(widget=forms.Textarea,required=False)
    content_list_3 = forms.CharField(widget=forms.Textarea,required=False)
    content_list_4 = forms.CharField(widget=forms.Textarea,required=False)
    content_list_5 = forms.CharField(widget=forms.Textarea,required=False)
    resume = forms.CharField(widget=forms.Textarea)
    author = forms.CharField(max_length=30)
