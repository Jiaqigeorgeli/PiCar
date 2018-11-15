"""This program allows for complete control of the PiCar's movement 
and data collection using the keyboard"""
from comms import I2C
import curses
import smbus
import time
import subprocess

i2c = I2C()
# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.start_color()
curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
curses.noecho()
curses.cbreak()
screen.scrollok(True)
#curses.halfdelay(1)
screen.keypad(True)
start_time = 0
flag = True
right_counter = 0
left_counter = 0
command = 0
data_flag = 0
commands = []
times = []
x = 0
first_flag = 1

#

#
elapsed_time = time.time() - start_time
start_time = time.time()

##            if char != ord('d'):
##                right_counter = 0
##
##            if char != ord('a'):
##                left_counter = 0
##
##            if (data_flag == 1 and first_flag == 0):
##                times.append(elapsed_time)
##
##            if (data_flag == 1):
##               first_flag = 0
##
##            if char == ord('q'):
##                i2c.writeNumber(5)
##                screen.addstr(str("{0:.3f}".format(elapsed_time)) + " seconds")
##                break
##
##            elif char == ord('w'):
##                if (data_flag == 1):
##                    commands.append(1)
##                if (command == 0):
##                    screen.addstr("Forward ")
##                i2c.writeNumber(2)

##            elif char == ord('d'):
##                if (data_flag == 1):
##                    commands.append(3)
##                if (data_flag == 1):
##                    commands.append(4)
##                if (left_counter != 3):
##                    left_counter += 1
##                if (left_counter == 1):
##                    if (command == 0):
##                        screen.addstr("Left(1) ")
##                    else:
##                        screen.addstr(str("{0:.3f}".format(elapsed_time)) + " seconds\n" + "Left(1) ")
##                elif (left_counter == 2):
##                    screen.addstr(str("{0:.3f}".format(elapsed_time)) + " seconds\n" + "Left(2) ")
##                elif (left_counter == 3):
##                    screen.addstr(str("{0:.3f}".format(elapsed_time)) + " seconds\n" + "Left(3) ")
##                i2c.writeNumber(4)
##
##            elif char == ord('x'):
##                if flag:
##                    if (command == 0):
##                        screen.addstr("Data Recording Has Started ")
##                    else:
##                        screen.addstr(str("{0:.3f}".format(elapsed_time)) + " seconds\n" + "Data Recording Has Started ")
##                    flag = False
##                    data_flag = 1
##                    commands.clear()
##                    times.clear()
##                else:
##                    screen.addstr(str("{0:.3f}".format(elapsed_time)) + " seconds\n" + "Data Recording Has Stopped ")
##                    for i in commands:
##                        screen.addstr("\n" + str(i))
##                    screen.addstr("\n")
##                    for t in times:
##                        screen.addstr(str(t) + "\n")
##                    flag = True
##                    data_flag = 0
##                    first_flag = 1
##
##            elif char == ord('r'):
##                x = 0
##                screen.addstr(str("{0:.3f}".format(elapsed_time)) + " seconds\n" + "Replaying...\n")
##                screen.refresh()
##                while (x < len(commands)):
##                    i2c.writeNumber(commands[x])
##                    time1 = time.time()
##                    time.sleep(times[x])
##                    time2 = time.time() - time1
##                    screen.addstr(str(time2) + "\n")
##                    x += 1
##                screen.addstr("Replay Complete! ")

##            else:
##                if (data_flag == 1):
##                    commands.append(5)
##                if (command == 0):
##                    screen.addstr("Stop ")
##                else:
##                    screen.addstr(str("{0:.3f}".format(elapsed_time)) + " seconds\n" + "Stop ")
##                i2c.writeNumber(5)      if (right_counter != 3):
##                    right_counter += 1
##                if (right_counter == 1):
##                    if (command == 0):
##                        screen.addstr("Right(1) ")
##                    else:
##                        screen.addstr(str("{0:.3f}".format(elapsed_time)) + " seconds\n" +  "Right(1) ")
##                elif (right_counter == 2):
##                    screen.addstr(str("{0:.3f}".format(elapsed_time)) + " seconds\n" +  "Right(2) ")
##                elif (right_counter == 3):
##                    screen.addstr(str("{0:.3f}".format(elapsed_time)) + " seconds\n" +  "Right(3) ")
##                i2c.writeNumber(3)
##
##            elif char == ord('a'):
##                if (data_flag == 1):
##                    commands.append(4)
##                if (left_counter != 3):
##                    left_counter += 1
##                if (left_counter == 1):
##                    if (command == 0):
##                        screen.addstr("Left(1) ")
##                    else:
##                        screen.addstr(str("{0:.3f}".format(elapsed_time)) + " seconds\n" + "Left(1) ")
##                elif (left_counter == 2):
##                    screen.addstr(str("{0:.3f}".format(elapsed_time)) + " seconds\n" + "Left(2) ")
##                elif (left_counter == 3):
##                    screen.addstr(str("{0:.3f}".format(elapsed_time)) + " seconds\n" + "Left(3) ")
##                i2c.writeNumber(4)
##
##            elif char == ord('x'):
##                if flag:
##                    if (command == 0):
##                        screen.addstr("Data Recording Has Started ")
##                    else:
##                        screen.addstr(str("{0:.3f}".format(elapsed_time)) + " seconds\n" + "Data Recording Has Started ")
##                    flag = False
##                    data_flag = 1
##                    commands.clear()
##                    times.clear()
##                else:
##                    screen.addstr(str("{0:.3f}".format(elapsed_time)) + " seconds\n" + "Data Recording Has Stopped ")
##                    for i in commands:
##                        screen.addstr("\n" + str(i))
##                    screen.addstr("\n")
##                    for t in times:
##                        screen.addstr(str(t) + "\n")
##                    flag = True
##                    data_flag = 0
##                    first_flag = 1

##            elif char == ord('r'):
##                x = 0
##                screen.addstr(str("{0:.3f}".format(elapsed_time)) + " seconds\n" + "Replaying...\n")
##                screen.refresh()
##                while (x < len(commands)):
##                    i2c.writeNumber(commands[x])
##                    time1 = time.time()
##                    time.sleep(times[x])
##                    time2 = time.time() - time1
##                    screen.addstr(str(time2) + "\n")
##                    x += 1
##                screen.addstr("Replay Complete! ")

##            else:
##                if (data_flag == 1):
##                    commands.append(5)
##                if (command == 0):
##                    screen.addstr("Stop ")
##                else:
##                    screen.addstr(str("{0:.3f}".format(elapsed_time)) + " seconds\n" + "Stop ")
##                i2c.writeNumber(5)         else:
##                    screen.addstr(str("{0:.3f}".format(elapsed_time)) + " seconds\n" + "Forward ")
##                i2c.writeNumber(1)
##
##            elif char == ord('s'):
##                if (data_flag == 1):
##                    commands.append(2)
##                if (command == 0):
##                    screen.addstr("Reverse ")
##                else:
##                   screen.addstr(str("{0:.3f}".format(elapsed_time)) + " seconds\n" + "Reverse ")
for x in range(2,5):
    i2c.writeNumber(x)
    time.sleep(5)
    if x ==5:
        break

for x in range(2,5):
    i2c.writeNumber(x)
    time.sleep(5)
    if x ==5:
        break
##
##            elif char == ord('d'):
##                if (data_flag == 1):
##                    commands.append(3)
##                if (data_flag == 1):
##                    commands.append(4)
##                if (left_counter != 3):
##                    left_counter += 1
##                if (left_counter == 1):
##                    if (command == 0):
##                        screen.addstr("Left(1) ")
##                    else:
##                        screen.addstr(str("{0:.3f}".format(elapsed_time)) + " seconds\n" + "Left(1) ")
##                elif (left_counter == 2):
##                    screen.addstr(str("{0:.3f}".format(elapsed_time)) + " seconds\n" + "Left(2) ")
##                elif (left_counter == 3):
##                    screen.addstr(str("{0:.3f}".format(elapsed_time)) + " seconds\n" + "Left(3) ")
##                i2c.writeNumber(4)
##
##            elif char == ord('x'):
##                if flag:
##                    if (command == 0):
##                        screen.addstr("Data Recording Has Started ")
##                    else:
##                        screen.addstr(str("{0:.3f}".format(elapsed_time)) + " seconds\n" + "Data Recording Has Started ")
##                    flag = False
##                    data_flag = 1
##                    commands.clear()
##                    times.clear()
##                else:
##                    screen.addstr(str("{0:.3f}".format(elapsed_time)) + " seconds\n" + "Data Recording Has Stopped ")
##                    for i in commands:
##                        screen.addstr("\n" + str(i))
##                    screen.addstr("\n")
##                    for t in times:
##                        screen.addstr(str(t) + "\n")
##                    flag = True
##                    data_flag = 0
##                    first_flag = 1
##
##            elif char == ord('r'):
##                x = 0
##                screen.addstr(str("{0:.3f}".format(elapsed_time)) + " seconds\n" + "Replaying...\n")
##                screen.refresh()
##                while (x < len(commands)):
##                    i2c.writeNumber(commands[x])
##                    time1 = time.time()
##                    time.sleep(times[x])
##                    time2 = time.time() - time1
##                    screen.addstr(str(time2) + "\n")
##                    x += 1
##                screen.addstr("Replay Complete! ")
##
##            else:
##                if (data_flag == 1):
##                    commands.append(5)
##                if (command == 0):
##                    screen.addstr("Stop ")
##                else:
##                    screen.addstr(str("{0:.3f}".format(elapsed_time)) + " seconds\n" + "Stop ")
##                i2c.writeNumber(5)      if (right_counter != 3):
##                    right_counter += 1
##                if (right_counter == 1):
##                    if (command == 0):
##                        screen.addstr("Right(1) ")
##                    else:
##                        screen.addstr(str("{0:.3f}".format(elapsed_time)) + " seconds\n" +  "Right(1) ")
##                elif (right_counter == 2):
##                    screen.addstr(str("{0:.3f}".format(elapsed_time)) + " seconds\n" +  "Right(2) ")
##                elif (right_counter == 3):
##                    screen.addstr(str("{0:.3f}".format(elapsed_time)) + " seconds\n" +  "Right(3) ")
##                i2c.writeNumber(3)
##
##            elif char == ord('a'):
##                if (data_flag == 1):
##                    commands.append(4)
##                if (left_counter != 3):
##                    left_counter += 1
##                if (left_counter == 1):
##                    if (command == 0):
##                        screen.addstr("Left(1) ")
##                    else:
##                        screen.addstr(str("{0:.3f}".format(elapsed_time)) + " seconds\n" + "Left(1) ")
##                elif (left_counter == 2):
##                    screen.addstr(str("{0:.3f}".format(elapsed_time)) + " seconds\n" + "Left(2) ")
##                elif (left_counter == 3):
##                    screen.addstr(str("{0:.3f}".format(elapsed_time)) + " seconds\n" + "Left(3) ")
##                i2c.writeNumber(4)
##
##            elif char == ord('x'):
##                if flag:
##                    if (command == 0):
##                        screen.addstr("Data Recording Has Started ")
##                    else:
##                        screen.addstr(str("{0:.3f}".format(elapsed_time)) + " seconds\n" + "Data Recording Has Started ")
##                    flag = False
##                    data_flag = 1
##                    commands.clear()
##                    times.clear()
##                else:
##                    screen.addstr(str("{0:.3f}".format(elapsed_time)) + " seconds\n" + "Data Recording Has Stopped ")
##                    for i in commands:
##                        screen.addstr("\n" + str(i))
##                    screen.addstr("\n")
##                    for t in times:
##                        screen.addstr(str(t) + "\n")
##                    flag = True
##                    data_flag = 0
##                    first_flag = 1
##
##            elif char == ord('r'):
##                x = 0
##                screen.addstr(str("{0:.3f}".format(elapsed_time)) + " seconds\n" + "Replaying...\n")
##                screen.refresh()
##                while (x < len(commands)):
##                    i2c.writeNumber(commands[x])
##                    time1 = time.time()
##                    time.sleep(times[x])
##                    time2 = time.time() - time1
##                    screen.addstr(str(time2) + "\n")
##                    x += 1
##                screen.addstr("Replay Complete! ")
##
##            else:
##                if (data_flag == 1):
##                    commands.append(5)
##                if (command == 0):
##                    screen.addstr("Stop ")
##                else:
##                    screen.addstr(str("{0:.3f}".format(elapsed_time)) + " seconds\n" + "Stop ")
##                i2c.writeNumber(5)
##
#command = 1
##finally:
##    #Close down curses properly, inc turn echo back on!
##    curses.nocbreak()
##    screen.keypad(0)
##    curses.echo()
##    curses.endwin()

