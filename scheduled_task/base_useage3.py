import time
from apscheduler.schedulers.background import BackgroundScheduler


def job():
    print('job:', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


if __name__ == '__main__':
    # BackgroundScheduler: 适合于要求任何在程序后台运行的情况，当希望调度器在应用后台执行时使用。
    scheduler = BackgroundScheduler()
    # 采用非阻塞的方式

    # 采用固定时间间隔（interval）的方式，每隔3秒钟执行一次
    scheduler.add_job(job, 'interval', seconds=3)
    # 这是一个独立的线程
    scheduler.start()

    # 其他任务是独立的线程
    while True:
        print('main-start:', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        time.sleep(2)
        print('main-end:', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))