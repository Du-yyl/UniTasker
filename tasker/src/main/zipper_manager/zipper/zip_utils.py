# @Time: 2023/8/26 0:53 53
# @Author: charlatans
# @Name: zip_utils.py
# Path: tasker/src/main/zipper_manager/zipper
# ProjectName: UniTasker
#   Il n'ya qu'un héroïsme au monde :
#       c'est de voir le monde tel qu'il est et de l'aimer.
import concurrent
import concurrent.futures
import os
import zipfile

import pyzipper

from src.main.time_utils import TimeUtils


class zip_utils:
    @staticmethod
    def zip_file(input_data,output_file,compression_level=zipfile.ZIP_DEFLATED):
        # 输入内容不为空
        # 输入内容为数组 且长度不为0

        # 如果长度为 1
            # 按照文件夹或文件进行处理 w
        # 如果长度更长
            # 如果更长使用追加方式 a
        pass


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
    def zip_single_file(input_file, output_zip, compression_level=zipfile.ZIP_DEFLATED):
        """
        压缩当个文件
        """
        with zipfile.ZipFile(output_zip, 'w', compression=compression_level) as zipf:
            file_name = os.path.basename(input_file)
            zipf.write(input_file, arcname=file_name)

    @staticmethod
    def zip_single_folder(input_folder, output_zip, compression_level=zipfile.ZIP_DEFLATED):
        """
        压缩文件夹
        """
        # 如果文件夹存在
        if os.path.exists(input_folder) is False:
            print("指定文件不存在")
            return False

        # 使用os.path模块的normpath函数来规范化路径
        normalized_path = os.path.normpath(output_zip)
        # 使用os.path模块的isabs函数判断是否是绝对路径
        if os.path.isfile(normalized_path) is False:
            print("输出路径错误")
            return False

        with zipfile.ZipFile(output_zip, 'w', compression=compression_level) as zipf:
            for root, _, files in os.walk(input_folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, input_folder)
                    zipf.write(file_path, arcname=arcname)
        return True

    @staticmethod
    def zip_multiple_files(input_files, output_zip, compression_level=zipfile.ZIP_DEFLATED):
        """
        压缩多个文件
        """
        with zipfile.ZipFile(output_zip, 'w', compression=compression_level) as zipf:
            for input_file in input_files:
                file_name = os.path.basename(input_file)
                zipf.write(input_file, arcname=file_name)


# D:\Python-frame\UniTasker\tasker\src\temp\新建 文本文档.txt
# D:\Python-frame\UniTasker\tasker\src\temp\demo.zip
# 前缀 b 跟随着单引号或双引号，可以用来创建字节字符串（bytes）。字节字符串是一种表示原始二进制数据的方式，特别在处理文件、加密等情况下非常有用。
if __name__ == '__main__':
    folderArr = [
        "D:\\Python-frame\\UniTasker\\tasker\\src\\temp",
        "E:\\新建文件夹\\(XIUREN) - 鱼子酱Fish - Student girl after school"
    ]
    outputSrc = "D:\\Python-frame\\UniTasker\\tasker\\src\\temp\\temp.zip"

    print("开始")
    startTime = TimeUtils.get_timestamp(True)
    zip_utils.zip_multiple_files(folderArr, outputSrc)

    endTime = TimeUtils.get_timestamp(True)
    print(TimeUtils.time_difference(startTime, endTime))
