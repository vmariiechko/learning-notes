# Special Methods

There are certain methods such as the `__init__` and `__del__` methods which have special significance in classes.

Some useful special methods are listed in the following table. If you want to know about all the special methods, [see the manual](https://docs.python.org/3/reference/datamodel.html#special-method-names).

* `__init__(self, ...)`

    * This method is called just before the newly created object is returned for usage.

* `__del__(self)`

    * Called just before the object is destroyed (which has unpredictable timing, so avoid using this)

* `__str__(self)`

    * Called when we use the print function or when str() is used.

* `__lt__(self, other)`

    * Called when the less than operator (<) is used. Similarly, there are special methods for all the operators (+, >, etc.)

* `__getitem__(self, key)`

    * Called when x[key] indexing operation is used.

* `__len__(self)`

    * Called when the built-in len() function is used for the sequence object.