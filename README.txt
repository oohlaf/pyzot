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

- ./bin/initialize_PyZot_db development.ini

Starting PyZot for Development
------------------------------

You can choose between pserve and uWSGI

For pserve execute

- ./bin/pserve etc/development.ini

For uWSGI

- ./bin/uwsgi etc/development.ini

Configure your webserver (i.e., Nginx or Apache) to forward the requests to
pserve or connect to the uWSGI socket in var/run.

