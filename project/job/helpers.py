import time
import webbrowser

__author__ = 'mandreacchio'


class Alarms(object):

    @staticmethod
    def alarm(time_param):
        print('{} Alarm! This alarm was scheduled at {}.'.format(time.strftime("%H:%M:%S"), time_param))

    @staticmethod
    def browser_alarm(event_id):
        print(time.strftime("%H:%M:%S"), "Browser Alarm Triggered")
        # TODO: try to use url_for insetad of hardcoded URL
        webbrowser.open('http://127.0.0.1:5000/songs/playrandom/{}'.format(event_id))


