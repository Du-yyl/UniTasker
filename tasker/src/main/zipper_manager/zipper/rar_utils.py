# @Time: 2023/8/27 14:55 35
# @Author: charlatans
# @Name: rar_utils.py
# Path: tasker/src/main/zipper_manager/zipper
# ProjectName: UniTasker
#   Il n'ya qu'un héroïsme au monde :
#       c'est de voir le monde tel qu'il est et de l'aimer.
import os

from unrar.rarfile import RarFile


class rar_utils:
    @staticmethod
    # 解压RAR文件
    def extract_rar(rar_filename, extract_path):
        pass
        # with rarfile.RarFile(rar_filename, 'r') as rf:

    # todo: 能实现加密解压的功能，但是解压目录不能控制；还有将加密和解密进行融合；爆破解密
    # 解密解压加密的RAR文件
    @staticmethod
    def decrypt_and_extract_encrypted_rar(rar_filename, extract_path, pwd):
        rar_file = RarFile(rar_filename, pwd=pwd)
        rar_file.extractall()


if __name__ == '__main__':
    file_path = "D:\\Python-frame\\UniTasker\\tasker\\src\\temp\\test_rar.rar"
    extract_path = "D:\\Python-frame\\UniTasker\\tasker\\src\\temp\\test_rar"
    password = b"anhfree.com"
    pwd = "anhfree.com"
    print(rar_utils.decrypt_and_extract_encrypted_rar(file_path, extract_path, pwd))
    print("")
