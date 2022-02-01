
# Django Rest Cookiecutter template for Rest Framework/DRF

a django cookiecutter rest framework /drf cookiecutter template for bootstrapping `headless` **Django** with minimal efforts and ensuring the best practices followed in at the very beginning,

[![Sanity Check](https://github.com/n0tNoah/django-cookiecutter-rest/actions/workflows/sanitycheck.yml/badge.svg)](https://github.com/n0tNoah/django-cookiecutter-rest/actions/workflows/sanitycheck.yml)

## Features
This template does not force you to integrate `boto3`,`postgres`,`docker` or any other dependancy / practices, but rather focuses on the important and crucial things,at the same time giving you options to branch out in directions with the boilerplate,it let's you deicde your pizza toppings as you develop further, while [agconti/cookiecutter-django-rest](https://github.com/agconti/cookiecutter-django-rest) changes things drastically in terms of settings,packages and project structure that i feel a need to start over.

- For Django 3.2.10
- Works with Python 3.9/3.8/3.7
- [12-Factor](http://12factor.net/) compliance
- Optimized development and production settings
- Comes with custom user model ready to go
- Docker support using [Dockerfile](https://github.com/docker) for development and production
- [Procfile](https://devcenter.heroku.com/articles/procfile) for deploying to Heroku
- PostgreSQL support
- Default integration with [pre-commit](https://github.com/pre-commit/pre-commit) for identifying simple issues before submission to code review

## Usage

Let's pretend you want to create a Django project called "petstore". Rather than using `startproject`
and then editing the results to include your name, email, and various configuration issues that always get forgotten until the worst possible moment, get [cookiecutter](https://github.com/cookiecutter/cookiecutter) to do all the work.

First, get Cookiecutter:

    $ pip install "cookiecutter>=1.7.0"

Now run it against this repo:

    $ cookiecutter https://github.com/n0tNoah/django-cookiecutter-rest/

You'll be prompted for some values. Provide them, then a Django project will be created for you.

## Contributing 
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
Suggestions,opinions & issues are welcome.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Authors

* **Vishal P** - *Initiator* - [n0tNoah](https://github.com/n0tNoah)

##  Acknowledgments
- 🎩 Hat tip to anyone whose code was used
- Inspired by [agconti/cookiecutter-django-rest](https://github.com/agconti/cookiecutter-django-rest)

###### Powered by [Cookiecutter](https://github.com/cookiecutter/cookiecutter) & [Django](https://www.djangoproject.com/)
