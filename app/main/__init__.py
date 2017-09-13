#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Blueprint


main = Blueprint('main', __name__)

from . import views, errors
from ..models import Permission

#巴Permission加入模板上下文？有疑问
@main.app_context_processor()
def inject_permissions():
    return dict(Permission=Permission)