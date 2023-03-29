from pytube import YouTube
url = 'https://www.youtube.com/watch?v=NVPZM_jy-sk&ab_channel=MOKS346'
yt = YouTube(url)
streams = yt.streams.filter(progressive=True)
print(streams)

formats = yt.streams.filter(file_extension='mp4').all()

# Выведите список форматов
for f in formats:
    print(f)