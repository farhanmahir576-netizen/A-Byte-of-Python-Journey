import os
import platform
import logging

# সহজ লগিং সিস্টেম
logging_file = 'test.log'

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename=logging_file,
    filemode='w',
)

logging.debug("Start of the program")
logging.info("Everything is working fine")
logging.warning("This is a warning log")

print("Logging completed. OS:", platform.system())
