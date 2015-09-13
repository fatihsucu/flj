sudo apt-get install apache2
sudo apt-get install libapache2-mod-wsgi
sudo a2enmod wsgi

sudo apt-get install mongodb-server
sudo apt-get install python-pip
sudo apt-get install python-dev
sudo apt-get install supervisor
sudo apt-get install libxml2-dev
sudo apt-get install libxslt1-dev
sudo apt-get install zlib1g-dev
sudo apt-get install rabbitmq-server

sudo pip install flask
sudo pip install schema
sudo pip install colorlog
sudo pip install pillow
sudo pip install pymongo
sudo pip install arrow
sudo pip install scrapy
sudo pip install twisted
sudo pip install cssselect
sudo pip install lxml
sudo pip install w3lib
sudo pip install celery

sudo cp /flj/setup/apache-dev.conf /etc/apache2/sites-available/flj-dev.conf
sudo a2ensite flj-dev.conf
service apache2 restart