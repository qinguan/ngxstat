__author__ = 'xuguojun'

import time
from contextlib import closing


def process(lines, result):
    for line in lines:
        process_line(line, result)
    return result


def process_line(line, nginx_result):
    """
    Process a given line and save data to nginx_result.
    """
    words = line.split()
    for locate in nginx_result.field_dict.keys():
        field_key = words[locate]
        nginx_result.field_dict[locate].incre(field_key)

    return nginx_result

def follow_line(file_path):
    """
    Follow a given file and yield new lines when they are available, like `tail -f`.
    """
    with open(file_path) as f:
        f.seek(0, 2)  # seek to eof
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.1)  # sleep briefly before trying again
                continue
            yield line


def read_lines(file_path):
    """
    :return: lines from given file.
    """
    with closing(open(file_path)) as f:
        return [_ for _ in f.readlines()]


def report(field, list):
    """
    format output.
    :return:
    """
    print "%6.6s\t%s" % ("number", field)
    for item in list:
        print "%6.6s\t%s" % (item[1], item[0])


if __name__ == "__main__":
    import os
    """
    lines = follow_line(os.getcwd() + "/follow.log")
    for line in lines:
        print line
    """
    field = ["number","request"]
    list = [('/apis/msg/hasnew.action', 9494), ('/apis/msg/mixer/navall.action', 6107), ('/apis/msg/update_status.action', 788), ('http://notice.iqiyi.com/apis/msg/hasnew.action', 738), ('/favicon.ico', 433), ('/apis/msg/list_messages.action', 271), ('/apis/msg/update_all_status.action', 190), ('http://notice.iqiyi.com/apis/msg/mixer/navall.action', 162), ('/apis/msg/del.action', 150), ('/apis/msg/send_private_msg.action', 136)]
    report(field, list)