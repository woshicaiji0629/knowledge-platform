[日志服务控制台](https://sls.console.aliyun.com)，在Project列表，单击打开目标Project。
左侧导航栏中，选择资源>机器组。在打开的机器组页面中，选择机器组右侧的>创建机器组。登录日志服务控制台，在机器组页面单击创建机器组。
在弹出的创建机器组页面，填写以下信息，并单击确定。

| 参数 | 说明 |
| --- | --- |
| 名称 | 机器组 名称，命名规则如下所示： 只能包括小写字母、数字、短划线（-）和下划线（_）。 必须以小写字母或者数字开头和结尾。 长度必须在 2~128 字符之间。 重要 创建后，不支持修改机器组名称，请谨慎填写。 |
| 机器组标识 | 选择 IP 地址 。 |
| 机器组 Topic | （可选） 机器组 Topic 用于区分不同服务器产生的日志数据。 |
| IP 地址 | 填入 Logtail 自动获取的服务器 IP： 在已安装 Logtail 的服务器，打开 app_info.json 文件，并查看 ip 字段的值。 app_info.json 文件路径说明 Logtail 自动获取的服务器 IP 地址记录在 app_info.json 文件的 ip 字段中。 [root@iZ2zexxx ]# cat /usr/local/ilogtail/app_info.json { "UUID" : "Cxxx", "compiler" : "GCC 9.3.1", "hostname" : "iZ2zeixxx", "instance_id" : "xxx_l_172.26.128.15_1730267282", "ip" : "172.26.128.15", "logtail_version" : "1.8.7", "os" : "Linux; 5.10.134-17.2.al8.x86_64; #1 SMP Fri Aug 9 15:49:42 CST 2024; x86_64", "update_time" : "2024-10-30 13:48:02" } 重要 存在多台服务器时，请手动输入对应的 IP 地址，IP 地址之间需使用换行符分隔。 同一机器组中不允许同时存在 Linux 和 Windows 服务器。请勿将 Windows 和 Linux 服务器 IP 添加到同一 机器组 中。 |
