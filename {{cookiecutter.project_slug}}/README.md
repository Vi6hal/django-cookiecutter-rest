
## Code Quality
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)


## Dependencies

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)

# {{ cookiecutter.django_project_name }}
A Django project built using [n0tNoah/django-cookiecutter-rest](https://github.com/n0tNoah/django-cookiecutter-rest)

## Dev-Setup
```bash
pip install pre-commit
git init

```


## Installation

```bash
git clone https://github.com/n0tNoah/django-cookiecutter-rest
pip install -r requirements.txt
python3 manage.py migrate

#optional to start contributing
pip install pre-commit
pre-commit install

```

## running locally

```bash
python3 manage.py runserver
```

## License

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

## Actions & Workflows

**Action**: New PR Create for (`master`/`main`) branch:
>Outcome:
	- **Fail**: Reviewer Should Reject PR and ask dev to fix the issues
	- **Pass**: Merge PR

>Steps:
	- Check package dependency/vulnerability issues 
	- Run Code Analysis (run pre-commit hooks on checkout )
	- Run Test Cases

**Action**: Push/PR Merge in (`master`/`main`) branch:
> #Outcome:
	- **Fail**: NA
	- **Pass**: Trigger `Schematic Versioning Tag` release (**automatic**)

> #Steps:
-Check Package dependency/vulnerability issues
-Run Code Analysis (run pre-commit hooks on checkout )
-Run Test Cases

**Action**: New Release Create:
> #Outcome:
	- **Fail**: NA
	- **Pass**: Trigger image build and push to `container registery` (**automatic**)

> #Steps:
-Checkout Release tag and build container image
-Run Test Cases
-Perform CodeCov Report
-Perform Sonar-Cube Scan
-Push Container image to ECR/Docker Hub

**Action**: Manual on Branch:
> #Outcome:
	- **Fail**: NA
	- **Pass**: NA

> #Steps:
	-Checkout Branch
	- Check Package dependency/vulnerability issues
	- Run pre-commit checks
	- Run Test Cases



