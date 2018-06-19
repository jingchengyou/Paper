from django import forms


class RegisterForm(forms.Form):
    name = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=30)
    telephone = forms.CharField(max_length=15)  # 填入时需要验证合法性
    nickname = forms.CharField(max_length=30)  # 填入时需要验证合理性，如敏感词、字母开头等
    address = forms.CharField(max_length=100)


class NovelForm(forms.Form):
    title = forms.CharField(max_length=30)
    summary = forms.CharField(max_length=1000)
