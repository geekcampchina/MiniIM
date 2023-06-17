from pathlib import PurePath

from happy_python import HappyLog

LOG_CONFIG_FILENAME = str(PurePath(__file__).parent / 'log.ini')

hlog = HappyLog.get_instance(LOG_CONFIG_FILENAME)
