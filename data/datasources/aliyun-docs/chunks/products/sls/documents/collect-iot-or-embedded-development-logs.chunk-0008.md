## 性能测试
环境配置
高性能场景：传统X86服务器。
低性能场景：树莓派（低功耗环境）。
配置如下：
C Producer配置
ARM（树莓派）
缓存：10 MB
聚合时间：3秒（聚合时间、聚合数据包大小、聚合日志数任一满足即打包发送）
聚合数据包大小：1 MB
聚合日志数：1000
发送线程：1
自定义tag：5
X86
缓存：10MB
聚合时间：3秒（聚合时间、聚合数据包大小、聚合日志数任一满足即打包发送）
聚合数据包大小：3 MB
聚合日志数：4096
发送线程：4
自定义tag：5
日志样例（9个键值对，数据量约为350字节）
__source__: 192.0.2.1 __tag__:1: 2 __tag__:5: 6 __tag__:a: b __tag__:c: d __tag__:tag_key: tag_value __topic__: topic_test _file_: /disk1/workspace/tools/aliyun-log-c-sdk/sample/log_producer_sample.c _function_: log_producer_post_logs _level_: LOG_PRODUCER_LEVEL_WARN _line_: 248 _thread_: 40978304 LogHub: Real-time log collection and consumption Search/Analytics: Query and real-time analysis Interconnection: Grafana and JDBC/SQL92 Visualized: dashboard and report functions
测试结果
X86平台结果
C Producer可以轻松到达90 MB/s的发送速度，每秒上传日志20万，占用CPU只有70%，内存140 MB。
服务器在200条/s，发送数据对于CPU基本无影响（降低到0.01%以内）。
客户线程发送一条数据（输出一条日志）的平均耗时为1.2 us。
树莓派平台结果
在树莓派的测试中，由于CPU的频率只有600 MHz，性能差不多是服务器的1/10左右，每秒可发送最多2万条日志。
树莓派在20条/s的时候，发送数据对于CPU基本无影响（降低到0.01%以内）。
客户线程发送一条数据（输出一条日志）的平均耗时为：12 us左右（树莓派通过USB连接到PC共享网络）。
更多日志服务典型场景可以参见[云栖论坛](https://yq.aliyun.com/teams/4/type_blog-cid_8?spm=a2c4g.11186623.2.35.2dfc505eazEyHL)。
该文章对您有帮助吗？
反馈
