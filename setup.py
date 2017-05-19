from setuptools import setup, find_packages

version = '0.0.1'

setup(name="helga-boy_wonder",
      version=version,
      description=('Holy Interplanetary Yardstick!'),
      classifiers=['Development Status :: 1 - Beta',
                   'Environment :: IRC',
                   'Intended Audience :: Twisted Developers, IRC Bot Developers',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: IRC Bots'],
      keywords='irc bot shaun',
      author='Kevin Chmiel',
      author_email='kevin.m.chmiel@gmail.com',
      url='https://github.com/kevinchmiel/helga-boy_wonder',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      py_modules=['helga-boy_wonder'],
      zip_safe=True,
      entry_points = dict(
          helga_plugins = [
              'boy_wonder= helga_boy_wonder:boy_wonder',
          ],
      ),
)

