import subprocess as sp
import time as t
from discord_webhook import DiscordWebhook as dwh
import random as r
from datetime import datetime as dt, timedelta as td
from threading import Thread

exe = ""      # (string): Path to the executable file of Binmaster
wh_url = ""   # (string): URL for the Discord webhook used for notifications


active_time = 30            # (int): Base duration for active running time in minutes
break_time = 20             # (int): Base duration for break time in minutes
active_randomization = 12   # (int): Randomization range for active running time in minutes
break_randomization = 12    # (int): Randomization range for break time in minutes
warning_time = 5            # (int): Time in minutes to warn before the break ends




base_run_dur = active_time * 60
base_sleep_dur = break_time * 60
run_var = active_randomization * 60
sleep_var = break_randomization * 60
soontime = warning_time * 60

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

def read_output(proc):
    while True:
        try:
            output = proc.stdout.readline()
            if output == '' and proc.poll() is not None:
                break
            if output:
                print(output.strip())
        except UnicodeDecodeError:
            print("line unicode decode error, line skipped")
            continue

while True:
    rundur = randomdur(base_run_dur, run_var)
    sleepdur = randomdur(base_sleep_dur, sleep_var)
    run_end_time = formatend(rundur)
    start_msg = f"starting binmaster until {run_end_time} ({formatdur(rundur)})..."
    print(start_msg)
    webhook(start_msg)
    proc = sp.Popen([exe], stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE, text=True)
    output_thread = Thread(target=read_output, args=(proc,))
    output_thread.start()
    t.sleep(rundur)
    stop_msg = f"stopping binmaster"
    print(stop_msg)
    webhook(stop_msg)
    proc.stdin.write("pause\n")
    proc.stdin.flush()
    t.sleep(3)
    proc.terminate()
    output_thread.join()
    sleep_end_time = formatend(sleepdur)
    sleep_msg = f"taking a break until {sleep_end_time} ({formatdur(sleepdur)})..."
    print(sleep_msg)
    webhook(sleep_msg)
    t.sleep(sleepdur - soontime)
    soonmsg = f"continuing in {warning_time} minutes..."
    print(soonmsg)
    webhook(soonmsg)
    t.sleep(soontime)
