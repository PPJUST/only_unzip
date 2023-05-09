UZIP软件的解压功能的Python复写，个人学习Python期间的练手程序。

### 实现功能
1. 拖入文件进行解压、拖入文件夹解压其中所有文件
2. 支持测试文件夹密码
3. 基于maigc模块识别压缩包格式
4. 支持一些简单的设置项（解除套娃文件夹、删除原文件）
5. 解压密码计数，密码使用次数多的优先进行测试，加快搜索正确密码的速度。
6. 解压历史记录，包括成功解压与失败

### 制作中的功能
1. 多线程测试密码
2. 解除套娃压缩包

### 实测存在问题
启动占用内存60mb，解压时占用100mb

### 历史记录
2023.05.04 重写GUI版中
2023.05.09 完成GUI版

