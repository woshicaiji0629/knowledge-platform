## 步骤三：创建Logtail采集配置
使用阿里云账号A登录[日志服务控制台](https://sls.console.aliyun.com)。
在数据接入区域，单击Kubernetes-文件。
选择目标Project和LogStore，单击下一步。
单击使用现有机器组。
选中您在[步骤二：创建机器组](use-logtail-to-collect-container-logs-across-accounts.md)中所创建的机器组，将该机器组从源机器组移动到应用机器组，单击下一步。
设置Logtail采集配置，单击下一步。
具体参数说明，请参见[通过](use-the-log-service-console-to-collect-container-text-logs-in-daemonset-mode.md)[DaemonSet-控制台方式采集容器文本日志](use-the-log-service-console-to-collect-container-text-logs-in-daemonset-mode.md)。
重要
默认一个文件只能匹配一个Logtail采集配置。此时账号B下的采集未停止，账号A下的Logtail采集配置无法生效，因此您需要使用如下方式使账号A下的Logtail采集配置生效。
停止账号B下的采集，即使用账号B登录日志服务控制台，从目标机器组中移除Logtail采集配置。具体操作，请参见[应用](manage-machine-groups.md)[Logtail](manage-machine-groups.md)[采集配置到指定机器组](manage-machine-groups.md)。
在账号A下添加强制采集配置。更多信息，请参见[如何实现文件中的日志被采集多份](what-do-i-do-if-i-want-to-use-multiple-logtail-configurations-to-collect-logs-from-a-log-file.md)。
此处创建Logtail采集配置成功后，请删除阿里云账号B下的原有Logtail采集配置，避免重复采集日志。如何删除，请参见[删除](manage-logtail-configurations-for-log-collection.md)[Logtail](manage-logtail-configurations-for-log-collection.md)[采集配置](manage-logtail-configurations-for-log-collection.md)。
预览数据及设置索引，单击下一步。
日志服务默认开启全文索引。您也可以根据采集到的日志，手动或者自动设置字段索引。更多信息，请参见[创建索引](create-indexes.md)。
