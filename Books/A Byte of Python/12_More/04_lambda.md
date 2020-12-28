# Lambda Forms

A lambda statement is used to create new function objects. Essentially, the lambda takes a parameter followed by a single expression. Lambda becomes the body of the function. The value of this expression is returned by the new function.

~~~
points = [{'x': 2, 'y': 3},
          {'x': 4, 'y': 1}]
points.sort(key=lambda i: i['y'])
print(points)
~~~

Notice that the sort method of a list can take a key parameter which determines how the list is sorted (usually we know only about ascending or descending order). In our case, we want to do a custom sort, and for that we need to write a function. Instead of writing a separate def block for a function that will get used in only this one place, we use a lambda expression to create a new function.