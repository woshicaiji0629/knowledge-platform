### 如何获取服务器的IP地址，作为机器组标识？
在已安装LoongCollector（Logtail）的服务器上，打开/usr/local/ilogtail/app_info.json文件，查看ip值。
Logtail自动获取的服务器IP地址记录在app_info.json文件的ip字段中，如下所示。
重要
存在多台服务器时，请手动输入对应的IP地址，IP地址之间需使用换行符分隔。
同一机器组中不允许同时存在Linux和Windows服务器。请勿将Windows和Linux服务器IP添加到同一机器组中。
