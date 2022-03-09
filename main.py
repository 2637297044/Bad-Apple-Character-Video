import os
import time
import curses
from pathlib import Path

os.system("title Bad Apple 字符画视频程序")

FRAME_RATE = 1 / 30

if Path("video_data.py").exists():
    from video_data import video_data
else:
    input("请先运行 Bad Apple.py 生成视频数据文件！")
        
count = 0

stdsrc = curses.initscr()
curses.start_color()
stdsrc.resize(30, 100)
time.sleep(0.4)
now = time.time()

for frame_data in video_data:
    for i in range(len(frame_data)):
        stdsrc.addstr(i, 0, frame_data[i], curses.COLOR_WHITE)
    while time.time() - now < count * FRAME_RATE:
        time.sleep(max(count * FRAME_RATE - (time.time() - now), 0))
    stdsrc.refresh()
    count += 1

curses.endwin()
