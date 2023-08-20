# Object Relational Mapping
> Each file in this repository holds code that illustrates an essential concept of programming,
> specific to databases and uses MySQLdb and sqlAlchemy with Python scripts

### Resources
[ORMs](https://www.fullstackpython.com/object-relational-mappers-orms.html), [SQLAlchemy](https://www.fullstackpython.com/sqlalchemy.html), [MySQLdb documentation](https://mysqlclient.readthedocs.io/), [Python MySQL documentation](http://www.mikusa.com/python-mysql-docs/index.html), [SQLAlchemy documentation](http://docs.sqlalchemy.org/en/latest/orm/tutorial.html), [prevent SQL injections](http://bobby-tables.com/python)

### Environment
* Language: Python 3.853
* Databases: MySQL 5.7, MySQLdb v2.0.x, sqlAlchemy v1.4.x
* OS: Ubuntu 20.04 LTS
* Compiler: python3
* Style guidelines: [PEP 8 (version 1.7) for Python 3.5](https://www.python.org/dev/peps/pep-0008/) || [Google Style Python Docstrings](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)

MySQLdb
```
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.__version__ 
'(2, 0, 3, 'final', 0)'
```
Isntall SQLAlchemy
```
$ pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'
```
Also, you can have this warning message:
```
/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be re
moved in a future release.")                                                                                                                    
  cursor.execute(statement, parameters)  
You can ignore it.
```
---
### Authors
THEOPHILUS NYARKO-MENSAH [![K](https://github.com/KOBBY-IM)
