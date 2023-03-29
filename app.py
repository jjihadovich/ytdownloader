from flask import Flask, render_template
from forms import YtSearch
from pytube import YouTube




app = Flask(__name__)
app.config['SECRET_KEY'] = 'nigga'

@app.route('/', methods=['GET', 'POST'])
def index():
    vidtitle = ""
    vidimg = ""
    load = ""
    loadaudio = ""
    loadvideo = ""
    audio = ""
    video = ""
    author = ""
    imagecss = ""
    wait = "Вставьте Ссылку!"
    form = YtSearch()
    link = form.link
    if form.is_submitted():
        try:
            print("pressed")
            wait = "Ожидайте!"
            yt = YouTube(form.link.data)
            vidtitle = yt.title
            vidimg = yt.thumbnail_url
            imagecss = "border: 4px solid white;"
            load = "Скачать"
            audio = "Аудио"
            video = "Видео"
            loadaudio = yt.streams.get_audio_only().url
            loadvideo = yt.streams.get_highest_resolution().url
            wait = ""
            print("loaded")
        except:
            wait = "Очевидно, произошла ошибка. Проверьте подлинность введенной ссылки или перезагрузите страницу ¯\_(ツ)_/¯"
            print("error")



    return render_template("index.html", form=form, vidtitle=vidtitle, vidimg=vidimg, load=load, loadaudio=loadaudio, loadvideo=loadvideo, audio=audio, video=video, wait=wait, imagecss=imagecss)

if __name__ == "__main__":
    app.run(debug=True)