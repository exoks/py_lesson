#  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣦⣴⣶⣾⣿⣶⣶⣶⣶⣦⣤⣄⠀⠀⠀⠀⠀⠀⠀
#  ⠀⠀⠀⠀⠀⠀⠀⢠⡶⠻⠛⠟⠋⠉⠀⠈⠤⠴⠶⠶⢾⣿⣿⣿⣷⣦⠄⠀⠀⠀             𓐓  __init__.py 𓐔           
#  ⠀⠀⠀⠀⠀⢀⠔⠋⠀⠀⠤⠒⠒⢲⠀⠀⠀⢀⣠⣤⣤⣬⣽⣿⣿⣿⣷⣄⠀⠀
#  ⠀⠀⠀⣀⣎⢤⣶⣾⠅⠀⠀⢀⡤⠏⠀⠀⠀⠠⣄⣈⡙⠻⢿⣿⣿⣿⣿⣿⣦⠀       Dev: oezzaou </var/spool/mail/oezzaou>
#  ⢀⠔⠉⠀⠊⠿⠿⣿⠂⠠⠢⣤⠤⣤⣼⣿⣶⣶⣤⣝⣻⣷⣦⣍⡻⣿⣿⣿⣿⡀
#  ⢾⣾⣆⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
#  ⠀⠈⢋⢹⠋⠉⠙⢦⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇       Created: 2025/07/24 16:59:34 by oezzaou
#  ⠀⠀⠀⠑⠀⠀⠀⠈⡇⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇       Updated: 2025/07/24 17:09:43 by oezzaou
#  ⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢀⣾⣿⣿⠿⠟⠛⠋⠛⢿⣿⣿⠻⣿⣿⣿⣿⡿⠀
#  ⠀⠀⠀⠀⠀⠀⠀⢀⠇⠀⢠⣿⣟⣭⣤⣶⣦⣄⡀⠀⠀⠈⠻⠀⠘⣿⣿⣿⠇⠀
#  ⠀⠀⠀⠀⠀⠱⠤⠊⠀⢀⣿⡿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠘⣿⠏⠀⠀                             𓆩♕𓆪
#  ⠀⠀⠀⠀⠀⡄⠀⠀⠀⠘⢧⡀⠀⠀⠸⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠐⠋⠀⠀⠀                     𓄂 oussama ezzaou𓆃
#  ⠀⠀⠀⠀⠀⠘⠄⣀⡀⠸⠓⠀⠀⠀⠠⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# INFO:-------------------------------------------------------------------------
# - When Adding __init__.py, you tell the python that this directory is package
#   python start seeing directory as package, so everything inside becomes
#   'importable'

# ===[ QUESTION:]==============================================================
# - Why can we just import the module inside the directory by it's path,
#   like in c, c++
# You're absolutely right to feel this is a bit strange — Python's import system works very differently from C/C++, and it's rooted in Python's philosophy and design decisions.
# Let’s walk through why this is the case, and why Python doesn't allow path-based importing like C/C++'s #include "file.h":
# 🚀 Why Python Doesn't Import by File Path Like C/C++
# 🔗 1. Python is interpreted, not compiled
#
#     In C/C++, #include literally copies the contents of a file into another during preprocessing.
#
#     In Python, import is not textual inclusion — it's a runtime operation.
#
#     Python loads and executes modules dynamically using its module resolution system.
#
# 🗂️ 2. Python uses package/module hierarchy, not file paths
#
# Python modules are resolved using:
#
#     sys.path (a list of search directories)
#
#     Package structure (__init__.py)
#
#     Module names (not paths)
#
# Example:
#
# from utils import math_tools
#
# Python looks:
#
#     In current dir
#
#     In PYTHONPATH
#
#     In site-packages
#
#     Inside packages (if __init__.py is present)
#
# 📁 It’s not "look in /path/to/utils/math_tools.py" — it’s "look for a 
#    package named utils, and a module named math_tools inside it."
# ❌ Why Not Allow from /some/path/file.py import foo?
#
# It seems logical, but has issues:
#
#     Breaks portability
#
#     Breaks Python’s ability to cache and reuse modules
#
#     Would tightly couple scripts to file structure
#
#     Introduces security risks (importing arbitrary paths)
#
#     Harder to lint, debug, test, and introspect
#
# ✅ What you can do if you really want path-based importing
#
# Python has workarounds, but they’re advanced:
# 🧪 Option 1: Manually extend sys.path
#
# import sys
# sys.path.append("/path/to/my/modules")
# from my_module import something
#
#     ✅ Works but not clean — breaks in production or multi-platform.
#
# 🧪 Option 2: Use importlib.util (dynamic import by path)
#
# import importlib.util
#
# spec = importlib.util.spec_from_file_location("my_module", "/path/to/my_module.py")
# module = importlib.util.module_from_spec(spec)
# spec.loader.exec_module(module)
#
# module.some_function()
#
#     ✅ Full path import! But clunky and not beginner-friendly.
#
# 🧠 Philosophy: Python favors namespaces and packages over file paths
#
# Python's import system is designed to:
#
#     Be safe
#
#     Promote modularity
#
#     Encourage readable and maintainable code
#
#     Avoid C-style spaghetti code from #include abuse
#
# 🔥 TL;DR
# Feature	C/C++	Python
# Include by file path	#include "file.h"	❌ Not supported directly
# Import by module name	❌	✅ Standard way (import x)
# Can override search paths	-I compiler flag	sys.path or PYTHONPATH
# Copy/paste code into source	#include	❌ Not how import works
# Portable across systems	❌ Often path-specific	✅ Yes
