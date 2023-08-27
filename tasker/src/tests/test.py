import os
import zipfile
import pyzipper
import concurrent.futures
import re

if __name__ == '__main__':
    outputSrc = "D:\\Python-frame\\UniTasker\\tasker\\src\\temp\\temp.zip"
    normalized_path = os.path.normpath(outputSrc)
    pattern = r"^[a-zA-Z]:\\(?:[\w\s!@#$%^&()-_+={}[\];',.~]+\\)*[\w\s!@#$%^&()-_+={}[\];',.~]+\.?[a-zA-Z]+$"
    print(re.match(pattern, outputSrc) is not None)
    pass
