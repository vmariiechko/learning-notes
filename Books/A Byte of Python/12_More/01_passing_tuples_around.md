# Passing tuples around

Ever wished you could return two different values from a function? You can. All you have to do is use a tuple.

~~~
>>> def get_error_details():
...     return (2, 'details')
...
>>> errnum, errstr = get_error_details()
>>> errnum
2
>>> errstr
'details'
~~~

Notice that the usage of `a, b = <some expression>` interprets the result of the expression as a tuple with two values.

This also means the fastest way to swap two variables in Python is:

~~~
>>> a = 5; b = 8
>>> a, b
(5, 8)
>>> a, b = b, a
>>> a, b
(8, 5)
~~~