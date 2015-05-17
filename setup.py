from distutils.core import setup

setup(
    name='password-generator',
    version='0.1',
    url='https://github.com/wirbi7/password-generator',
    license='GNU GPL 2.0',
    author='Igor Nekrasov',
    author_email='nekrasov.i.m@gmail.com',
    description='Little Linux Password Generator written on Python 3 with Gtk',
    packages=['passwordgenerator'],
    package_dir={'passwordgenerator': 'passwordgenerator'},
    package_data={'passwordgenerator': ['pasgen.glade']},
    scripts=['pasgen'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: POSIX',
        'Programming Language :: Python',
    ]
)
