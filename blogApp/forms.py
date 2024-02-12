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

class commentForm(forms.Form):
    comment = forms.CharField(max_length=500)

class signupForm(forms.Form):
    name = forms.CharField(max_length=50)
    lastname = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=254)
    password = forms.CharField(max_length=50)

class loginForm(forms.Form):
    email = forms.EmailField(max_length=254)
    password = forms.CharField(max_length=50)
