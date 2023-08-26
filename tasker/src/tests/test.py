import os
import zipfile
import pyzipper
import concurrent.futures


class FileZipper:
    @staticmethod
    def zip_item(input_item, output_zip):
        with pyzipper.AESZipFile(output_zip, 'w', compression=pyzipper.ZIP_DEFLATED) as zipf:

            if os.path.isfile(input_item):
                arcname = os.path.basename(input_item)
                zipf.write(input_item, arcname=arcname)
            elif os.path.isdir(input_item):
                for root, _, files in os.walk(input_item):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, input_item)
                        zipf.write(file_path, arcname=arcname)

    @staticmethod
    def zip(input_data, output_zip, compression_level=zipfile.ZIP_DEFLATED, password=None, num_threads=2):
        if password:
            password = password.encode('utf-8')

        if isinstance(input_data, str):
            input_data = [input_data]

        with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = []
            for item in input_data:
                future = executor.submit(FileZipper.zip_item, item, output_zip, compression_level, password)
                futures.append(future)

            for future in concurrent.futures.as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    print(f"An error occurred: {e}")


if __name__ == '__main__':
    input_folder = "D:\\Python-frame\\UniTasker\\tasker\\src\\temp"
    input_file = "your_input_file.txt"
    input_files = ["file1.txt", "file2.txt", "file3.txt"]
    input_folders = ["folder1", "folder2"]
    output_zip = "D:\\Python-frame\\UniTasker\\tasker\\src\\temp\\temp.zip"
    password = "132"
    num_threads = 3

    FileZipper.zip_item(input_folder, output_zip)
    print("结束")

