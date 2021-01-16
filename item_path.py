import os
'''
目的：通过item_path.py获取整个工程的绝对路径
'''
ABS_PATH = os.path.abspath(__file__)
print(ABS_PATH)
DIR_NAME = os.path.dirname(ABS_PATH)
print(DIR_NAME)