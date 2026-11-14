"""演示导入以数字开头的同目录模块，并调用其中的函数。"""

import importlib


# 模块名以数字开头，使用字符串动态导入，名称中不包含 .py。
function_module = importlib.import_module("06_function")

if __name__ == '__main__':
    # 导入时不会执行原文件主入口中的三次调用，这里主动调用一次。
    function_module.welcome()
