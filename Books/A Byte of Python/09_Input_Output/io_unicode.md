# Unicode

So far, when we have been writing and using strings, or reading and writing to a file, we have used simple English characters only. Both English and non-English characters can be represented in Unicode and Python 3 by default stores string variables in Unicode.

> NOTE: If you are using Python 2, and we want to be able to read and write other non-English languages, we need to use the `unicode` type, and it all starts with the character `u`, e.g. `u"hello world"`

~~~
>>> "hello world"
'hello world'
>>> type("hello world")
<class 'str'>
>>> u"hello world"
'hello world'
>>> type(u"hello world")
<class 'str'>
~~~

When data is sent over the Internet, we need to send it in bytes... something your computer easily understands. The rules for translating Unicode (which is what Python uses when it stores a string) to bytes is called encoding. A popular encoding to use is UTF-8. We can read and write in UTF-8 by using a simple keyword argument in our open function.

~~~
# encoding=utf-8
import io

f = io.open("abc.txt", "wt", encoding="utf-8")
f.write(u"Imagine non-English language here")
f.close()

text = io.open("abc.txt", encoding="utf-8").read()
print(text)
~~~

We use io.open and then use the encoding argument in the first open statement to encode the message, and then again in the second open statement when decoding the message. Note that we should only use encoding in the open statement when in text mode.

Whenever we write a program that uses Unicode literals (by putting a u before the string) like we have used above, we have to make sure that Python itself is told that our program uses UTF-8, and we have to put # encoding=utf-8 comment at the top of our program.

You should learn more about this topic by reading:

* ["The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets"](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)
* [Python Unicode Howto](https://docs.python.org/3/howto/unicode.html)
* [Pragmatic Unicode talk by Nat Batchelder](https://nedbatchelder.com/text/unipain.html)