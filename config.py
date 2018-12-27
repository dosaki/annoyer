import configparser, os

class Config(object):
    def __init__(self, file_path):
        self.config = configparser.ConfigParser()
        self.config.read(file_path)

    def get(self, section):
        dict1 = {}
        options = self.config.options(section)
        for option in options:
            try:
                dict1[option] = self.config.get(section, option)
                if dict1[option] == -1:
                    DebugPrint("skip: %s" % option)
            except:
                print("exception on %s!" % option)
                dict1[option] = None
        return dict1
