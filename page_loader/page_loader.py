import requests

from page_loader.url_converter import convert_output_file_name, convert_file_path  # noqa E501


def download(output_directory, url):
    response = requests.get(url)
    output_file_name = convert_output_file_name(url)
    output_path = convert_file_path(output_directory, output_file_name)
    with open(output_path, 'wb') as file:
        for chunk in response.iter_content():
            file.write(chunk)
    return output_path
