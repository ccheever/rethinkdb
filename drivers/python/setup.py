# Copyright 2010-2013 RethinkDB, all rights reserved.

from setuptools import setup

setup(name="rethinkdb"
      ,version = "1.12.0-0"
      ,description = "This package provides the Python driver library for the RethinkDB database server."
      ,url = "http://rethinkdb.com"
      ,maintainer = "RethinkDB Inc."
      ,maintainer_email = "bugs@rethinkdb.com"
      ,packages = ['rethinkdb']
      ,entry_points = {'console_scripts': [
          'rethinkdb-import = rethinkdb._import:main',
          'rethinkdb-dump = rethinkdb._dump:main',
          'rethinkdb-export = rethinkdb._export:main',
          'rethinkdb-restore = rethinkdb._restore:main']})
