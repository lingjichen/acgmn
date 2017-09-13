#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(FlaskForm):
    email = StringField('邮件', validators=[Required(), Length(1,64),
                                          Email()])
    password = PasswordField('密码', validators=[Required()])
    remember_me = BooleanField('记住我')
    submit = SubmitField('登陆')


class RegistrationForm(FlaskForm):
    email = StringField('邮件', validators=[Required(), Length(1,64),
                                          Email()])
    username = StringField('用户名', validators=[
        Required(), Length(1,64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                         '用户名只能包含字母，数字，下划线，点号')
    ])
    password = PasswordField('密码', validators=[
        Required(), EqualTo('password2', message='密码必须一致')
    ])
    password2 = PasswordField('确认密码', validators=[Required()])
    submit = SubmitField('注册')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已注册.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已被使用')


class  ChangePasswordForm(FlaskForm):
    old_password = PasswordField('旧密码', validators=[Required()])
    password = PasswordField('新密码', validators=[
        Required(), EqualTo('password2', message='密码必须一致')
    ])
    password2 = PasswordField('确认密码', validators=[Required()])
    submit = SubmitField('更新密码')


class PasswordResetRequestForm(FlaskForm):
    email = StringField('邮件', validators=[Required(), Length(1,64),
                                          Email()])
    submit = SubmitField('重置密码')

class PasswordResetForm(FlaskForm):
    email = StringField('邮件', validators=[Required(), Length(1,64),
                                          Email()])
    password = PasswordField('新密码', validators=[
        Required(), EqualTo('password2', message='密码必须一致')])
    password2 = PasswordField('Confirm password', validators=[Required()])
    submit = SubmitField('重置密码')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first() is None:
            raise ValidationError('无效邮箱地址')


class ChangeEmailForm(FlaskForm):
    email = StringField('新邮箱', validators=[Required(), Length(1, 64),
                                                 Email()])
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField('更新邮箱地址')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first() is None:
            raise ValidationError('邮箱地址已注册')