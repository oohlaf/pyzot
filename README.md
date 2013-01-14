PyZot README
============

Installation
------------

- git clone https://github.com/oohlaf/pyzot.git PyZot

- virtualenv PyZot

- cd PyZot

- . bin/activate

- python bootstrap.py -t

- ./bin/buildout

- ./bin/initialize_PyZot_db etc/development.ini

Starting PyZot for Development
------------------------------

You can choose between pserve and uWSGI

For pserve execute

- ./bin/pserve etc/development.ini

For uWSGI, either start

- ./bin/uwsgi --ini-paste etc/development.ini

- ./bin/uwsgi --ini-paste-logged etc/development.ini

The latter will log every request made according to the logging settings in
development.ini.

Next, configure your webserver (i.e., Nginx or Apache) to forward the requests to
pserve or connect to the uWSGI socket in var/run.

