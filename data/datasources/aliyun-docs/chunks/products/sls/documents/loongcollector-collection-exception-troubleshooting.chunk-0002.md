### 数据重复采集
内存使用率极高，一直在崩溃。崩溃会重新从checkpoint检查点采集导致数据重复，请[修改](loongcollector-management-linux.md)[CPU](loongcollector-management-linux.md)[使用上限或网络发送并发限制](loongcollector-management-linux.md)。
文件用编辑器编辑过（如使用vim编辑保存）：查看文件创建时间，确认被采集文件是否发生重写。
#方法一：看birth time stat your_file #方法二：有时候方法一不管用，看crtime stat -c %i your_file df . #查询分区 sudo debugfs -R 'stat <3014895>' /dev/sda3 #替换<>中间的inode（<>要保留），替换sda3为上一行命令分区所在dev
检查是否存在多个采集器实例。
日志量极小的情况下（15分钟以上无新日志）：采集进度可能被清理，造成重复采集。
检查是否采集配置重复：stdout由于允许重复采集，尤其需要注意。
[控制台通过诊断信息排查采集错误](loongcollector-collection-exception-troubleshooting.md)：存在MULTI_CONFIG_MATCH_ALARM错误。
删除多余采集配置：重复采集配置采集同一个目录时，采集路径最精确的优先级最高。
修改相关配置：[实现一个文件中的日志被采集多份](what-do-i-do-if-i-want-to-use-multiple-logtail-configurations-to-collect-logs-from-a-log-file.md)。
采集日志路径总会在多个路径变化，删除采集配置会立刻重建：
排查目录是否存在软连接导致重复采集。
排查是否由env创建或ack中配置了日志标签，配置了需要删掉。
Pod容器重启，且使用hostpath挂载，导致重复采集。
采集容器日志的原理是通过类似docker ps的方法探测容器，通过类似docker inspect的方法找到采集路径。当匹配采集配置时，采集器会向主程序报送一条采集路径+配置。当容器重启时，采集器会认为是创建新容器，并再次向主程序报送一条采集路径+配置。此时，由于业务pod日志路径挂载的是hostPath，因此前一个容器持久化的日志会被保留下来，采集器默认往回读取1M日志导致日志重复。
容器内日志发生采集重复，并且采集路径含NAS。
如果创建reader的时间点因为（NAS）目录注册慢没有赶上dump checkpoint的时间点，那么进度都会丢失。add a new watcher持续时间过长也是一个特征，解决方法是把check_point_dum
