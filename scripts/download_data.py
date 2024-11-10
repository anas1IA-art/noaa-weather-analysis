import argparse
from scripts.data_collector import NOAADataDownloader

def  download():
    parser = argparse.ArgumentParser(description='Download NOAA weather data for a specified station.')
    parser.add_argument('station_name', type=str, help='The name of the weather station to download data for')
    parser.add_argument('data_directory', type=str, default='data', help='Directory to store downloaded data (default: data)')

    args = parser.parse_args()

    try:
        downloader = NOAADataDownloader(args.station_name, args.data_directory)
        print(f"the information of your staton {args.station_name} are {list(downloader._get_station_info())}")
        downloader.download_all_data()
    except ValueError as e:
        print(e)
