import time
from apscheduler.schedulers.blocking import BlockingScheduler


def job():
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


if __name__ == '__main__':
    # BlockingScheduler：在进程中运行单个任务，调度器是唯一运行的东西
    scheduler = BlockingScheduler()
    # 采用阻塞的方式

    # 采用date的方式，在特定时间只执行一次
    scheduler.add_job(job, 'date', run_date='2020-12-10 16:43:30')

    scheduler.start()