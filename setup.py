# from distutils.core import setup
from setuptools import setup

setup(
	name='fragment',
	url='https://github.com/zweifisch/fragment',
	version='0.0.1',
	description='just another static site generator',
	author='Feng Zhou',
	author_email='zf.pascal@gmail.com',
	packages=['fragment'],
	install_requires=['markdown2', 'docopt'],
	entry_points={
		'console_scripts': ['fragment=fragment:main'],
	},
)
