# Django Basic

## Requirement

- Python3 (>= v3.6 is recommended)
   Follow this tutorial : [Installing Python3](http://docs.python-guide.org/en/latest/starting/installation/#python-3-installation-guides) or [Setup Python3 on Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-ubuntu-16-04#step-2-%E2%80%94-setting-up-a-virtual-environment)
- PostgreSQL (>= v9.6 is recommended)
  Useful links:  [PostgreSQL Guide: Install](http://postgresguide.com/setup/install.html), [DigitalOceanL Install Postgress on Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04)

In other side you can setup your requirement by your own. You can use Docker, etc. Feel free to explore your self.

## Installing & Running

After prerequisites has been setup. You have to make the program run. 
  - Install `python` ( >= v3.6 is recommended), `pip`, `virtualenv`
  - Clone project
  - Create `virtualenv` to `env` directory by using `virtualenv env`
  - Acitvated python virtual env with this command `$source env/bin/activate`
  - Create `.env` file by rename or copy `env.dist` to `.env`
  - Make sure all variables value in your `.env` is yours
  - Install dependency library for project sting ray with run this command `pip install -r requirements.txt` 
  - Run this command `python manage.py migrate`
  - Run this command to start server `python manage.py runserver 0.0.0.0:9000 --settings=config.settings.local`
