import os
import sys
import time


time.sleep(2)
os.execv(sys.executable, ['test'] + sys.argv)

