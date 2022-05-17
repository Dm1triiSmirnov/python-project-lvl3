import argparse


def args_parse():
    parser = argparse.ArgumentParser(description=None)
    parser.add_argument('directory')
    parser.add_argument('web_page')
    parser.add_argument('-o', '--output',
                        default='"/app"',
                        help='output dir (default: "/app"')
    parser.add_argument('-V', '--version',
                        help='output the version number')
    parser.add_argument('-h', '--help',
                        help='display help command')
    args = parser.parse_args()
    return args


def main():
    args = args_parse()
    page = download(args.directory, args.web_page, args.output)
    print(page)


if __name__ == '__main__':
    main()
