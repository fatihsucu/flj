sudo apt-get install apache2
sudo apt-get install libapache2-mod-wsgi
sudo a2enmod wsgi

sudo apt-get install mongodb-server
sudo apt-get install python-pip
sudo apt-get install python-dev
sudo apt-get install supervisor

sudo pip install flask
sudo pip install schema
sudo pip install colorlog
sudo pip install pillow
sudo pip install pymongo

sudo cp /flj/setup/apache-dev.conf /etc/apache2/sites-available/flj-dev.conf
sudo a2ensite flj-dev.conf
service apache2 restart