import requests
import datetime
from urllib import quote

def calculateTimeToLookForInSchedule(date):
    minute = date.minute
    hour = date.hour
    if minute == 0:
        return formatTime(hour, 0)
    elif minute > 30:
        return formatTime(hour + 1, 0)
    else:
        return formatTime(hour, 30)


def sendNotificationToSlackFor(entries, day, time):
    text = reduce(lambda x, y: x + '\n' + y,
                  map(lambda x: x['loc'][0] + ": " + x['title'], entries)
                  )
    text = "@channel *Now starting " + day + " " + time + "*\n" + text
    r = requests.post('$$$ADD_URL$$$',
                      data='{"text":"' + text.encode('utf-8') + '"}')


def formatTime(hour, minute):
    return '{num:02d}'.format(num=hour) + ':' + '{num:02d}'.format(num=minute)


now = datetime.datetime.now()
r = requests.get('https://raw.githubusercontent.com/swacamp/web/gh-pages/schedule/program.json')

minute = now.minute
timeToLookFor = calculateTimeToLookForInSchedule(now)
#timeToLookFor="15:00"
dateToLookFor = str(datetime.date.today())
json = r.json()
forDay = filter(lambda x: x['date'] == dateToLookFor, json)
forTime = filter(lambda x: x['time'] == timeToLookFor, forDay)

print forDay
print forTime
if len(forTime) > 0:
    sendNotificationToSlackFor(forTime, dateToLookFor, timeToLookFor)

