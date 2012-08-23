django-sql-stacktrace
=====================

Reusable application, which puts a python stack trace in the SQL query as a comment (useful for debugging).

After installed you can see in ``processlist`` a SQL-query and comment with python stack trace:

    watch -n1 mysqladmin processlist --verbose

Or you can see in a log files, such as ``log_slow_queries`` or ``log-bin`` (aka 'binlog').


How to install this wonderful package?
=====================

Add to settings.py:
---------------------

    INSTALLED_APPS = (
        'sqlstacktrace',
    )

    SQL_STACKTRACE = True


Start runserver or any other server:
---------------------

    ./manage.py runserver 8000


I wish you a successful debugging!