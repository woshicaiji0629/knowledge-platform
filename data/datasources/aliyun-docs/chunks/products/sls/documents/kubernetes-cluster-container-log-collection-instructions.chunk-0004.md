### 日志源与挂载点要求（重要）
对于标准输出类型的日志，LoongCollector会根据容器元信息自动识别获取文件所在路径。
对于容器文本文件类型的日志，LoongCollector默认将宿主机根目录挂载到自身的/logtail_host目录下，一般来说无须再手动挂载。如果需要自定义挂载点需满足：
自定义挂载点要求
日志文件路径：
禁止使用软链接：
错误配置：/var/log -> /mnt/logs。
正确配置：直接使用物理路径/mnt/logs。
挂载路径匹配规则：若业务容器的数据目录通过数据卷（Volume）挂载，采集路径必须≥挂载点路径。
1挂载点：/var/log/service 2✅ 有效采集路径：/var/log/service 或 /var/log/service/subdir 3❌ 无效采集路径：/var/log （路径过短）
不建议使用共享网络存储介质，如NAS、OSS等，否则可能导致数据截断，内容不一致或采集停止，建议使用EBS。
