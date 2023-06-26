from happy_python import HappyLog
from happy_python.happy_log import HappyLogLevel

hlog = HappyLog.get_instance()
hlog.set_level(HappyLogLevel.TRACE.value)
