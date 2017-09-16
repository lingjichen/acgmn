#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import re
import unittest
from flask import url_for
from app import create_app, db
from app.models import User, Role


class FlaskClientTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        Role.insert_roles()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_home_page(self):
        response = self.client.get(url_for('main.index'))
        self.assertTrue(b'firends' in response.data)

    def test_register_and_login(self):
        #注册新用户
        response = self.client.post(url_for('auth.register'), data={
            'email': 'john@example.com',
            'username': 'john',
            'password': 'cat',
            'password2': 'cat',
        })
        self.assertTrue(response.status_code == 302)

        #使用新用户登录
        response = self.client.post(url_for('auth.login'), data={
            'email': 'john@example.com',
            'password': 'cat'
        }, follow_redirects=True)
        self.assertTrue(re.search(b'hello', response.data))
        self.assertTrue(
            b'you dont cnnfirm you count ' in response.data
        )

        #退出
        response = self.client.get(url_for('auth.logout'), follow_redirects=True)
        self.assertTrue(b'you log out' in response.data)