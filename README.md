lcdsysinfo-weather
==================

Put weather info in LCDsysinfo display. Borrowed from http://kontroller.blogspot.nl/2013/04/raspberry-pi-weather-station.html

uses yahoo weather. Code is already updated a bit.
Would be nice to do the API call in Python.

Requires a watchmousnkey file in the proper directory

Ansible:
use 
```
ansible-playbook ansible/playbooks/lcdinfo.yml -i ansible/hosts
```
