from .step import Step


class ReadCaption(Step):
    def process(self, data, inputs, utils):
        print('In ReadCaption')
        for yt in data:
            if not utils.caption_file_exists(yt):
                continue
            with open(yt.caption_filepath, 'r', encoding='utf-8') as f:
                captions = {}
                time_line = False
                time = None
                caption = None
                for line in f:
                    if '-->' in line:
                        time_line = True
                        time = line.strip()
                        continue
                    if time_line:
                        caption = line.strip()
                        captions[caption] = time
                        time_line = False
            yt.captions = captions
        return data






