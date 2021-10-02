import time
from plyer import notification



if __name__ == "__main__":
    title = input(str("What is title of the message: \n"))
    message = input(str("What is the message: \n"))
    tm = input("After how many seconds you want to repeat it: \n")
    tm = int(tm)
    while True:
        notification.notify(title=title, message=message ,timeout=2,)
        time.sleep(tm)
