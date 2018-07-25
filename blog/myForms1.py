from django import forms
from django.forms import widgets
from blog.models import UserInfo
from django.core.exceptions import ValidationError


class UserForm(forms.Form):
    user = forms.CharField(max_length=32,label="用户名",
                           error_messages={"required": "该字段不能为空"},
                           widget=widgets.TextInput(attrs={"class": "form-control"}))
    pwd = forms.CharField(max_length=32, label="密码",
                          widget=widgets.PasswordInput(attrs={"class": "form-control"}))
    re_pwd = forms.CharField(max_length=32, label="确认密码",
                          widget=widgets.PasswordInput(attrs={"class": "form-control"}))
    email = forms.EmailField(max_length=32, label="邮箱",
                          widget=widgets.EmailInput(attrs={"class": "form-control"}))

    # 用户名的认证
    def clean_user(self):
        user = self.cleaned_data.get('user')

        user_obj = UserInfo.objects.filter(username=user).first()
        if not user_obj:
            return user
        else:
            raise ValidationError('该用户名已经注册')
            # return ValidationError('该用户名已经注册')   # 不能用出现bug

    # 密码
    def clean(self):
        pwd = self.cleaned_data.get("pwd")
        re_pwd = self.cleaned_data.get("re_pwd")

        if pwd and re_pwd:
            if pwd == re_pwd:
                return self.cleaned_data
            else:
                # return ValidationError("两次密码不一致!")
                raise ValidationError("两次密码不一致!")
        else:
            return self.cleaned_data
