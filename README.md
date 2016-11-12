# What is this?
This is a little script to send a random fact every X minutes to a person.

# But... Why?
To annoy [this man here](https://github.com/mfontoura) as part of the International Annoy Mitó Day

# Requirements
* Python 2.7 + Pip:
  * Windows: [Download here](https://www.python.org/ftp/python/2.7.12/python-2.7.12.msi)
  * Linux (Debian): `apt-get -y install build-essential checkinstall libbz2-dev libsqlite3-dev libreadline-dev zlib1g-dev libncurses5-dev libssl-dev libgdbm-dev python python-pip`
  * MacOS: [¯\\\_(ツ)\_/¯](https://www.python.org/downloads/release/python-2712/)
* Twilio Library
  * On a command line type: `pip install twilio`

# How to Use
1. Simply register for a [free twilio account](https://www.twilio.com/try-twilio).
  1. ![Twilio: Fill your details](https://raw.githubusercontent.com/dosaki/annoyer/master/1_fill_your_details.png)
  2. ![Twilio: Insert Number](https://raw.githubusercontent.com/dosaki/annoyer/master/2_insert_number.png)
2. Fill in the twilio details in `twilio.cfg`:
```
[twilio]
number: +351123456789
account: ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
token: yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
```
3. Fill in the victims number in `twilio.cfg`:
```
[victim]
number: +351987654321
```
4. Open a command line and type `python annoyer.py`

## Bonus: Scheduling
You could schedule the script to happen every 15 minutes or so.
### On Linux
If you're on a linux environment:
1. On a terminal type `crontab -e`
2. Insert the line: `*/15 * 12 11 * python /path/to/the/script/annoyer.py >/dev/null 2>&1`
  * The line above makes the script run every 15 minutes on the 12th of November
3. Do your best evil laugh!

### On Windows
Open the `Task Scheduler`:
  * Press `Windows Key` + `R`
  * Type `taskschd.msc`
  * Press `Enter`

Follow the steps below:

1. ![General](https://raw.githubusercontent.com/dosaki/annoyer/master/w_1_general.png)
2. ![Trigger](https://raw.githubusercontent.com/dosaki/annoyer/master/w_2_trigger.png)
3. ![Action](https://raw.githubusercontent.com/dosaki/annoyer/master/w_3_action.png)
4. ![Conditions](https://raw.githubusercontent.com/dosaki/annoyer/master/w_4_conditions.png)
5. ![Settings](https://raw.githubusercontent.com/dosaki/annoyer/master/w_5_settings.png)
