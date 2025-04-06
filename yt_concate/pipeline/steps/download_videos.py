from pytubefix import YouTube
from pytubefix.cli import on_progress

from .step import Step
from yt_concate.settings import VIDEOS_DIR

class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        print('In DownloadVideos')
        yt_set = set([found.yt for found in data])
        for yt in yt_set:
            url = yt.url
            if utils.video_file_exists(yt):
                print(f'Youtube video exists for {url}')
                continue

            print(f'Downloading video for {url}')
            youtube = YouTube(url, on_progress_callback=on_progress)
            ys = youtube.streams.get_highest_resolution()
            ys.download(output_path=VIDEOS_DIR, filename=yt.id + '.mp4')

        return data

