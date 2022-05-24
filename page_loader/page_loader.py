from page_loader.url_converter import (convert_output_file_name,
                                       convert_file_path,
                                       convert_output_dir_name)
from page_loader.content_loader import download_all_content


def download(output_directory, url):
    output_file_name = convert_output_file_name(url)
    output_path = convert_file_path(output_directory, output_file_name)
    output_files_dir = convert_output_dir_name(url)
    output_files_path = convert_file_path(output_directory, output_files_dir)
    html_doc = download_all_content(url, output_files_path)
    with open(output_path, 'w') as file:
        file.write(html_doc)
    return output_path
