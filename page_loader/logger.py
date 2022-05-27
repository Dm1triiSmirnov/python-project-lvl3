import logging


def configurate_logger():
    logging.basicConfig(level=logging.DEBUG,
                        filename='logs.txt',
                        filemode='w',
                        format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',  # noqa E501
                        datefmt='%d-%b-%y %H:%M:%S')
