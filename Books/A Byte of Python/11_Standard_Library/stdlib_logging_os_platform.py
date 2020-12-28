import os	# interacting with the operating system
import platform	# information about the platform (operating system)
import logging 	# log information

# Check which operating system we are using
if platform.platform().startswith('Windows'):

	# If it is Windows, we figure out the home drive, the home folder 
	# and the filename where we want to store the information.
	# Putting these three parts together, we get the full location of the file.
	# We use the os.path.join() function to put these three parts of the location together
    logging_file = os.path.join(os.getenv('HOMEDRIVE'),
                                os.getenv('HOMEPATH'),
                                'test.log')
else:
	# For other platforms, we need to know just the home folder of the user
	# and we get the full location of the file

    logging_file = os.path.join(os.getenv('HOME'),
                                'test.log')

print("Logging to", logging_file)

# Configure the logging module to write all the messages 
# in a particular format to the file we have specified.
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename=logging_file,
    filemode='w',
)

logging.debug("Start of the program")
logging.info("Doing something")
logging.warning("Dying now")