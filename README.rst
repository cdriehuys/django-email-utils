##################
django-email-utils
##################

.. image:: https://img.shields.io/travis/com/cdriehuys/django-email-utils/master
    :alt: Travis CI Status
    :target: https://travis-ci.com/cdriehuys/django-email-utils

.. image:: https://img.shields.io/codecov/c/github/cdriehuys/django-email-utils.svg
    :alt: Codecov
    :target: https://codecov.io/gh/cdriehuys/django-email-utils

.. image:: https://img.shields.io/pypi/v/django-email-utils
   :alt: PyPI
   :target: https://pypi.org/project/django-email-utils/

.. image:: https://img.shields.io/github/license/cdriehuys/django-email-utils
   :alt: GitHub License
   :target: https://github.com/cdriehuys/django-email-utils/blob/master/LICENSE


A utility function to ease the process of sending templated emails with Django.


************
Requirements
************

* Python version 3.5 or higher
* Django version 2.2 or higher

************
Installation
************

Install from PyPI::

    pip install django-email-utils


*****
Usage
*****

``email_utils.send_email(template_name, context=None, **kwargs)``
=================================================================

Send templated emails containing HTML, plain text, or both. The function is a
thin wrapper around Django's ``send_mail`` function that loads the email content
from a template.

Example::

    from email_utils import send_email


    send_email(
        context={'foo': 'bar'},
        from_email='no-reply@myproject.com',
        recipient_list=['test@example.com'],
        subject='My Templated Email',
        template_name='myapp/template',
    )

Parameters
----------

``template_name``
  The base name of the templates to use. The function then looks for the
  templates ``{template_name}.html`` and ``{template_name}.txt``.

``context``
  The context used to render the templates. Defaults to an empty dictionary.

``**kwargs``
  Additional keyword arguments to pass to Django's ``send_mail`` function.

Raises
------

``email_utils.NoTemplatesException``
  If neither the HTML nor plain text templates are found.

*******
Testing
*******

Tests are run using pytest. To run the tests, install the requirements and then
execute the tests::

    pip install -r requirements/test.txt
    pytest

*******
License
*******

This project is licensed under the MIT License.


*******
Authors
*******

Chathan Driehuys (chathan@driehuys.com)
