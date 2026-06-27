## Upstart Job
说明
如需使用Upstart Job，您需要为实例安装upstart服务，支持采用upstart服务管理启动行为的操作系统有CentOS 6、Ubuntu 10/12/14以及Debian 6/7。
简介
Upstart是一个事件驱动型的初始化系统，Upstart Job是一个配置文件，定义了一个服务或任务何时启动、停止和如何运行。它通常放置在/etc/init/目录下，文件扩展名为.conf。
运行频率
启动实例：实例每次启动都会自动运行。
更换操作系统：自动运行。
重新初始化系统盘：自动运行。
重要
以下情况不会自动运行脚本：
如果更换操作系统使用的是自定义镜像且来源于原实例，更换操作系统时会判断实例不是初次启动，因此不会自动运行脚本。
如果创建使用的是自定义镜像，则创建实例时系统盘就有数据，初始化系统盘时会判断实例不是首次启动，因此不会自动运行脚本。
格式
首行为#upstart-job，且起始位置不能有空格。
Upstart Job内容示例
#upstart-job description "upstart test" start on runlevel [2345] #在运行级别2、3、4、5执行 stop on runlevel [!2345] #在运行级别2、3、4、5以外不执行 exec echo "Hello World. The time is now $(date -R)!" | tee /root/output.txt
示例Upstart Job表示在系统进入指定的运行级别时输出一条包含时间戳的消息，并将该消息记录到/root/output.txt文件中。当系统离开这些运行级别时，作业会停止执行。
