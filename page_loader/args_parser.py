import argparse


def args_parse():
    parser = argparse.ArgumentParser(description='Cli-utilit downloads web-pages from the internet and saves them on your computer')  # noqa E501
    parser.add_argument('output_directory')
    parser.add_argument('url')
    parser.add_argument('-o', '--output',
                        default='"/"',
                        help='output dir (default: "/"')
    parser.add_argument('-V', '--version',
                        help='output the version number')
    args = parser.parse_args()
    return args
