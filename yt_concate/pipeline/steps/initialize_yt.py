from .step import Step
from yt_concate.model.yt import YT


class InitializeYT(Step):
    def process(self, data, inputs, utils):
        print('In InitializeYT')
        return [YT(url) for url in data]
