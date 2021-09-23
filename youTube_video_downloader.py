import pytube, time
from pytube.cli import on_progress
url = input('Enter a YouTube video link: ')
yt = pytube.YouTube(url, on_progress_callback=on_progress)
print(f'The video is being downloaded | {yt.title}')
print(yt.thumbnail_url)
time.sleep(1)
video=yt.streams.get_highest_resolution()
time.sleep(1)
video.download()
time.sleep(1)