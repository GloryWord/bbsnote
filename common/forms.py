from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    # 필수 값으로 두고 싶은 변수는 이곳 Meta 위에 적는다. 지금은 email이 필수값이 된다.
    class Meta:
        model = User
        fields = ("username","email") # 수업 때 여기에 first_name, last_name을 추가했다. 