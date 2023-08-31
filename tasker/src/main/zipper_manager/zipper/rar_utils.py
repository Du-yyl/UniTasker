# @Time: 2023/8/27 14:55 35
# @Author: charlatans
# @Name: rar_utils.py
# Path: tasker/src/main/zipper_manager/zipper
# ProjectName: UniTasker
#   Il n'ya qu'un héroïsme au monde :
#       c'est de voir le monde tel qu'il est et de l'aimer.
import os
import shutil

from unrar import unrarlib, constants
from unrar.rarfile import RarFile, BadRarFile, RarInfo

# 临时路径
temp_path = "D:\\____temp"


class rar_utils:

    @staticmethod
    # 解压RAR文件
    def extract_rar(rar_filename, extract_path):
        pass
        # with rarfile.RarFile(rar_filename, 'r') as rf:

    # 解密解压加密的RAR文件
    @staticmethod
    def decrypt_file(rar_filename, extract_path, pwd):
        """
        解压文件
        :param rar_filename: 文件路径
        :param extract_path: 要解压到的目录
        :param pwd: 密码
        """
        rar_file = RarFile(rar_filename, pwd=pwd)
        rar_file.extractall(path=extract_path)

    @staticmethod
    def test_password(rar_filename, password):
        """
        测试输入的密码是否正确，如果正确将返回 true，反之为 false
        原理：根据密码解压第一个文件，如果成功则确认密码为正确
        注意：如果一个文件没有秘钥，那么传递秘钥时也将会返回 True 所以应该先测试 None 然后再进行其他密码的测试
        :param rar_filename: 要解压的文件路径
        :param password: 密码
        :return: 密码的测试结果
        """
        permission = 0o755  # 修改为您希望设置的权限值

        if password == "":
            password = None

        if os.path.exists(temp_path):
            os.chmod(temp_path, permission)  # 更改文件夹权限
            try:
                shutil.rmtree(temp_path)  # 删除整个文件夹及其内容
            except Exception as e:
                print(f"删除文件夹时出错：{e}")

        # 创建对应文件夹
        os.mkdir(temp_path)
        os.chmod(temp_path, permission)  # 更改文件夹权限

        try:
            with RarFile(rar_filename, "r", pwd=password) as rar:
                file_to_extract = rar.namelist()[0]  # 获取第一个文件成员的名称
                rar.extract(file_to_extract, temp_path)
                shutil.rmtree(temp_path)
        except BadRarFile:
            print("密码错误")
            return False
        except unrarlib.MissingPassword:
            return False
        except unrarlib.BadPassword:
            return False
        except unrarlib.BadDataError:
            return False
        except unrarlib.UnrarException as e:
            return False
        except RuntimeError:
            return False

        return True

    @staticmethod
    def blow_up_password(file_path, passwords):
        """
        爆破密码
        :param file_path: 文件路径
        :param passwords: 要测试的密码数组
        :return: 如果存在密码返回密码，反之返回异常
        """
        passwords.append(None)
        for password in passwords:
            if rar_utils.test_password(file_path, password):
                return password

        return "无匹配密码"

    # todo:该方法存在问题，无法进行批量破解
    @staticmethod
    def blow_up_decrypt(file_path, passwords):
        """
        爆破解压
        :param file_path: 文件路径
        :param passwords: 密码列表
        """
        passwords.append(None)
        for password in passwords:
            try:
                rar_utils.decrypt_file(file_path, None, password)
            except RuntimeError:
                print(password+"密码错误")

        return "无匹配密码"


if __name__ == '__main__':
    file_path = "D:\\Python-frame\\UniTasker\\tasker\\src\\temp\\test_rar.rar"
    extract_path = "D:\\Python-frame\\UniTasker\\tasker\\src\\temp\\test_rar"
    pwd = "anhfree.com"
    print(rar_utils.decrypt_file(file_path, extract_path, pwd))
    # print(rar_utils.blow_up_decrypt(file_path, pwd))
