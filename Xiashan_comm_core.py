# -*- coding: utf-8 -*-
import subprocess
from tqdm import tqdm
import sys
import time
import codecs

sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer, 'strict')
sys.stderr = codecs.getwriter('utf8')(sys.stderr.buffer, 'strict')


class XiaShanMessageCore:
    def __init__(self):
        # 显示启动进度条
        for i in tqdm(range(100), desc="Initializing XiaShan Core"):
            time.sleep(0.01)  # 模拟启动过程中的延迟

        # 启动“青龙湖”终端
            import Azure_Dragon_Smart_Terminal

        print("Successful boot the 'Azure Dragon Lake Terminal'")

    # 使用示例：创建XiaShanMessageCore实例


if __name__ == "__main__":
    core = XiaShanMessageCore()