import pytube, time
url = input('#> Enter the video link: ')
yt = pytube.YouTube(url)
print(f'The video is being downloaded | {yt.title}')
video=yt.streams.first()
video.download()