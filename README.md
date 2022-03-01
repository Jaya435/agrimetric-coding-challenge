# Software Engineering Challenge

This repository contains a python project that used Django Rest Framework to create an API to list 
cafe orders and return a job schedule.

## Assumptions

1. Once an order has been served, Giovanni will update the order so that it is completed
2. The schedule will be recreated each time Giovanni gets it. The scheduled time will increment 
from then.
3. There is no frontend for the code, it is just an API
4. An sqlite3 database is acceptable (although it could be reconfigured for a PostgreSQL DB)

## Getting Started

These instructions will let you get a copy of the project up and running on your local machine for
development and testing purposes. See deployment for notes on how to deploy the project on a live
system.

### Prerequisites

You will need to run this programme using Python3. You can follow a guide here to install Python3
on your local machine https://installpython3.com/. Once Python3 is installed, you can run this
programme from within a virtual environment.

### Installing

A step by step series of examples that tell you how to get a development env running

Clone the repository onto your local machine
```
https://github.com/Jaya435/agrimetric-coding-challenge.git
```
Create your Python 3 virtual environment and install all requirements
```
make install
```
to activate the venv use:
```
make activate
```

To run a development web server
```
make runserver
```

To perform code formatting
```
make black
```
To perform code linting
```
make flake8
```

Other make commands to aid development are available on the commandline.


## Running the tests

The automated tests can be run using the below command:
```
make test
```

## Using the Web Server
Once you have run:
```
make runserver
```
The API endpoints can be viewed at:
```
http://localhost:8000/api/
```
To view a list of sandwiches
```
http://localhost:8000/api/sandwich
```
To view an order schedule
```
http://localhost:8000/api/orders
```

## Authors

* **Tom Richmond** - *Initial work* - [Jaya435](https://github.com/Jaya435/)
