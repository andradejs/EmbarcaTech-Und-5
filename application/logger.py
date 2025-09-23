import logging
import os

'''
Classe para salvar os loggs de uso 

Para implementar é necessário que a pasta onde o arquivo irá ser salvo
tenha as permissões de criar ou editar arquivos

Na função em que será feito o log, chame o Decorator @loggger_func_exec

ex:
@log.logger_func_exec
def somar(a, b):
    return a + b

somar(1,2)
    
saída:
    Data: 2025-09-23 14:59:52,097 - Result of execution  somar: 3
'''

class Logger():
    def __init__(self, log_filename:str, local_to_save:str):

        self.Logger = logging.getLogger(__name__)

        log_file = os.path.join(local_to_save, log_filename)

        logging.basicConfig(
            level=logging.DEBUG,
            format='Data: %(asctime)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file, encoding='utf-8'),
                logging.StreamHandler()
            ]
        )

    def logger_func_exec(self, func):
        def wrapper(*args, **kwargs):

            result = func(*args, **kwargs)

            self.Logger.debug(f'Result of execution  {func.__name__}: {result}\n')

            return result
            

        return wrapper
    