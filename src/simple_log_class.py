from datetime import *
import time

class simple_log_class():
    def __init__(self, filename):
        self.filename = filename
        
    def write_log_without_timestamp(self, msg):
        try:
            file_handle = open(self.filename, 'a')
        except:
            return

        try:
            file_handle.write('%s\n' % msg)
        finally:
            file_handle.close()

    def write_log(self, msg):
        try:
            file_handle = open(self.filename, 'a')
        except:
            return

        try:
            file_handle.write('%s %s\n' % (time.ctime(), msg))
        finally:
            file_handle.close()

    def clear_log(self):
        try:
            file_handle = open(self.filename, 'w')
        except:
            return

        try:
            file_handle.write('')
        finally:
            file_handle.close()
