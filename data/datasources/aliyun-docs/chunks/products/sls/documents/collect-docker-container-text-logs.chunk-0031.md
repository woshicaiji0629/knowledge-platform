### 错误日志：The parameter is invalid : uuid=none
问题描述：如果LoongCollector（Logtail）日志（/usr/local/ilogtail/ilogtail.LOG）中出现The parameter is invalid : uuid=none的错误日志。
解决方案：请在宿主机上创建一个product_uuid文件，在其中输入任意合法UUID（例如169E98C9-ABC0-4A92-B1D2-AA6239C0D261），并把该文件挂载到LoongCollector（Logtail）容器的/sys/class/dmi/id/product_uuid目录。
