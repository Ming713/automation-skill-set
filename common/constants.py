import os

BROWSER_NAME = os.getenv('BROWSER_NAME', 'DESKTOP CHROME')
MOBILEOS = os.getenv('MOBILEOS', None)
MOBILE_OS_VERSION = os.getenv('MOBILE_OS_VERSION', None)

TARGET_ENV = os.getenv('TARGET_ENV', 'LOCALS')
BROWSER_VERSION = os.getenv('BROWSER_VERSION', 'latest')
