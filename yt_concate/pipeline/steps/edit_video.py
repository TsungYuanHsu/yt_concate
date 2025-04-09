from moviepy import VideoFileClip
from moviepy import concatenate_videoclips

from .step import Step

class EditVideo(Step):
    def process(self, data, inputs, utils):
        print('In EditVideo')
        clips = []
        for found in data:
            print(found.time)
            yt = found.yt
            start_time, end_time = self.parse_caption_time(found.time)
            video_clip = VideoFileClip(yt.get_video_filepath()).subclipped(start_time, end_time)
            clips.append(video_clip)
            if len(clips) > inputs['limit']:
                break

        final_clip = concatenate_videoclips(clips)
        output_path = utils.get_output_filepath(inputs['channel_id'], inputs['search_word'])
        final_clip.write_videofile(output_path)

    def parse_caption_time(self, caption_time):
        start_time, end_time = caption_time.split(' --> ')
        return self.parse_time_str(start_time), self.parse_time_str(end_time)

    def parse_time_str(self, time_str):
        h, m, s = time_str.split(':')
        s, ms = s.split(',')
        return int(h), int(m), int(s) + int(ms) / 1000