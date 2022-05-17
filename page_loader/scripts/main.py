from page_loader.args_parser import args_parse
from page_loader.page_loader import download


def main():
    args = args_parse()
    file_path = download(args.output_directory, args.url)
    print(file_path)


if __name__ == '__main__':
    main()