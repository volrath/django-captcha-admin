======================
 Django Captcha Admin
======================

Simple way to add a ReCaptcha_ field to your admin login page.

4 simple steps
==============

1. Install ``django-captcha-admin`` from pypi::

     $> pip install django-captcha-admin

2. Add ``captcha_admin`` and ``captcha`` to your ``INSTALLED_APPS``::

     INSTALLED_APPS = (
         ...
         'captcha_admin',
         'captcha',
     )

3. Add your captcha keys to your settings, the way django-recaptcha_
   indicates::

     RECAPTCHA_PUBLIC_KEY = 'your-public-key'
     RECAPTCHA_PRIVATE_KEY = 'your-private-key'

4. Edit your code so instead of `autodiscovering` from
   ``django.contrib.admin.autodiscover`` you use ``captcha_admin`` and
   use ``captcha_admin`` urls::

     import captcha_admin
     captcha_admin.autodiscover()

     urlpatterns = patterns(
         ...
         url(r'^admin/', include(captcha_admin.site.urls)),
         ...
     )

That's it!

.. _ReCaptcha: https://www.google.com/recaptcha/
.. _django-recaptcha: https://github.com/praekelt/django-recaptcha
