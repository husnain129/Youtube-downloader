from fastapi import FastAPI
from pytube import YouTube
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Download(BaseModel):
    link: str
    type: Optional[str] = "mp4"


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/download")
def youtube_video_download(body: Download):
    try:
        download(body.link, body.type)
        return {"status": "downloaded"}

    except Exception as e:
        return {"status": "fail", "error": str(e)}


@app.get("/download")
def youtube_video_download(type: Optional[str] = "mp4", link: str = None):
    try:
        download(link, type)
        return {"status": "downloaded"}
    except Exception as e:
        return {"status": "fail", "error": str(e)}


def download(link, type):
    yt = YouTube(link)

    if type == "mp3":

        yt.streams.get_audio_only().download(output_path="mp3")
    else:
        yt.streams.get_highest_resolution().download(output_path="mp4")
