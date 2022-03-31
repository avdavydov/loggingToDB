from logging import basicConfig, getLogger, INFO, FileHandler, Formatter, StreamHandler

from .crud import Crud
from .db_handler import DBHandler


def get_logger(db_connection_string, encoding='utf-8', pool_size=10, max_overflow=20, log_level=INFO, pool_recycle=3600,
               file_log_name=None, console_out=True):
    crud = Crud(
        connection_string=db_connection_string,
        encoding=encoding,
        pool_size=pool_size,
        max_overflow=max_overflow,
        pool_recycle=pool_recycle)
    crud.initiate()

    basicConfig(format='[%(asctime)s] [%(levelname)s] %(message)s',
                datefmt='%d-%m-%Y %H:%M:%S',
                level=log_level)

    logger = getLogger('logger')
    db_handler = DBHandler(crud=crud)
    db_handler.setLevel(log_level)
    db_format = Formatter('%(message)s')
    db_handler.setFormatter(db_format)
    logger.addHandler(db_handler)

    if console_out:
        console_out = StreamHandler()
        console_out.setLevel(log_level)
        console_format = Formatter('[%(asctime)s] [%(levelname)s] %(message)s', datefmt='%d-%m-%Y %H:%M:%S')
        console_out.setFormatter(console_format)
        logger.addHandler(console_out)

    if file_log_name:
        file_handler = FileHandler(file_log_name)
        file_handler.setLevel(log_level)
        file_format = Formatter('[%(asctime)s] [%(levelname)s] %(message)s')
        file_handler.setFormatter(file_format)
        logger.addHandler(file_handler)

    return logger


if __name__ == "__main__":
    logger = get_logger(db_connection_string='postgresql://test_user:test2022@localhost/edu_test',
                        file_log_name='../log.log')
    logger.debug('debug: hello world!')
    logger.info('info: hello world!')
    logger.warning('warning: hello world!')
    logger.error('error: hello world!')
    logger.critical('critical: hello world!!!!')
