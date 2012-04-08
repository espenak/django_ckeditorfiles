from setuptools import setup, find_packages

setup(name = 'django_ckeditorfiles',
      description = 'CKEditor bundled as a django staticfiles app.',
      version = '1.0',
      url = 'http://espenak.net',
      author = 'Espen Angell Kristiansen',
      license = 'LGPL',
      packages=find_packages(exclude=['ez_setup']),
      zip_safe = False,
      install_requires = ['setuptools', 'Django']
)
