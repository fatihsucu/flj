Start to contribute
===================

```sh
echo "192.168.34.10 flj.com flj" >> /etc/hosts
vagrant up
vagrant ssh
# the following lines must be run in your vagrant
cd setup
sudo ./setup.sh

```
And to test whether it works or not, go to your browser and hit to http://flj.com/api/jobs