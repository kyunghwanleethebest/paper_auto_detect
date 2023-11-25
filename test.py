import schedule
import time

def message1():
    print("스케쥴 실행중...")

def message2(text):
    print(text)

# 주기 설정
job1 = schedule.every(1).seconds.do(message1)
job2 = schedule.every(2).seconds.do(message2,'2초마다 알려줄게요')


count = 0

while True:

    schedule.run_pending()
    time.sleep(1)

    count = count + 1

    if count > 5:
        schedule.cancel_job(job1)