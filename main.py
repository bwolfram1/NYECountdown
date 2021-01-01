import board
import dotstar_featherwing
import time
import busio as io
import adafruit_ds3231
import font3

wing = dotstar_featherwing.DotstarFeatherwing(board.D13, board.D11)

i2c = io.I2C(board.SCL, board.SDA)  # Change to the appropriate I2C clock & data
# pins here!

# Create the RTC instance:
rtc = adafruit_ds3231.DS3231(i2c)

WAITING = 0
DROPPING = 1
NEWYEAR = 2

xmas_colors = {'w': ( 32,  32,  10),
               'y': ( 32,  32,   0)}

xmas_animation = [["w.w.w.w.w.w.",
                   ".w.w.w.w.w.w",
                   "w.w.w.w.w.w.",
                   ".w.w.w.w.w.w",
                   "w.w.w.w.w.w.",
                   ".w.w.w.w.w.w"],
                  [".w.w.w.w.w.w",
                   "w.w.w.w.w.w.",
                   ".w.w.w.w.w.w",
                   "w.w.w.w.w.w.",
                   ".w.w.w.w.w.w",
                   "w.w.w.w.w.w."]]

days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
TESTING = False
TimeTesting = False
STATE = WAITING

# pylint: disable-msg=using-constant-test
if TESTING == True:  # change to True if you want to set the time!
    #                     year, mon, date, hour, min, sec, wday, yday, isdst
    t = time.struct_time((2020, 12, 31, 00, 00, 00, 0, -1, -1))
    # you must set year, mon, date, hour, min, sec and weekday
    # yearday is not supported, isdst can be set but we don't do anything with it at this time
    print("Setting time to:", t)  # uncomment for debugging
    rtc.datetime = t
    print()
else: 
    t = time.struct_time((2020, 12, 31, 23, 24, 30, 4, -1, -1))
    # you must set year, mon, date, hour, min, sec and weekday
    # yearday is not supported, isdst can be set but we don't do anything with it at this time
    print("Setting time to:", t)  # uncomment for debugging
    rtc.datetime = t
    print()
    
while True:
    now = time.monotonic()
    t = rtc.datetime
    #print(
    #    "The date is {} {}/{}/{}".format(
    #        days[int(t.tm_wday)], t.tm_mday, t.tm_mon, t.tm_year
    #    )
    #)
    #print("The time is {}:{:02}:{:02}".format(t.tm_hour, t.tm_min, t.tm_sec))
    if STATE == WAITING:
        if TESTING or (t.tm_mday == 31 and
                        t.tm_mon == 12 and
                        t.tm_hour == 23 and
                        t.tm_min == 59 and
                        t.tm_sec == 50):
                            STATE = DROPPING
        else:
            print(
                "The date is {} {}/{}/{}".format(
                    days[int(t.tm_wday)], t.tm_mday, t.tm_mon, t.tm_year
                )
            )
            print("The time is {}:{:02}:{:02}".format(t.tm_hour, t.tm_min, t.tm_sec))
    elif STATE == DROPPING:
        wing.clear()
        wing.shift_in_string(font3.font, "10", (32, 32, 32), 0.2)
        time.sleep(0.8)
        wing.clear()
        wing.shift_in_string(font3.font, "9", (32, 32, 32), 0.2)
        time.sleep(0.8)
        wing.clear()
        wing.shift_in_string(font3.font, "8", (32, 32, 32), 0.2)
        time.sleep(0.8)
        wing.clear()
        wing.shift_in_string(font3.font, "7", (32, 32, 32), 0.2)
        time.sleep(0.8)
        wing.clear()
        wing.shift_in_string(font3.font, "6", (32, 32, 32), 0.2)
        time.sleep(0.8)
        wing.clear()
        wing.shift_in_string(font3.font, "5", (32, 32, 32), 0.2)
        time.sleep(0.8)
        wing.clear()
        wing.shift_in_string(font3.font, "4", (32, 32, 32), 0.2)
        time.sleep(0.8)
        wing.clear()
        wing.shift_in_string(font3.font, "3", (32, 32, 32), 0.2)
        time.sleep(0.8)
        wing.clear()
        wing.shift_in_string(font3.font, "2", (32, 32, 32), 0.2)
        time.sleep(0.8)
        wing.clear()
        wing.shift_in_string(font3.font, "1", (32, 32, 32), 0.2)
        time.sleep(0.8)
        wing.clear()
        STATE = NEWYEAR
    elif STATE == NEWYEAR:
        wing.clear()
        wing.display_animation(xmas_animation, xmas_colors, 10, 0.1)
        wing.shift_in_string(font3.font, "Happy New Year!", (32, 32, 32), 0.1)
        wing.shift_in_string(font3.font, " 2021!", (32, 32, 32), 0.1)
        wing.clear()
    if TimeTesting:
        TESTING = False
        print(
            "The date is {} {}/{}/{}".format(
                days[int(t.tm_wday)], t.tm_mday, t.tm_mon, t.tm_year
            )
        )
        print("The time is {}:{:02}:{:02}".format(t.tm_hour, t.tm_min, t.tm_sec))
    time.sleep(1)
