# sentry-django-plugin

sentry plugin for django.

## sentry

* path: `ridi.sentry_django_plugin`

# Getting started

## Installation

To install and use this package, specify its version and put the following line into your `requirements.txt`:

```
git+ssh://git@github.com/ridi/sentry-django-plugin
```

You can check the release versions and histories in [here](https://github.com/ridi/sentry-django-plugin/releases).

### Authentication

During its installation, it may ask your GitHub credentials. Please read these [articles](https://help.github.com/articles/connecting-to-github-with-ssh/) for further information.

## Usage

```python
from ridi.sentry_django_plugin import configure, get_django_config, get_context_processor

configure(
    public_dsn=SENTRY_PUBLIC_DSN,
    private_dsn=SENTRY_DSN,
    git_sha= GIT_SHA,
)

RAVEN_CONFIG = get_django_config()
sentry_context_processor = get_context_processor()
```

