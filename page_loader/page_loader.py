import requests

from page_loader.url_converter import convert_output_file_name, convert_file_path, convert_output_dir_name  # noqa E501
from page_loader.img_loader import download_all_images


def download(output_directory, url):
    response = requests.get(url)
    output_file_name = convert_output_file_name(url)
    output_path = convert_file_path(output_directory, output_file_name)
    with open(output_path, 'wb') as file:
        for chunk in response.iter_content():
            file.write(chunk)
    output_files_dir_name = convert_output_dir_name(url)
    output_files_path = convert_file_path(output_directory, output_files_dir_name)
    download_all_images(url, output_files_path)
    return output_path




