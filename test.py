from kivy.app import App
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
import requests
import json
import os,ast
from kivy.factory import Factory


from kivy.config import ConfigParser
from kivy.properties import ObjectProperty


class Sign_in(Screen):
    login = ObjectProperty()
    password = ObjectProperty()

    def Sign_in_user(self):
        if self.login.text == '' or self.password.text == '':
            pass
        else:
            url = '127.0.0.1'
            headers = {
                'Content-type': 'application/json',
                'Accept': 'text/json',
                'Content-Encoding': 'utf-8'
            }
            data = {'user info':
                [
                    {
                        "login": "{}".format(self.login.text),
                        'password': '{}'.format(self.password.text),
                    }
                ],
                'login_in': 'yes'
            }
            answer = requests.post(url, data=json.dumps(data), headers=headers)
            if answer == '404':
                pass
            if answer == '200':
                pass


class Sign_up(Screen):
    fio = ObjectProperty()
    email = ObjectProperty()
    group = ObjectProperty()
    password = ObjectProperty
    password_return = ObjectProperty()

    def New_user(self):
        if self.email.text == '' or \
                self.group.text == '' or \
                self.fio.text == '' or \
                self.password.text == '' or \
                self.password_return == '':
            pass
        elif self.password_return.text != self.password.text:
            pass
        else:
            url = '127.0.0.1'
            headers = {
                'Content-type': 'application/json',
                'Accept': 'text/json',
                'Content-Encoding': 'utf-8'
            }
            data = {'user info':
                [
                    {
                        "FIO": "{}".format(self.fio.text),
                        'Email': '{}'.format(self.email.text),
                        'Password': '{}'.format(self.password.text),
                        'Group': '{}'.format(self.group.text)
                    }
                ],
                'registr': 'yes'
            }
            answer = requests.post(url, data=json.dumps(data), headers=headers)
            if answer == '404':
                pass
            if answer == '200':
                pass


class Menu(Screen):
    pass

pressentation = Builder.load_file('my.kv')


class Myapp(App):
    def __init__(self, **kvargs):
        super(Myapp, self).__init__(**kvargs)

        self.config = ConfigParser()
        self.screen_manager = Factory.ManagerScreens()
    def build(self):
        return self.screen_manager


if __name__ == "__main__":
    Myapp().run()
