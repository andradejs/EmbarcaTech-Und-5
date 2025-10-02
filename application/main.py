from logger import Logger
from aht10 import aht10_init, aht10_read
from time import sleep as sleep_sc
from random import randint

logger = Logger('datalogger.txt','/mnt/sdcard/logs')

@logger.logger_func_exec
def main_read_aht10():
    aht10_init()
    while True:

        temperature, humidity = aht10_read()

        results = {
            'Temperatiure': temperature,
            'Humidity': humidity
        }

        logger.logger_write_result_dict(results)

        sleep_sc(10)

main_read_aht10()