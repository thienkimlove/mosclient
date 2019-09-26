## Install Project

* virtualenv -p python3 venv

* source venv/bin/activate

* pip install django

* django-admin startproject project

* cd project

* python manage.py startapp core

## Paho MQTT client

`https://www.eclipse.org/paho/clients/python/docs/#subscribe-unsubscribe`

`https://eclipse.org/paho/clients/js/utility/`

`http://www.steves-internet-guide.com/client-connections-python-mqtt/`

`https://github.com/eclipse/paho.mqtt.python/issues/381`

## Deploy

`ln -s /var/www/html/mosclient/project/deploy/mosclient.service /etc/systemd/system/mosclient.service`

### Instruction

1. Kết nối với Server MQTT 

* Kết nối bằng giao thức `mqtt://` với địa chỉ `mqtt.scoach.vn` port 8883 với thông tin đăng nhập

```textmate
User: admin
Pass: tieungao

```
* Kết nối bằng giao thức websocket

```text
Host : mqtt.scoach.vn
Port : 8083
Path : ws

user and pass nhu tren

```
### Test info

Xem danh sach message tai `http://mosclient.scoach.vn/admin/core/message/`

Dang nhap voi tai khoan `admin/tieungao`