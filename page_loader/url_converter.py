import re
import os


def convert_output_file_name(url):
    domain = re.sub(r'https:\/\/|http:\/\/', '', url)
    output_file_name = domain.replace('.', '-').replace('/', '-')
    output_file_name += '.html'
    return output_file_name


def convert_file_path(output_directory, output_file_name):
    file_path = os.path.join(output_directory, output_file_name)
    return file_path
