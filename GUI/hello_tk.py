import tkinter as tk
import threading

class App(tk.Frame):
    pass

def test_hello_tk():
    root=tk.Tk()
    root.title("hahah")
    root.mainloop()

if __name__ == '__main__':
    # test_hello_tk()
    try:
        t = threading.Thread(target=test_hello_tk)
        t.start()
        t.join()
    except:
        print('exception')

