# Single Statement Blocks

If your block of statements contains only one single statement, then you can specify it on the same line of, say, a conditional statement or looping statement. The following example should make this clear:

~~~
>>> flag = True
>>> if flag: print('Yes')
...
Yes
~~~

Notice that the single statement is used in-place and not as a separate block. Although, you can use this for making your program smaller, I strongly recommend avoiding this short-cut method, except for error checking, mainly because it will be much easier to add an extra statement if you are using proper indentation.