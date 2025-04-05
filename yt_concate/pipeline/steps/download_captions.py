from pytubefix import YouTube

from yt_concate.pipeline.steps.step import Step


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        print('In download_captions')
        for yt in data:
            print('Downloading caption:', yt.url)
            if utils.caption_file_exists(yt):
                print('Caption downloaded:', yt.url)
                continue

            youtube = YouTube(yt.url)
            try:
                caption = youtube.captions['a.en']
            except KeyError:
                print('KeyError occurs for caption:', yt.url)
                continue

            en_caption_convert_to_srt = (caption.generate_srt_captions())

            text_file = open(yt.caption_filepath, "w", encoding="utf-8")
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
        return data

