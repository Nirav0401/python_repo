
import schedule
import time
from plyer import notification
from win10toast import ToastNotifier

import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")

def job():
        notification.notify(
        title='Drink Water!',
        message='You should atleast drink 2 liter of water a day!',
        )
        speaker.Speak("Drink Water!, You should atleast drink 2 liters of water a day!")

# Schedule the job to run every 2 seconds
# schedule.every(5).seconds.do(job)

# Schedule the job to run every day at 12:00 PM
# schedule.every().day.at("11:15").do(job)

# Schedule the job to run every 30 minutes
# schedule.every(30).minutes.do(job)

# Schedule the job to run every 30 minutes
# schedule.every(1).hours.do(job)

# while loop schedules a job to run every 30 minutes for a total of 3 times
i = 0
while(i<3):
        schedule.every(30).minutes.do(job)
        i += 1

while True:
    # It continuously checks for pending scheduled jobs
    schedule.run_pending()
    time.sleep(1)