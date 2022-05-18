import argparse
import os


def args_parse():
    parser = argparse.ArgumentParser(description='Cli-utilit downloads web-pages from the internet and saves them on your computer')  # noqa E501
    parser.add_argument('url')
    parser.add_argument('-o', '--output',
                        default=os.getcwd(),
                        help=f'output dir (default: "{os.getcwd()}"')
    args = parser.parse_args()
    return args
