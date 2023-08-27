# @Time: 2023/8/27 13:36 13
# @Author: charlatans
# @Name: file_utils.py
# Path: common/src/main
# ProjectName: UniTasker
#   Il n'ya qu'un héroïsme au monde :
#       c'est de voir le monde tel qu'il est et de l'aimer.
import os
import re


class FileUtils:
    @staticmethod
    def is_valid_path(path):
        """
        文件路径是否有效
        """
        normalized_path = os.path.normpath(path)
        # 正则表达式检测
        # pattern = r"^[a-zA-Z]:\\(?:[\w\s!@#$%^&()-_+={}[\];',.~]+\\)*[\w\s!@#$%^&()-_+={}[\];',.~]+\.?[a-zA-Z]+$"
        # return re.match(pattern, normalized_path) is not None
        # 通过绝对路径检测
        return os.path.isabs(normalized_path)


if __name__ == '__main__':
    print("")
