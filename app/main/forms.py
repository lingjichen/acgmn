#!/usr/bin/env python3
# -*- coding:utf-8 -*

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class NameForm(FlaskForm):
    name = StringField('你的名字是？', validators=[Required()])
    submit = SubmitField('提交')