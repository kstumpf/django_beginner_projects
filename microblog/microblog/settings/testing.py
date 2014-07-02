# Taken from http://snipt.net/kennethlove/tag/gswd/

from .base import *

# Creates a different default database for our test to use.
# Due to the name memory --v
# Lives entirely in memory instead of being written to disk, which makes it much faster.

# Don't use sqlite3 for production, but it is fast so good for testing.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# Control what class we use for tests,
# the two settings for where to look for tests,
# and what pattern we want to use for matching test file names.

# This is not needed for versions of Django greater than 1.6.
# TEST_RUNNER = 'discover_runner.DiscoverRunner'
# TEST_DISCOVER_TOP_LEVEL = root('..')
# TEST_DISCOVER_ROOT = root('..')
# TEST_DISCOVER_PATTERN = 'test_*'
