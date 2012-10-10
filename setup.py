from setuptools import setup, find_packages
from sqlstacktrace import __version__

long_description = ""
try:
    readme = open("README.rst")
    long_description = str(readme.read())
    readme.close()
except:
    pass

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
        "Environment :: Web Environment",
        "Programming Language :: Python",
        "Programming Language :: SQL",
        "Framework :: Django",
        "License :: OSI Approved :: BSD License",
        "Topic :: Software Development :: Debuggers",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
