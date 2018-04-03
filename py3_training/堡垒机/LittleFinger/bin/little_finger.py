#_*_coding:utf-8_*_
__author__ = 'Alex Li'
import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print(BASE_DIR)
sys.path.append(BASE_DIR) #将当前父目录加入到系统路径下

if __name__ == '__main__':
    from modules.actions import excute_from_command_line #  从 modules.actions 导入 excute_from_command_line
    excute_from_command_line(sys.argv) #传递命令行启动的参数并且执行这个函数
