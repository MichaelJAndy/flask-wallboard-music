import time

__author__ = 'mandreacchio'


class Alarms(object):

    @staticmethod
    def alarm(time_param):
        print('{} Alarm! This alarm was scheduled at {}.'.format(time.strftime("%H:%M:%S"), time_param))
