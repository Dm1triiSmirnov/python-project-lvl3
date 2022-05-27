import os
import requests
import logging
from tqdm import tqdm
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

from .logger import configurate_logger


logging.getLogger(__name__)
configurate_logger()


RESOURCES = {'img': 'src', 'script': 'src', 'link': 'href'}


def is_valid_url(url):
    return bool(urlparse(url).netloc) and bool(urlparse(url).scheme)


def replace_link(src_link, output_dir):
    file_name = src_link.split('/')[-1]
    new_link = output_dir + '/' + file_name
    return new_link


def get_content_links(url, output_dir_path):
    try:
        response = requests.get(url)
    except requests.RequestException:
        logging.error('Connection error', exc_info=True)
    soup = BeautifulSoup(response.content, features="html.parser")
    links = []
    tags = soup.find_all(RESOURCES.keys())
    for item in tags:
        link = item.get(RESOURCES[item.name])
        if not link:
            continue
        link = urljoin(url, link)
        try:
            pos = link.index("?")
            link = link[:pos]
        except ValueError:
            logging.error('Exception occurred', exc_info=True)
        if is_valid_url(link):
            links.append(link)
        item[RESOURCES[item.name]] = replace_link(link, output_dir_path)
    html_doc = soup.prettify()
    return links, html_doc


def download_element(link, output_dir):
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)
    response = requests.get(link, stream=True)
    file_name = link.split('/')[-1]
    file_size = int(response.headers.get("Content-Length", 0))
    file_path = os.path.join(output_dir, link.split('/')[-1])
    progress = tqdm(response.iter_content(),
                    f"Downloading {file_name}",
                    total=file_size, unit="B",
                    unit_scale=True,)
    if not os.path.isdir(file_path):
        with open(file_path, 'wb') as file:
            for data in progress.iterable:
                file.write(data)
                progress.update(len(data))
            logging.info(f'File {file_name} successfully downloaded')


def download_all_content(url, output_dir_path):
    links, html_doc = get_content_links(url, output_dir_path)
    for link in links:
        download_element(link, output_dir_path)
    return html_doc
