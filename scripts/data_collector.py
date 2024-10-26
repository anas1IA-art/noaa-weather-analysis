import os
import requests
import gzip
from bs4 import BeautifulSoup

class NOAADataDownloader:
    def __init__(self, station_name, data_directory="data_f"):
        self.station_name = station_name
        self.station_list_url = "https://www1.ncdc.noaa.gov/pub/data/noaa/isd-history.txt"
        self.base_data_url = "https://www1.ncdc.noaa.gov/pub/data/noaa/"
        self.data_directory = data_directory
        os.makedirs(data_directory, exist_ok=True)

        # Retrieve station metadata
        self.station_id, self.country, self.start_year, self.end_year = self._get_station_info()
        if not all([self.station_id, self.start_year, self.end_year]):
            raise ValueError("Station not found or has invalid year data.")

    def _get_station_info(self):
        """Retrieve station metadata including USAF ID, country code, start year, and end year."""
        try:
            response = requests.get(self.station_list_url)
            response.raise_for_status()
            lines = response.text.splitlines()

            for line in lines:
                if self.station_name in line:
                    usa_fid = line[0:6].strip()
                    country = line[43:46].strip()

                    start_year = self._safe_int(line[82:86].strip())
                    end_year = self._safe_int(line[90:95].strip())

                    return usa_fid, country, start_year, end_year
        except Exception as e:
            print(f"Error retrieving station info: {e}")
        return None, None, None, None

    def _safe_int(self, value):
        """Convert a string to an integer, returning None if conversion fails."""
        try:
            return int(value)
        except ValueError:
            return None

    def download_all_data(self):
        """Download and decompress data files for the specified station and years."""
        for year in range(self.start_year, self.end_year + 1):
            year_url = f"{self.base_data_url}{year}/"
            try:
                response = requests.get(year_url)
                response.raise_for_status()
                self._process_year_data(response.text, year_url, year)
            except Exception as e:
                print(f"Error accessing data for year {year}: {e}")

    def _process_year_data(self, html_content, year_url, year):
        """Process HTML content to find relevant files for the station and download them."""
        soup = BeautifulSoup(html_content, 'html.parser')
        for link in soup.find_all('a', href=True):
            filename = link['href']
            if filename.startswith(f"{self.station_id}-99999-{year}"):
                file_url = f"{year_url}{filename}"
                self._download_and_decompress(file_url, filename)

    def _download_and_decompress(self, file_url, filename):
        """Download a .gz file and decompress it to .txt in the data directory."""
        gz_path = os.path.join(self.data_directory, filename)
        txt_path = gz_path.replace('.gz', '.txt')

        try:
            response = requests.get(file_url, stream=True)
            response.raise_for_status()
            with open(gz_path, "wb") as gz_file:
                for chunk in response.iter_content(1024):
                    gz_file.write(chunk)
            print(f"Downloaded {gz_path}")

            with gzip.open(gz_path, 'rb') as f_in, open(txt_path, 'wb') as f_out:
                f_out.write(f_in.read())
            print(f"Decompressed to {txt_path}")

            os.remove(gz_path)  # Clean up the .gz file
        except Exception as e:
            print(f"Error processing {filename}: {e}")


