import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
import sys
import yaml
from tqdm import tqdm


def Data_downloader(year, start_idx, end_idx):
    url = "https://www.ncei.noaa.gov/data/local-climatological-data/access/"+f"{year}"+"/"
    download_path  = "/Users/anikbhowmick/Python/Big_Data_Assignment/A03/Downloaded_Data/"
    os.mkdir("/Users/anikbhowmick/Python/Big_Data_Assignment/A03/Downloaded_Data")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    csv_files = []
    for link in soup.find_all("a"): 
        href = link.get("href")
        if href.endswith(".csv"):
            csv_name = href.split("/")[-1]
            csv_files.append(csv_name)

    downloadable_csvs = csv_files[start_idx: end_idx]
    
    for csv_name in tqdm(downloadable_csvs):
        csv_url = urljoin(url, csv_name)
        response = requests.get(csv_url)
        with open(os.path.join(download_path, csv_name), "wb") as f:
            f.write(response.content)

if __name__ == "__main__":
    params = yaml.safe_load(open("params.yaml"))["Data_downloader"]
    year = params["year"]
    start_idx = params["start_idx"]
    end_idx = params["end_idx"]
    Data_downloader(year, start_idx, end_idx)

