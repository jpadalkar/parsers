"""File for crawling various parts of sec.gov"""

import requests
import zipfile
import io
from bs4 import BeautifulSoup


def get_file_links(archive_url, filetype='zip'):
    r = request.get(archive_url)
    soup = BeautifulSoup(r.content, 'html5lib')
    links = soup.findAll('a')
    file_links = [archive_url + link['href'] for link in links if link['href'].endswith(filetype)]
    return(zip_links)


def download_zips(zip_links, out_dir):
    try:
        os.makedirs(out_dir)
    except FileExistsError:
        print("Target directory for zip files already exists")
    except OSError:
        print("Target directory for zip files already exists")
    for link in zip_links:
        file_name = link.split('/')[-1]
        print("Downloading: " + file_name)
        #make get request to url where zip is located
        r = requests.get(link, stream = True)
        if r.ok:
            z = zipfile.ZipFile(io.BytesIO(r.content))
            z.extractall(path=out_dir)
