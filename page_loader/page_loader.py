import requests
import re

def convert_output_file_name(url):
    result =


def download(output_directory, url):
    response = requests.get(url)
    output_file_name =

    with open(output_file_name, 'wb') as file:
        for chunk in response.iter_content():
            file.write(chunk)


