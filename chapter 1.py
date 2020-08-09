# Magic Method
from os.path import join
class FileObject:
  ''''给文件对象进行包装从而确认在删除时文件流关闭'''
  def __init__(self,filepath = './',filename='sameple.txt'):
    # 读写模式打开一个文件
    self.file = open(join(filepath,filename),'r+')
  def __del__(self):
    self.file.close()
    del  self.file