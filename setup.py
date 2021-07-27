from setuptools import setup, find_packages
import os.path

long_description = None
readmeLocation = os.path.join(os.path.dirname(__file__), "README.rst")
with open(readmeLocation) as readmeFile:
  long_description = readmeFile.read()

requires=['blessings']

setup(name='rpgdieroller',
      description='RPG Gaming Die Roller',
      long_description=long_description,
      author='Justin Hugon',
      author_email='opensource AT hugonweb.com',
      version='1.0.alpha',
      packages=find_packages(),
      license='GPLv3',
      classifiers = [
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        ],
      entry_points = {
        'console_scripts':[
            'rpgdierollershell = rpgdieroller.shell:main',
        ]
      },
      provides=['rpgdieroller'],
      setup_requires = requires,
      install_requires = requires,
      )

