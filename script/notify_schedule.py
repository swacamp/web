import requests
import datetime


def calculateTimeToLookForInSchedule(date):
    minute = date.minute
    hour = date.hour
    if minute == 0:
        return formatTime(hour, 0)
    elif minute > 30:
        return formatTime(hour + 1, 0)
    else:
        return formatTime(hour, 30)


def sendNotificationToSlackFor(entries):
    text = reduce(lambda x, y: x + '\n' + y,
                  map(lambda x: x['loc'][0] + ": " + x['title'], entries)
                  )
    text = "*Now starting*:\n" + text
    requests.post('https://hooks.slack.com/services/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',
                      data='{"text":"' + text + '"}')


def formatTime(hour, minute):
    return '{num:02d}'.format(num=hour) + ':' + '{num:02d}'.format(num=minute)


now = datetime.datetime.now()
r = requests.get('http://swacamp.org/schedule/program.json')

minute = now.minute
#timeToLookFor = calculateTimeToLookForInSchedule(now)
dateToLookFor = str(datetime.date.today())
timeToLookFor="10:30"


json = r.json()
forDay = filter(lambda x: x['date'] == dateToLookFor, json)
forTime = filter(lambda x: x['time'] == timeToLookFor, forDay)

print dateToLookFor + " " + timeToLookFor + ": found:" + str(forTime)
