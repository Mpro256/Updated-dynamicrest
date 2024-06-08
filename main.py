import subprocess as sp
import time as t
from discord_webhook import DiscordWebhook as dwh
import random as r
from datetime import datetime as dt, timedelta as td

exe = "" # enter the path to binmaster slayer bot here
wh_url = "" # enter your discord webhook here

base_run_dur = 40 * 60 # in this case 40 is the amount of base minutes of running, you can set it to lower or higher but dont change the 60

base_sleep_dur = 20 * 60 # in this case 20 is the amount of base minutes of the break, you can set it to lower or higher but dont change the 60

run_var = 8 * 60 # here the minutes of running you set above get randomized by the range of 8 minutes, you can change this too but dont change the 60

sleep_var = 8 * 60 # here the minutes of the break you set above get randomized by the range of 8 minutes, you can change this too but dont change the 60

soontime = 5 * 60 # this defines how much minutes before it will warn you before continuing (so if 5 minutes are left till continuing it will notify on the webhook) if you change the 5 it will notify at a different time but the message wont change, so dont change it unless you need to

def randomdur(base, var):
    return base + r.randint(-var, var)

def webhook(msg):
    wh = dwh(url=wh_url, content=msg)
    wh.execute()

def formatdur(dur):
    mins = dur // 60
    secs = dur % 60
    return f"{mins} minutes and {secs} seconds"

def formatend(dur):
    endtime = dt.now() + td(seconds=dur)
    return endtime.strftime("%H:%M")

while True:
    rundur = randomdur(base_run_dur, run_var)
    sleepdur = randomdur(base_sleep_dur, sleep_var)
    run_end_time = formatend(rundur)
    start_msg = f"Starting Binmaster till {run_end_time} ({formatdur(rundur)})..."
    print(start_msg)
    webhook(start_msg)
    proc = sp.Popen([exe])
    t.sleep(rundur)
    stop_msg = f"Stopping Binmaster after {formatdur(rundur)}..."
    print(stop_msg)
    webhook(stop_msg)
    proc.terminate()
    sleep_end_time = formatend(sleepdur)
    sleep_msg = f"Taking a break till {sleep_end_time} ({formatdur(sleepdur)})..."
    print(sleep_msg)
    webhook(sleep_msg)
    t.sleep(sleepdur - soontime)
    soonmsg = "Continuing in 5 minutes..."
    print(soonmsg)
    webhook(soonmsg)
    t.sleep(soontime)
