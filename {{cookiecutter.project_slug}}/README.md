[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Code Quality

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[GitHub Actions](https://img.shields.io/badge/githubactions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)

## Dependencies

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)

# {{ cookiecutter.django_project_name }}

## Installation

```bash
pip install -r requirements.txt
python3 manage.py migrate
```

## Usage

```bash
python3 manage.py runserver
```

## License

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}.svg?style=for-the-badge
[contributors-url]: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}.svg?style=for-the-badge
[forks-url]: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}/network/members
[stars-shield]: https://img.shields.io/github/stars/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}.svg?style=for-the-badge
[stars-url]: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}/stargazers
[issues-shield]: https://img.shields.io/github/issues/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}.svg?style=for-the-badge
[issues-url]: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}/issues
[license-shield]: https://img.shields.io/github/license/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}?style=for-the-badge
[license-url]: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}/blob/main/LICENSE.txt
