from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer

import json
from app01 import models

clients = {}
usersList = {}


def getCookie(cookies):
    cookie_dic = {}
    cookies_arr = cookies.split(";")
    for c in cookies_arr:
        temp = c.split("=")
        cookie_dic[temp[0].replace(" ", "")] = temp[1]
    return cookie_dic


#至少以下三种方法
class ChatConsumer(WebsocketConsumer):
    #链接请求
    def websocket_connect(self, message):
        self.accept()  #允许创建链接

    #接受数据请求
    def websocket_receive(self, message):
        self.send("hello")

    #断开请求
    def websocket_disconnect(self, message):

        raise StopConsumer()