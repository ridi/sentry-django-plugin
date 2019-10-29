import json
from . import config


def get_context_processor():
    def sentry_contexts(request):
        if request.user.is_authenticated:
            user_context = json.dumps({
                'email': request.user.email,
                'id': request.user.id,
            })
        else:
            user_context = ""

        return {
            'SENTRY_PUBLIC_DSN': config.SENTRY_CONFIGS.public_dsn,
            'SENTRY_USER_CONTEXT_JSON': user_context,
        }
    return sentry_contexts
