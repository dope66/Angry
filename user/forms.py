from django import forms
from user.models import Member
from user.signupform.forms import UserCreationForm


class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = ""

    class Meta:
        model = Member
        fields = ['username', 'email', 'nickname', 'last_name', 'first_name']
        labels = {
            'username': '아이디',
            'email': '이메일',
            'nickname': '닉네임',
            'last_name': '이름',
            'first_name': ''
        }
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control w-50',
                    'placeholder': '이메일을 입력하세요'
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control w-50',
                    'placeholder': '아이디를 입력하세요'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control w-50',
                    'placeholder': '성을 입력하세요'
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control w-50',
                    'placeholder': '이름을 입력하세요'
                }
            ),
            'nickname': forms.TextInput(
                attrs={
                    'class': 'form-control w-50',
                    'placeholder': '닉네임을 입력하세요'
                }
            )
        }


class LoginForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = ""
        self.fields['password'].help_text = ""

    class Meta:
        model = Member
        fields = ['username', 'password']
        labels = {
            'username': '아이디',
            'password': '비밀번호'
        }
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control w-50',
                    'placeholder': '아이디를 입력하세요'
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control w-50',
                    'placeholder': '비밀번호를 입력하세요'
                }
            )
        }
