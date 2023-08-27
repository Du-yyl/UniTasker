# @Time: 2023/8/27 14:55 35
# @Author: charlatans
# @Name: rar_utils.py
# Path: tasker/src/main/zipper_manager/zipper
# ProjectName: UniTasker
#   Il n'ya qu'un héroïsme au monde :
#       c'est de voir le monde tel qu'il est et de l'aimer.
import rarfile


class rar_utils:
    @staticmethod
    # 解压RAR文件
    def extract_rar(rar_filename, extract_path):
        with rarfile.RarFile("archive.rar") as rf:
            with rf.open("README") as f:
                for ln in f:
                    print(ln.strip())

    # 解密解压加密的RAR文件
    # todo:这里的内容还有问题，需要修改
    @staticmethod
    def decrypt_and_extract_encrypted_rar(rar_filename, extract_path, pwd):
        with rarfile.RarFile(rar_filename, 'r') as rf:
            need_password = rf.needs_password()
            if need_password:
                try:
                    print("开始解压...")
                    rf.extractall(path=extract_path, pwd=pwd)
                    print("解压完成")
                    return True, "解压成功"
                except rarfile.RarWrongPassword:
                    return False, "密码错误"
                except Exception as e:
                    print("解压异常:", e)
                    return False, str(e)
            else:
                return False, "不需要密码"
            # rf.extractall(extract_path)


if __name__ == '__main__':
    file_path = "D:\\Python-frame\\UniTasker\\tasker\\src\\temp\\test_rar.rar"
    extract_path = "D:\\Python-frame\\UniTasker\\tasker\\src\\temp\\test_rar"
    password = b"anhfree.com"
    pwd = "anhfree.com"
    print(rar_utils.decrypt_and_extract_encrypted_rar(file_path, extract_path, pwd))
    print("")
