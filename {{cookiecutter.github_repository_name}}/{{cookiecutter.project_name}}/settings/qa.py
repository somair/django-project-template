from common import *
# Enter your test settings here.

DEBUG = False

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_HSTS_SECONDS=1200
SECURE_HSTS_INCLUDE_SUBDOMAINS=False

{% if cookiecutter.use_celery == 'y' %}
########## CELERY
# In QA, tasks must be executed by a worker
CELERY_ALWAYS_EAGER = False
########## END CELERY
{% endif %}
