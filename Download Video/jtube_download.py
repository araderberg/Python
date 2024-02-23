###Program Name: jtube_download.py
###Programmer: Aaliyah Raderberg
###Project: Python to download video

#make sure you have pytube installed. You can install it via pip
#pip install pytube

from pytube import YouTube
import os

def download_video(url, output_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path)
        print("Video downloaded successfully.")
    except Exception as e:
        print(f"An error occurred while downloading the video: {e}")

def main():
    url = input("Enter the YouTube video URL: ")
    output_path = input("Enter the output directory to save the video: ")

    # Check if the output directory exists, if not create it
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    download_video(url, output_path)

if __name__ == "__main__":
    main()
