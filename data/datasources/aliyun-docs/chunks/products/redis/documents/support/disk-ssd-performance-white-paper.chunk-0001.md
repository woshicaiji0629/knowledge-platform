## 测试工具
采用开源社区的YCSB压测工具进行压测。YCSB是一款Java编写的支持多种数据库的性能测试工具，具体安装和使用方法请参见[YCSB](https://github.com/brianfrankcooper/YCSB/tree/master/redis)。
本测试中，对YCSB的相关内容做了一定的修改，使其支持导入long类型的recordcount参数、支持测试Redis的String相关命令，修改后的完整源代码请参见[YCSB](https://docs-aliyun.cn-hangzhou.oss.aliyun-inc.com/assets/attach/120287/cn_zh/1601176553772/YCSB.tar.gz)[源码](https://docs-aliyun.cn-hangzhou.oss.aliyun-inc.com/assets/attach/120287/cn_zh/1601176553772/YCSB.tar.gz)。
