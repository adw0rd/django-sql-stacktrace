__version__ = "0.3.0"


from django.conf import settings
from .replacer import replace_call


SQL_STACKTRACE = settings.SQL_STACKTRACE if hasattr(settings, 'SQL_STACKTRACE') else False
if SQL_STACKTRACE:
    from django.db.backends.base.base import BaseDatabaseWrapper
    from .stacktracecursor import StacktraceCursorWrapper

    @replace_call(BaseDatabaseWrapper.cursor)
    def cursor(func, self):
        result = func(self)
        return StacktraceCursorWrapper(result, self)
