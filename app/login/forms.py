# -*- coding:utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError, SelectField
from wtforms.validators import Required, Length, Email, EqualTo


class LoginForm(FlaskForm):
	sex = SelectField('性别', coerce=str)
	email = StringField('邮箱', validators=[Length(4, message='长度必须大于4'), Email(message='你输入的不符合邮箱格式')])
	password = PasswordField('密码')

	remember = BooleanField('记住密码')
	submit = SubmitField('登入')


	def __init__(self, *args, **kwargs):
		super(LoginForm, self).__init__(*args, **kwargs)
		self.sex.choices = [("male", "男"), ("female", "女")]


	def validate_email(self, field):
		if self.email.data.endswith("163.com"):
			raise ValidationError("邮箱必须市163")