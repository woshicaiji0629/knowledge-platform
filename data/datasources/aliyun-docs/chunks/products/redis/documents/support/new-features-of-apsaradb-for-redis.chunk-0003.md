### 新特性
关于Redis7.0的新特性请参见[7.0 release note](https://raw.githubusercontent.com/redis/redis/7.0/00-RELEASENOTES)。
例如对于使用Background线程的module命令，慢日志功能会记录整个挂起的时间；对于普通的Block类命令（例如BLPOP），慢日志功能只会记录执行时间，不记录挂起时间。
