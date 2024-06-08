this lets your slayer bot on binmaster easily take breaks, nothing else, read the python file for any fields that need to be changed

# installation:
1. download python 3.12 (make sure to check `add python.exe to path`)
2. clone or download the repo
3. open main.py in any text editor to see all fields that need to be changed (at the top)
4. open cmd and run `pip install -r requirements.txt`
5. open cmd and enter `py main.py`

# easy variable explanation
- `exe` (string): Path to your binmaster executable
- `wh_url` (string): Discord Webhook URL
- `active_time` (int): Base time of running
- `break_time` (int): Base time of the break
- `active_randomization` (int): Randomization of running time
- `break_randomization` (int): Randomization of break time
- `warning_time` (int): Warns you N of minutes until finishing the break


(also you can open issues to suggest features)

dm me on discord for support: hvhnn
