"""File for crawling various parts of sec.gov"""

import os
import requests
import zipfile
import io
from bs4 import BeautifulSoup


def get_file_links(archive_url, filetype='zip'):
    r = requests.get(archive_url)
    soup = BeautifulSoup(r.content, 'html.parser')
    links = soup.find_all('a')
    file_links = []
    for link in links:
        if link.get('href') is None:
            continue
        if link.get('href').endswith(filetype):
            file_links.append("https://sec.gov/" + link.get('href'))
    return(file_links)


def download_zips(zip_links, out_dir):
    try:
        os.makedirs(out_dir)
    except FileExistsError:
        print(out_dir + " already exists")
    except OSError:
        print(out_dir + " already exists")
    for link in zip_links:
        file_name = link.split('/')[-1]
        #make get request to url where zip is located
        r = requests.get(link, stream = True)
        if r.ok:
            #print("Downloading: " + file_name)
            z = zipfile.ZipFile(io.BytesIO(r.content))
            try:
                os.makedirs(out_dir + file_name.split('.')[0])
            except OSError:
                print(file_name.split('.')[0] + " already exists")
            z.extractall(path=out_dir + file_name.split('.')[0])


def find_and_download(url, outdir):
    zips = get_file_links(url)
    download_zips(zips, out_dir = outdir)
