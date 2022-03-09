from pathlib import Path
import convert

VIDEO_PATH = "data/1.flv"
BGM_PATH = "data/bgm.mp3"

FRAME_RATE = 1 / 30

if Path("video_data.py").exists():
    print("不需要再转换一次！")
else:
    if not Path(VIDEO_PATH).exists():
        print("视频不存在: ", VIDEO_PATH)
    convert.write(VIDEO_PATH)
    input("\n请输入任意键继续")
