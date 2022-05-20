import os
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


def is_valid_url(url):
    return bool(urlparse(url).netloc) and bool(urlparse(url).scheme)


def get_images_urls(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, features="html.parser")
    urls = []
    img_src = soup.find_all('img')
    for img in tqdm(img_src, 'Downloading file'):
        img_url = img.attrs.get('src')
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
    return urls


def download_image(url, output_dir):
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)
    response = requests.get(url, stream=True)
    file_size = int(response.headers.get("Content-Length", 0))
    file_name = os.path.join(output_dir, url.split('/')[-1])
    progress = tqdm(response.iter_content(1024),
                    f"Downloading {file_name}",
                    total=file_size, unit="B",
                    unit_scale=True,
                    unit_divisor=1024)
    with open(file_name, 'wb') as file:
        for data in progress.iterable:
            file.write(data)
            progress.update(len(data))


def download_all_images(url, output_dir_path):
    imgs_urls = get_images_urls(url)
    for img in imgs_urls:
        download_image(img, output_dir_path)
