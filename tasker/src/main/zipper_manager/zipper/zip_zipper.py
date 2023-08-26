# @Time: 2023/8/26 0:53 53
# @Author: charlatans
# @Name: zip_zipper.py
# Path: tasker/src/main/zipper_manager/zipper
# ProjectName: UniTasker
#   Il n'ya qu'un héroïsme au monde :
#       c'est de voir le monde tel qu'il est et de l'aimer.
import pyzipper


class ZipZipper:
    @staticmethod
    def encrypt_file(input_file, output_file, password):
        with pyzipper.AESZipFile(output_file, 'w', compression=pyzipper.ZIP_DEFLATED,
                                 encryption=pyzipper.WZ_AES) as zipf:
            zipf.setpassword(password)
            zipf.write(input_file)


# D:\Python-frame\UniTasker\tasker\src\temp\新建 文本文档.txt
# D:\Python-frame\UniTasker\tasker\src\temp\demo.zip
# 前缀 b 跟随着单引号或双引号，可以用来创建字节字符串（bytes）。字节字符串是一种表示原始二进制数据的方式，特别在处理文件、加密等情况下非常有用。
if __name__ == '__main__':
    inputSrc = "D:\\Python-frame\\UniTasker\\tasker\\src\\temp\\新建 文本文档.txt"
    outputSrc = "D:\\Python-frame\\UniTasker\\tasker\\src\\temp\\demo.zip"

    ZipZipper.encrypt_file(inputSrc, outputSrc, b'')
    print("")
