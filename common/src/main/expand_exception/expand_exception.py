# @Time: 2023/8/27 12:49 08
# @Author: charlatans
# @Name: expand_exception.py
# Path: common/src/main/expand_exception
# ProjectName: UniTasker
#   Il n'ya qu'un héroïsme au monde :
#       c'est de voir le monde tel qu'il est et de l'aimer.
from enum import Enum


class ExpandException(Exception):
    def __init__(self, error_code, message):
        self.error_code = error_code
        self.message = message
        super().__init__(self.message)


class UtilsException(Enum):
    pass


if __name__ == "__main__":
    pass
