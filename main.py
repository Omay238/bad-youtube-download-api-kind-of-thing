from flask import Flask, send_file
from pytube import YouTube

app = Flask(__name__)

def download_video(video_id):
    video = YouTube(f"https://youtu.be/{video_id}")
    return video

@app.route("/<youtube_id>")
def send_video(youtube_id):
    video = download_video(youtube_id)

    video.streams.get_highest_resolution().download(output_path="downloads", filename=f"{video.title}.mp4")

    return send_file(f"./downloads/{video.title}.mp4", mimetype="video/mp4")

if __name__ == "__main__":
    app.run()
