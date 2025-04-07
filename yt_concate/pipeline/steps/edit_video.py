from moviepy import VideoFileClip

from .step import Step

class EditVideo(Step):
    def process(self, data, inputs, utils):
        VideoFileClip("long_examples/example2.mp4").subclipped(10, 20)
