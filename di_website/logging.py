from django.conf import settings
from django.core.cache import cache
from django.utils.log import AdminEmailHandler


class ThrottledAdminEmailHandler(AdminEmailHandler):

    PERIOD_LENGTH_IN_SECONDS = getattr(settings, 'EMAIL_ADMINS_CACHE_TIMEOUT', 10)
    MAX_EMAILS_IN_PERIOD = getattr(settings, 'EMAIL_ADMINS_MAX_EMAILS_PER_TIMEOUT', 1)
    COUNTER_CACHE_KEY = getattr(settings, 'EMAIL_ADMINS_CACHE_COUNTER_KEY', 'email_admins_cache_counter_key')

    def increment_counter(self):
        try:
            cache.incr(self.COUNTER_CACHE_KEY)
        except ValueError:
            cache.set(self.COUNTER_CACHE_KEY, 1, self.PERIOD_LENGTH_IN_SECONDS)
        return cache.get(self.COUNTER_CACHE_KEY)

    def emit(self, record):
        try:
            counter = self.increment_counter()
        except Exception:
            pass
        else:
            if counter > self.MAX_EMAILS_IN_PERIOD:
                return
        super().emit(record)
