# just to show how much time a func has spent

import datetime


def time_usage(func):
    def wrapper(*args, **kwargs):
        begin_time = datetime.datetime.now()
        print('-------start-------')
        print('begin time:' + str(begin_time))
        retval = func(*args, **kwargs)
        end_time = datetime.datetime.now()
        print('end time:' + str(end_time))
        print('time usage:' + str(end_time - begin_time))
        print('--------end--------')
        return retval
    return wrapper
