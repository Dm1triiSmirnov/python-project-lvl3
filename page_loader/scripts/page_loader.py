import logging
import sys

from page_loader.args_parser import args_parse
from page_loader.page_loader import download
from page_loader.logger import configurate_logger


logging.getLogger(__name__)
configurate_logger()


def main():
    args = args_parse()
    try:
        file_path = download(args.output, args.url)
    except Exception as error:
        logging.exception('Exception occurred', exc_info=True)
        print(f'Exception occurred: {error}')
        sys.exit()
    else:
        print(f'Web page successfully downloaded as: {file_path}')
    sys.exit()


if __name__ == '__main__':
    main()
