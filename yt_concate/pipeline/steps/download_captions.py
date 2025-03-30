from pytubefix import YouTube

from yt_concate.pipeline.steps.step import Step


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        print('In download_captions')
        for url in data:
            print('Downloading caption:', url)
            if utils.caption_file_exists(url):
                print('Caption downloaded:', url)
                continue

            yt = YouTube(url)
            try:
                caption = yt.captions['a.en']
            except KeyError:
                print('KeyError occurs for caption:', url)
                continue

            en_caption_convert_to_srt = (caption.generate_srt_captions())

            text_file = open(utils.get_caption_filepath(url), "w", encoding="utf-8")
            text_file.write(en_caption_convert_to_srt)
            text_file.close()

