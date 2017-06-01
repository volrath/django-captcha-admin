from distutils.core import setup
from captcha_admin import get_version, __maintainer__, __email__


long_description = open('README.rst').read()


setup(
    name = 'django-captcha-admin',
    version = get_version().replace(' ', '-'),
    url = 'http://github.com/volrath/django-captcha-admin',
    author = __maintainer__,
    author_email = __email__,
    license = 'MIT',
    packages = ['captcha_admin'],
    package_data= {
        'captcha_admin': ['templates/admin/*']
    },
    data_files=[('', ['LICENSE.txt', 'README.rst'])],
    install_requires=['django-recaptcha == 1.3.0'],
    description = 'Provides a recaptcha field in django\'s default admin login page.',
    long_description=long_description,
    classifiers = ['Development Status :: 5 - Production/Stable',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Topic :: Internet :: WWW/HTTP :: Dynamic Content']
)
