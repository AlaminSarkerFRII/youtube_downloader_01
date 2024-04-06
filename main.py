from flask import Flask, render_template, request, redirect, url_for
from youtube_videos import download_youtube_videos

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_url = request.form['video_url']
        download_youtube_videos(video_url)
        return redirect(url_for('index', downloaded=True))
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
