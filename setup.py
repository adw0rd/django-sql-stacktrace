from setuptools import setup, find_packages
from sqlstacktrace import __version__

long_description = """
For more details see:
---------------------

* http://adw0rd.com/2012/django-sql-stacktrace/en/
* http://github.com/adw0rd/django-sql-stacktrace


Settings:
---------------------

::

    INSTALLED_APPS = (
        'sqlstacktrace',
    )

    SQL_STACKTRACE = True

"""

setup(
    name='django-sql-stacktrace',
    version=__version__,
    description="Pluggable application, which puts a python stack trace in the SQL query as a comment (useful for debugging)",
    long_description=long_description,
    keywords='django, debug, debugging, logger, sql, stack, trace, frame',
    author='Mikhail Andreev',
    author_email='x11org@gmail.com',
    url='http://github.com/adw0rd/django-sql-stacktrace',
    license='BSD',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: SQL",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Topic :: Software Development :: Debuggers",
    ],
)
