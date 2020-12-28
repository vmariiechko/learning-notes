# `sys` module

The sys module contains system-specific functionality. 

Suppose we want to check the version of the Python software being used, the sys module gives us that information.

~~~
>>> import sys
>>> sys.version_info
sys.version_info(major=3, minor=6, micro=0, releaselevel='final', serial=0)
>>> sys.version_info.major == 3
True
~~~