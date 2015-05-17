from setuptools import setup

setup(
    name='password-generator-gtk',
    version='0.1',
    url='https://github.com/wirbi7/password-generator',
    license='GNU GPL 2.0',
    author='Igor Nekrasov',
    author_email='nekrasov.i.m@gmail.com',
    description='Little Linux Password Generator written on Python 3 with Gtk',
    packages=['passwordgeneratorgtk'],
    package_dir={'passwordgeneratorgtk': 'passwordgeneratorgtk'},
    package_data={'passwordgeneratorgtk': ['pasgen.glade']},
    scripts=['pasgen'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: POSIX',
        'Programming Language :: Python',
    ]
)
