django-sql-stacktrace
=======================

.. image:: https://pypip.in/d/django-sql-stacktrace/badge.png
    :target: http://pypi.python.org/pypi/django-sql-stacktrace

Pluggable application, which puts a python stack trace in the SQL query as a comment (useful for debugging).

For more details see http://adw0rd.com/2012/django-sql-stacktrace/en/

After installed you can see in ``processlist`` a SQL-query and comment with python stack trace::

    watch -n1 mysqladmin processlist --verbose

Or you can see in a log files, such as ``log_slow_queries`` or ``log-bin`` (aka 'binlog').


How to install this wonderful package?
--------------------------------------

Install from http://pypi.python.org/pypi/django-sql-stacktrace/::

    pip install django-sql-stacktrace

Or install the dev-version from GitHub::

    pip install -e git://github.com/adw0rd/django-sql-stacktrace.git#egg=sqlstacktrace


**Add to settings.py:**

::

    INSTALLED_APPS = (
        'sqlstacktrace',
    )

    SQL_STACKTRACE = True


**Start runserver or any other server:**
::

    ./manage.py runserver 8000

I wish you a successful debugging!
