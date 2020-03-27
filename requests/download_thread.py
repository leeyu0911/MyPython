from threading import Thread
import requests as r

# 一個下載任務 一個線程
class Download_Hanlder(Thread):
    def __init__(self, url, filepath='/Users/leeyu/Downloads/'):
        super().__init__()
        self.url = url
        self.filepath = filepath

    def run(self):
        filename = self.url[self.url.rfind('/') + 1:]  # 檔名為從最後一個斜線到後面
        file = r.get(self.url)
        with open(self.filepath + filename, 'wb') as f:
            f.write(file.content)

url = ''
Download_Hanlder(url).start()
