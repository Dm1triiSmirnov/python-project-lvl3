import re
import os


def convert_output_file_name(url):
    domain = re.sub(r'https:\/\/|http:\/\/', '', url)
    raw_file_name = domain.replace('.', '-').replace('/', '-')
    output_file_name = raw_file_name.strip('-') + '.html'
    return output_file_name


def convert_file_path(output_directory, output_file_name):
    file_path = os.path.join(output_directory, output_file_name)
    return file_path


def convert_output_dir_name(url):
    output_dir_name = convert_output_file_name(url).replace('.html', '_files')
    return output_dir_name
