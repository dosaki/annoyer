import random

class Reader(object):
    def __init__(self, file_path):
        self.file_path = file_path
        with open(file_path) as f:
            self.lines = [line.strip() for line in f]

    def getRandomLine(self):
            return self.lines[random.randrange(len(self.lines) - 1)]
