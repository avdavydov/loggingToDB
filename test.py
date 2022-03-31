# from logging import INFO, ERROR, WARNING, CRITICAL
from logger.logger_config import get_logger


def main():
    logger = get_logger(db_connection_string='postgresql://test_user:test2022@localhost/edu_test',
                        file_log_name='log.log')
    logger.debug('debug: hello world!')
    logger.info('info: hello world!')
    logger.warning('warning: hello world!')
    logger.error('error: hello world!')
    logger.critical('critical: hello world!!!!')


if __name__ == '__main__':
    main()
