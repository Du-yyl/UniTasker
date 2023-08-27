# @Time: 2023/8/26 0:53 53
# @Author: charlatans
# @Name: zip_utils.py
# Path: tasker/src/main/zipper_manager/zipper
# ProjectName: UniTasker
#   Il n'ya qu'un héroïsme au monde :
#       c'est de voir le monde tel qu'il est et de l'aimer.
import concurrent
import concurrent.futures
import contextlib
import os
import zipfile

import pyzipper

from src.main.file_utils import FileUtils
from src.main.time_utils import TimeUtils


class zip_utils:
    @staticmethod
    def encrypt_zip_file(input_file, output_file, password):
        """
        压缩加密文件
        :param input_file: 输入文件路径
        :param output_file: 加密后的文件路径
        :param password: 密码
        """
        with pyzipper.AESZipFile(
                output_file,
                'w',
                compression=pyzipper.ZIP_DEFLATED,
                encryption=pyzipper.WZ_AES) as zipf:
            # 获取要压缩的文件名（不包括路径）
            file_name = os.path.basename(input_file)
            zipf.setpassword(password)
            # 将文件添加到压缩文件中，使用 file_name 作为在压缩文件中的文件名
            zipf.write(input_file, arcname=file_name)

    @staticmethod
    def zipper(input_data, output_zip, compression_level=zipfile.ZIP_DEFLATED):
        """
        压缩文件或文件夹到指定的ZIP文件中。

        :param input_data: 待压缩的文件或文件夹列表。
        :param output_zip: 输出的ZIP文件路径。
        :param compression_level: 压缩级别。
        :return: 压缩操作是否成功，成功返回 (True, "文件压缩成功")，否则返回 (False, 错误消息)。
        """
        # 如果为 None
        if input_data is None:
            return False, "压缩目录为 None"
        # 如果长度为 0
        if len(input_data) == 0:
            return False, "压缩目录长度为 0"
        # 是否是一个文件
        if FileUtils.is_valid_path(output_zip) is False:
            return False, "输出路径错误"

        normalized_path = os.path.normpath(output_zip)
        # 文件是否存在
        if os.path.exists(normalized_path):
            with contextlib.suppress(FileNotFoundError):
                os.remove(normalized_path)
        # 压缩文件
        with pyzipper.AESZipFile(output_zip, 'w', compression=compression_level) as zipf:
            # 拿出内容进行压缩
            for item in input_data:
                normalized_item_path = os.path.normpath(item)
                # 文件压缩
                if os.path.isfile(normalized_item_path):
                    file_name = os.path.basename(item)
                    zipf.write(item, arcname=file_name)
                # 文件夹压缩
                if os.path.isdir(normalized_item_path):
                    for root, _, files in os.walk(item):
                        # 获取文件夹名称
                        for file in files:
                            file_path = os.path.join(root, file)
                            arcname = os.path.relpath(file_path, item)
                            zipf.write(file_path, arcname=arcname)
        return True, "文件压缩成功"


# D:\Python-frame\UniTasker\tasker\src\temp\新建 文本文档.txt
# D:\Python-frame\UniTasker\tasker\src\temp\demo.zip
# 前缀 b 跟随着单引号或双引号，可以用来创建字节字符串（bytes）。字节字符串是一种表示原始二进制数据的方式，特别在处理文件、加密等情况下非常有用。
if __name__ == '__main__':
    folderArr = [
        "D:\\Python-frame\\UniTasker\\tasker\\src\\temp\\temp",
    ]
    outputSrc = "D:\\Python-frame\\UniTasker\\tasker\\src\\temp\\temp.zip"

    print("开始")
    startTime = TimeUtils.get_timestamp()
    print(zip_utils.zipper(folderArr, outputSrc))
    # zip_utils.zip_single_folder("D:\\Python-frame\\UniTasker\\tasker\\src\\temp\\temp","D:\\Python-frame\\UniTasker\\tasker\\src\\temp\\temp2.zip")

    endTime = TimeUtils.get_timestamp()
    print(TimeUtils.time_difference(startTime, endTime))
