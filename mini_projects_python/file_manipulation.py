import os
import shutil


class FileManipulator:
    def __init__(self):
        pass

    def read(self, file_address, type):
        lines = ''
        if type == 'line':
            lines = []
            file = open(file_address, 'r')
            while True:
                line = file.readline()
                lines.append(line)

                if not line:
                    file.close()
                    break
        elif type == 'total':
            file = open(file_address, 'r')
            lines = file.readlines()
            file.close()
        else:
            print('choose correct type of reading mode')
        content = ''.join(lines)
        return content

    def write(self, file_address, content, mode='a+'):
        file = open(file_address, mode)
        file.write(content)
        file.close()

    def copy(self, address1, address2):
        content = self.read(address1, 'total')
        self.write(address2, content, 'a+')

    def make_folder(self, folder_address):
        os.makedirs(folder_address)

    def remove(self, address_list):
        for item in address_list:
            if os.path.isfile(item):
                os.remove(item)
            elif os.path.isdir(item):
                shutil.rmtree(item)

    def existence(self, file_address):
        if os.path.exists(file_address):
            print('I find it :)')
        else:
            print('Where is it?')


if __name__ == "__main__":
    obj = FileManipulator()
    # result = obj.read('sample.txt', 'line')
    # print(result)
    # obj.remove(['folder1', 'folder2', 'test.txt'])
    # obj.existence('sample.txt')
    # obj.copy('sample.txt', 'copy.txt')
    # obj.make_folder('my_folder')
    obj.remove(['my_folder', 'copy.txt'])
