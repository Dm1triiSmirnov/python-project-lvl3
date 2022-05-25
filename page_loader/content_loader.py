import os
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


def is_valid_url(url):
    return bool(urlparse(url).netloc) and bool(urlparse(url).scheme)


def replace_link(src_link, output_dir):
    file_name = src_link.split('/')[-1]
    new_link = output_dir + '/' + file_name
    return new_link


def get_content_links(url, output_dir_path):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, features="html.parser")
    links = []
    src = soup.find_all('img')
    for item in src:
        link = item['src']
        if not link:
            continue
        link = urljoin(url, link)
        try:
            pos = link.index("?")
            link = link[:pos]
        except ValueError:
            pass
        if is_valid_url(link):
            links.append(link)
        item['src'] = replace_link(link, output_dir_path)
    html_doc = soup.prettify()
    return links, html_doc


def download_element(link, output_dir):
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)
    response = requests.get(link, stream=True)
    file_name = link.split('/')[-1]
    file_size = int(response.headers.get("Content-Length", 0))
    file_path = os.path.join(output_dir, link.split('/')[-1])
    progress = tqdm(response.iter_content(1024),
                    f"Downloading {file_name}",
                    total=file_size, unit="B",
                    unit_scale=True,
                    unit_divisor=1024)
    with open(file_path, 'wb') as file:
        for data in progress.iterable:
            file.write(data)
            progress.update(len(data))


def download_all_content(url, output_dir_path):
    links, html_doc = get_content_links(url, output_dir_path)
    for link in links:
        download_element(link, output_dir_path)
    return html_doc
