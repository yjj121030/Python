from urllib.request import Request,urlopen
import threading
import time

class DownUtil:
    def __init__(self,path,target_file,thread_num):
        #定义下载资源的路径
        self.path = path
        # 定义需要使用多少个线程下载资源
        self.thread_num = thread_num
        # 指定下载的文件的保存位置
        self.target_file = target_file
        # 初始化threads数组
        self.threads = []
    def download(self):
        # 创建Request对象
        req = Request(url=self.path,method='GET')
        # # 添加请求头
        # req.add_header('Accept','*/*')
        # req.add_header('Charset','UTF-8')
        # req.add_header('Connection','Keep-Alive')
        # 打开要下载的资源
        f = urlopen(req)
        # 获取要下载的文件大小
        self.file_size = int(dict(f.headers).get('Content-Length',0))
        f.close()
        # 计算每个线程要下载的资源大小
        current_part_size = self.file_size//self.thread_num+1
        for i in range(self.thread_num):
            # 计算每个线程下载的开始位置
            start_pos = i * current_part_size
            # 每个线程都是用一个以wb模式打开的文件进行下载
            t = open(self.target_file,'wb')
            # 定位该线程的下载位置
            t.seek(start_pos,0)
            # 创建下载线程
            td = DownThread(self.path,start_pos,current_part_size,t)
            self.threads.append(td)
            td.start()
    # 获取下载完成的百分比
    def get_complete_rate(self):
        # 统计多个线程已经下载的资源总大小
        sum_size = 0
        for i in range(self.thread_num):
            sum_size+=self.threads[i].length
        # f返回已经完成的百分比
        return sum_size/self.file_size
class DownThread(threading.Thread):
    def __init__(self,path,start_pos,current_part_size,current_part):
        super().__init__()
        self.path = path
        # 当前线程的下载位置
        self.start_pos = start_pos
        # 定义当前线程负责下载的文件大小
        self.current_part_size = current_part_size
        # 当前线程需要下载的文件块
        self.current_part = current_part
        # 定义当前线程已经下载的字节数
        self.length = 0
    def run(self):
        # 创建Request对象
        req = Request(url=self.path,method='GET')
        # # 添加请求头
        req.add_header('Accept','*/*')
        req.add_header('Charset','UTF-8')
        req.add_header('Connection','Keep-Alive')
        # 打开要下载的资源
        f = urlopen(req)
        # 跳过self.start_pos个字节，表明该线程只下载自己负责的那部分内容
        f.read(self.start_pos)
        # 读取网络数据，并写入本地文件中
        while self.length<self.current_part_size:
            data = f.read(1024)
            if data is None or len(data)<=0:
                break
            self.current_part.write(data)
            # 累计该线程下载的资源总大小
            self.length+=len(data)
        self.current_part.close()
du = DownUtil("http://www.crazyit.org/data/attachment/forum/201907/06/093559ia613o5ch3z3eb6c.png",'a.png',1)
du.download()