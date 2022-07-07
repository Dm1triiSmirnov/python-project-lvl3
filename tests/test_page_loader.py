import os
import pytest
import requests
import tempfile
import requests_mock

from page_loader.page_loader import download
from page_loader.url_converter import convert_output_file_name


URL = 'https://ru.hexlet.io/courses'
OUTPUT_FILE_NAME = convert_output_file_name(URL)


def read_file(file_name):
    file_path = os.path.join(os.path.dirname(__file__), 'fixtures', file_name)
    with open(file_path) as file:
        result = file.read()
        return result


# @pytest.fixture
# def test_page(requests_mock):
#     requests_mock.get(URL, text=read_file(OUTPUT_FILE_NAME))
#
#
# def test_download(test_page):
#     with tempfile.TemporaryDirectory() as temp_dir:
#         output_path = download(temp_dir, URL)
#         expected = os.path.join(temp_dir, OUTPUT_FILE_NAME)
#         assert expected == output_path
#
#
# def test_page_content(test_page):
#     with tempfile.TemporaryDirectory() as temp_dir:
#         output_path = download(temp_dir, URL)
#         with open(output_path) as test_page:
#             assert test_page.read() == requests.get(URL).text


