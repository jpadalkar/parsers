"""
    SEC parser python package configuration.
"""

from setuptools import setup

setup(
      name='parserSEC',
      version='0.1.0',
      packages=['parserSEC'],
      include_package_data=True,
      install_requires=[
                        'click==6.7',
                        'sh==1.12.14',
                        'flask==0.12.3',
                        'arrow==0.10.0',
                        'html5validator==0.2.8',
                        'pycodestyle==2.3.1',
                        'pydocstyle==2.0.0',
                        'pylint==2.1.1',
                        'sh==1.12.14',
                        'selenium==3.6.0',
                        'requests==2.18.4'
                        ],
      entry_points={
      'console_scripts': [
                          'parserSEC = parserSEC.__main__:main'
                          ]
      },
      )
