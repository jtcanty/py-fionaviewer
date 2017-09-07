from setuptools import setup

setup(name = 'fionaviewer',
      version = '0.1.0',
      author = 'John Canty',
      author_email = 'jtcanty117@berkeley.edu',
      description = ('A PyQT application for analyzing single-molecule time series signals with discrete steps.'),
      license = 'MIT',
      packages = ['src'],
      install_requires = ['numpy','matplotlib'],
      include_package_data = True,
      zip_safe = False
      url = 'http://github.com/jtcanty/py-fionaviewer'

      classifiers = ['Development Status :: 2 - Pre-Alpha',
                     'Environment :: X11 Applications :: Qt',
                     'Intended Audience :: Science/Research',
                     'License :: OSI Approved :: MIT License',
                     'Operating System :: OS Independent',
                     'Programming Language :: Python :: 2.7',
                     'Topic :: Multimedia :: Graphics :: Viewers',
                     'Topic :: Scientific/Engineering :: Physics',
                     'Topic :: Scientific/Engineering :: Visualization'])



