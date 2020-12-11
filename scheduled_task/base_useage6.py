# from datetime import datetime
# from apscheduler.schedulers.blocking import BlockingScheduler
#
# def job_func():
#      print("当前时间：", datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")
#
# scheduler = BlockingScheduler()
#
# # 每2小时触发
# scheduler.add_job(job_func, 'interval', hours=2)
#
# # 在 2019-04-15 17:00:00 ~ 2019-12-31 24:00:00 之间, 每隔两分钟执行一次 job_func 方法
# scheduler .add_job(job_func, 'interval', minutes=2, start_date='2019-04-15 17:00:00' , end_date='2019-12-31 24:00:00')
#
# scheduler.start()

from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

def show(root):
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

if __name__ == '__main__':

    # root.attributes("-fullscreen", True)

    scheduler=BackgroundScheduler()
    # scheduler=BlockingScheduler()
    scheduler.add_job(show,"date",run_date=datetime(2020,12,11,11,27,20))
    scheduler.start()
    while True:
        pass