"""
ngxtop - ad-hoc query for nginx access log.

Usage:
    main.py [options]

Options:
    -l <file>, --access-log <file>  access log file to parse.
    -h, --help  print this help message.
    -n <number>, --limit <number> limit the number of items in report. [default: 10]
    -k <field>, --key <key> sort the result by field.
    --version  print version information.
"""

__author__ = 'xuguojun'

from model import LogResult
from parse import *
import constant
import logging
from docopt import docopt

import fabric.api as fab
from fabric.network import disconnect_all
from contextlib import contextmanager
from fabric.context_managers import hide

@contextmanager
def ssh(settings):
    with settings:
        try:
            yield
        finally:
            from fabric.state import connections

            for key in connections.keys():
                connections[key].close()
                del connections[key]

            #disconnect_all()


def anonymous():
    with ssh(fab.settings(host_string="192.168.1.102", user="root", password="123456")):
        with hide('warnings', 'running', 'stdout', 'stderr'):
            res = fab.run('ls -l')
        for _ in res.split("\\n"):
            print _
        print res.command


def main():
    args = docopt(__doc__, version='ngxstat 0.0.1')

    logging.basicConfig(level=logging.INFO)
    result = LogResult(constant.CONF_PATH)

    log_path = args["--access-log"]
    if log_path is None:
        log_path = constant.LOG_PATH

    lines = read_lines(log_path)

    #lines = follow_line(os.getcwd() + "/follow.log")
    result = process(lines, result)

    field = args["--key"]
    if field is None:
        field = constant.DEFAULT_FIELD

    if args["--limit"] is None:
        limit = 10
    else:
        limit = int(args["--limit"])

    field, sorted_list = result.sorted_by_field(field, limit)
    report(field, sorted_list)

if __name__ == "__main__":
    anonymous()
    #main()
