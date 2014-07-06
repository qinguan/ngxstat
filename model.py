__author__ = 'xuguojun'

import time
import logging


def to_int(value):
    return int(value) if value and value != '-' else 0


class Field(object):
    def __init__(self, field, locate, sep=None):
        self.field = field
        self.sep = sep
        self.locate = locate
        self.dict = {}

    def incre(self, key):
        if self.sep is not None:
            #TODO hardcode the word location
            #/apis/msg/mixer/navall.action?uid=123 => /apis/msg/mixer/navall.action
            key = key.split(self.sep)[0]

        if key in self.dict.keys():
            self.dict[key] += 1
        else:
            self.dict[key] = 1

    def sort(self):
        return sorted(self.dict.items(), key=lambda e: e[1], reverse=True)

    def to_string(self):
        logging.info("field:%s, locate:%s, sep:%s" % (self.field, self.locate, self.sep))
        for key in self.dict:
            logging.info('key=%s, value=%s' % (key, self.dict[key]))


class LogResult(object):
    def __init__(self, conf_path):
        self.begin = time.time()
        self.field_dict = {}
        self.init_result(conf_path)

    def init_result(self, conf_path):
        lines = open(conf_path).readlines()
        for line in lines:
            if line.startswith("field"):
                words = line.strip("\n").split(":")
                assert len(words) == 2, "the configuration is not valid." + line

                fields = words[1].split("=")
                assert len(fields) == 2, "the configuration is not valid." + line
                field = fields[0].strip()
                locate = fields[1].strip()
                self.field_dict[to_int(locate)] = Field(field, locate)
            elif line.startswith("refine_field"):
                words = line.strip("\n").split(":")
                assert len(words) == 4, "the configuration is not valid." + line
                #field = words[1]
                locate = words[2]
                sep = words[3]

                self.field_dict[to_int(locate)].sep = sep

        if len(self.field_dict.keys()) == 0:
            logging.error("key field in access log format should be specified.")

    def sorted_by_field(self, field, limit=-1):
        for _ in self.field_dict.values():
            if _.field == field:
                return field, _.sort()[0:limit]

    def print_result(self):
        for value in self.field_dict.values():
            logging.info(value.to_string())

if __name__ == "__main__":
    pass