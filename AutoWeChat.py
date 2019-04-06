import requests
import json
from wxpy import *
from apscheduler.schedulers.blocking import BlockingScheduler


bot = Bot(cache_path=True, console_qr=True)

def getWeather():
    url = 'http://t.weather.sojson.com/api/weather/city/101100201'
    r = requests.get(url)
    t = r.text
    data = json.loads(t)
    print(data)
    city = data['cityInfo']['city']
    # 今日信息
    today = data['data']['forecast'][0]['ymd']
    today_week = data['data']['forecast'][0]['week']
    today_hightem = data['data']['forecast'][0]['high']
    today_lowtem = data['data']['forecast'][0]['low']
    today_win = data['data']['forecast'][0]['fx'] + ' ' + data['data']['forecast'][0]['fl']
    today_wea = data['data']['forecast'][0]['type']
    today_aqi = data['data']['forecast'][0]['aqi']
    today_notice = data['data']['forecast'][0]['notice']

    # 明日信息
    tomorrow = data['data']['forecast'][1]['ymd']
    tomorrow_week = data['data']['forecast'][1]['week']
    tomorrow_hightem = data['data']['forecast'][1]['high']
    tomorrow_lowtem = data['data']['forecast'][1]['low']
    tomorrow_win = data['data']['forecast'][1]['fx'] + ' ' + data['data']['forecast'][1]['fl']
    tomorrow_wea = data['data']['forecast'][1]['type']
    tomorrow_aqi = data['data']['forecast'][1]['aqi']
    tomorrow_notice = data['data']['forecast'][1]['notice']

    info = city + '\n' + '今日天气:\n' + today + ' ' + today_week + '\n' + today_hightem + ' ' + today_lowtem + '\n' + today_wea + ' ' + '空气质量指数: ' + str(
        today_aqi) + '\n' + today_notice + '\n' + '明日天气:\n' + tomorrow + ' ' + tomorrow_week + '\n' + tomorrow_hightem + ' ' + tomorrow_lowtem + '\n' + tomorrow_wea + ' ' + '空气质量指数: ' + str(
        tomorrow_aqi) + '\n' + tomorrow_notice
    return info

def sendNews():
    try:
        contents = getWeather()
        my_friend = bot.friends().search('玫瑰')[0]
        my_friend.send(contents)

    except:
        my_friend = bot.friends().search('Anonymous')[0]
        my_friend.send('今天消息发送失败了')


def main():

    sc = BlockingScheduler()
    sc.add_job(sendNews, 'cron', hour=7, minute=1, second=10)
    sc.start()


if __name__ == '__main__':
    main()



