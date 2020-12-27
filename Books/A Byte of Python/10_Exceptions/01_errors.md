# Errors

Consider a simple print function call. What if we misspelt print as Print? Note the capitalization. In this case, Python raises a syntax error.

~~~
>>> Print("Hello World")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Print' is not defined
>>> print("Hello World")
Hello World
~~~

Observe that a NameError is raised and also the location where the error was detected is printed. This is what an error handler for this error does.