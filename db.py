__author__ = 'xuguojun'

import sqlite3
from contextlib import closing
import logging


class SQL(object):
    def __init__(self, fields, index_fields=None):
        self.column_list = ','.join(fields)
        self.holder_list = ','.join(':%s' % var for var in fields)
        self.index_fields = index_fields if index_fields is not None else []
        self.conn = sqlite3.connect(':memory:')
        self.init_db()

    def init_db(self):
        create_table = 'create table nginx (%s)' % self.column_list
        with closing(self.conn.cursor()) as cursor:
            logging.info('sqlite init: %s', create_table)
            cursor.execute(create_table)
            for idx, field in enumerate(self.index_fields):
                sql = 'create index log_idx%d on nginx (%s)' % (idx, field)
                logging.info('sqlite init: %s', sql)
                cursor.execute(sql)

    def insert(self, field_dict):
        pass