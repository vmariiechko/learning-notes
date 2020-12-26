# There are two types of fields - class variables and object variables

##### ##### ##### #####
### Class variables ###
##### ##### ##### #####
# Class variables are shared - they can be accessed by all instances of that class.
# There is only one copy of the class variable and when any one object makes a change 
# to a class variable, that change will be seen by all the other instances.

##### ##### ##### ######
### Object variables ###
##### ##### ##### ######
# Object variables are owned by each individual object/instance of the class. 
# In this case, each object has its own copy of the field i.e. they are not shared 
# and are not related in any way to the field by the same name in a different instance.

class Robot:
    """Represents a robot, with a name."""

    # A class variable, counting the number of robots
    population = 0

    def __init__(self, name):
        """Initializes the data."""
        self.name = name
        print("(Initializing {})".format(self.name))

        # When this person is created, the robot
        # adds to the population
		# refer to the population class variable as Robot.population and not as self.population
        Robot.population += 1	

    def die(self):
        """I am dying."""
        print("{} is being destroyed!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(
                Robot.population))

    def say_hi(self):
        """Greeting by the robot.

        Yeah, they can do that."""
        print("Greetings, my masters call me {}.".format(self.name))

   	# The method that belongs to the class and not to the object.
   	# We have marked the method as a class method using a decorator.
    @classmethod
    def how_many(cls):
        """Prints the current population."""
        print("We have {:d} robots.".format(cls.population))
   	# Decorators can be imagined to be a shortcut to calling a wrapper function
   	# applying the @classmethod decorator is the same as calling:
   	# how_many = classmethod(how_many)


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()

# Instead of Robot.population, we could have also used self.__class__.population 
# because every object refers to its class via the self.__class__ attribute.

# Observe that the __init__ method is used to initialize the Robot instance with a name.

# All class members are public. One exception: If you use data members with names 
# using the double underscore prefix such as __privatevar, Python uses name-mangling 
# to effectively make it a private variable.