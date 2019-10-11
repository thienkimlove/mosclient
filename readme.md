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


### Re install 

* Install SSL for `mqtt.scoach.vn` using 

```text
 1999  sudo add-apt-repository ppa:certbot/certbot
 2000  sudo apt-get update
 2001  sudo apt-get install certbot
```

Edit `/etc/nginx/sites-enabled/backend.scoach.vn` to add `mqtt.scoach.vn` as domain.

Run `sudo certbot certonly  --standalone-supported-challenges http-01 -d mqtt.scoach.vn`

to get SSL files and add to crontab

`15 3    * * *   root    certbot renew --noninteractive --post-hook "systemctl restart mosquitto"`




Config mosquitto host and port

`vim /etc/mosquitto/conf.d/default.conf`


```text
allow_anonymous false
password_file /etc/mosquitto/passwd
listener 1883 localhost

listener 8883
certfile /etc/letsencrypt/live/mqtt.scoach.vn/cert.pem
cafile /etc/letsencrypt/live/mqtt.scoach.vn/chain.pem
keyfile /etc/letsencrypt/live/mqtt.scoach.vn/privkey.pem


listener 8083
protocol websockets
certfile /etc/letsencrypt/live/mqtt.scoach.vn/cert.pem
cafile /etc/letsencrypt/live/mqtt.scoach.vn/chain.pem
keyfile /etc/letsencrypt/live/mqtt.scoach.vn/privkey.pem
```



```text
 1999  sudo add-apt-repository ppa:certbot/certbot
 2000  sudo apt-get update
 2001  sudo apt-get install certbot
 2002  sudo certbot certonly --standalone --standalone-supported-challenges http-01 -d mqtt.scoach.vn
 
 2006  vim /etc/mosquitto/conf.d/default.conf 
 2007  service mosquitto restart
 2008  service ufw status
 2009  sudo ufw allow 8083
 2010  sudo ufw allow 8883
 2011  mosquitto_pub -h mqtt.scoach.vn -t test -m "hello again" -p 8883 --capath /etc/ssl/certs/ -u "admin" -P "tieungao"
 
 2017  cd /var/log/mosquitto/
 2018  ls
 2019  cat mosquitto.log 
 2020  cd /etc/letsencrypt/
 2021  ls
 2022  cd live
 2023  sudo ufw allow http
 
 2038  vim backend.scoach.vn 
 2039  nginx -t
 2040  service nginx reload
 2041  cat backend.scoach.vn 
 2042  sudo certbot certonly  --standalone-supported-challenges http-01 -d mqtt.scoach.vn
 2043  service mosquitto restart
 
 2064  service mosclient status
 2065  service mosclient start
 2066  service mosclient status
```

* Ok at the end we have 2 instances : python run as service `service mosclient status`

and `backend.scoach.vn/admin` as Laravel Backend.

* Testing using `https://www.eclipse.org/paho/clients/js/utility/` port 8083, path : ws, user and pass.


### Error may got

`https://askubuntu.com/questions/759071/cant-update-upgrade-du-to-could-not-execute-apt-key-to-verify-signature`

`https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-the-mosquitto-mqtt-messaging-broker-on-ubuntu-16-04`