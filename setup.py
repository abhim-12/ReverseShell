import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "Win32":
    base = "Win32GUI"

# setup() is a function of cx_freeze
setup(name="remote_access", version="1.0", description="To gain Remote Access",
      executables=[Executable("client.py", base=base)])
