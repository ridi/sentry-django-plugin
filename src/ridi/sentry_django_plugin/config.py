from collections import namedtuple

ConnectArgsType = namedtuple('ConnectArgsType', [
    'public_dsn', 'private_dsn', 'git_sha',
])

SENTRY_CONFIGS = None


def configure(public_dsn=None, private_dsn=None, git_sha=None):
    global SENTRY_CONFIGS

    SENTRY_CONFIGS = ConnectArgsType(
        public_dsn=public_dsn,
        private_dsn=private_dsn,
        git_sha=git_sha,
    )


def get_django_config():
    return {
        'dsn': SENTRY_CONFIGS.private_dsn,
        'release': SENTRY_CONFIGS.git_sha,
    }
