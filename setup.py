from setuptools import setup, find_packages

setup(name = 'django_ckeditorfiles',
      description = 'CKEditor bundled as a django staticfiles app.',
      version = '1.3',
      url = 'https://github.com/espenak/django_ckeditorfiles',
      author = 'Espen Angell Kristiansen',
      license = 'LGPL',
      packages=find_packages(exclude=['ez_setup']),
      zip_safe = False,
      include_package_data=True,
      install_requires = ['setuptools', 'Django'],
      classifiers=[
                   'Development Status :: 5 - Production/Stable',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python'
                  ]
)
