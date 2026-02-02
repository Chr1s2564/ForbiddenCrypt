import logging
import sys

def logger_setup():
    #logger Config
    logger = logging.getLogger("Game")
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

    #logger destination
    console_out = logging.StreamHandler(sys.stdout)
    console_out.setLevel(logging.DEBUG) # maybe modify to .INFO
    console_out.setFormatter(formatter)

    #log file writing
    file_out = logging.FileHandler("logs.txt")
    file_out.setLevel(logging.DEBUG)
    file_out.setFormatter(formatter)

    logger.addHandler(console_out)
    logger.addHandler(file_out)

    return logger