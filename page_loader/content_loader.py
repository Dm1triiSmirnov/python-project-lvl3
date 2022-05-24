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


def get_img_urls(url, output_dir_path):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, features="html.parser")
    urls = []
    img_src = soup.find_all('img')
    for img in img_src:
        img_url = img['src']
        if not img_url:
            continue
        img_url = urljoin(url, img_url)
        try:
            pos = img_url.index("?")
            img_url = img_url[:pos]
        except ValueError:
            pass
        if is_valid_url(img_url):
            urls.append(img_url)
        img['src'] = replace_link(img_url, output_dir_path)
    html_doc = soup.prettify()
    return urls, html_doc


def download_image(url, output_dir):
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)
    response = requests.get(url, stream=True)
    file_name = url.split('/')[-1]
    file_size = int(response.headers.get("Content-Length", 0))
    file_path = os.path.join(output_dir, url.split('/')[-1])
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
    img_urls, html_doc = get_img_urls(url, output_dir_path)
    for img in img_urls:
        download_image(img, output_dir_path)
    return html_doc
