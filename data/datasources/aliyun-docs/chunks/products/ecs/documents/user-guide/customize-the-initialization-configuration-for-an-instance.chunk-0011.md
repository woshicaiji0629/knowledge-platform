## MIME multi-part文件
简介
MIME multi-part文件可以传输多类型指令。例如，您可以使用MIME multi-part文件将text/cloud-config（用于Cloud-Init配置）和text/x-shellscript（Shell脚本） 同时包含在用户数据中。Cloud-Init会分别解析并执行这些不同类型的指令。
运行频率
启动实例：由MIME消息中各个部分的类型和cloud-init的配置。例如，MIME消息中内容类型为User-Data脚本，则仅在实例首次启动时运行一次；MIME消息中内容类型为Cloud Config数据，则遵循Cloud Config数据的运行频率。
更换操作系统：自动运行。
重新初始化系统盘：自动运行。
重要
以下情况不会自动运行脚本：
如果更换操作系统使用的是自定义镜像且来源于原实例，更换操作系统时会判断实例不是初次启动，因此不会自动运行脚本。
如果创建使用的是自定义镜像，则创建实例时系统盘就有数据，初始化系统盘时会判断实例不是首次启动，因此不会自动运行脚本。
格式
首行为Content-Type：multipart/mixed：boundary="****"，boundary可自定义，且起始位置不能有空格。
第二行指定版本MIME-Version：1.0，该字段通常在每个MIME消息中是必需的。
MIME multi-part文件示例
Content-Type: multipart/mixed; boundary="//" MIME-Version: 1.0 --// Content-Type: text/cloud-config; charset="us-ascii" MIME-Version: 1.0 Content-Transfer-Encoding: 7bit Content-Disposition: attachment; filename="cloud-config.txt" #cloud-config runcmd: - [ mkdir, /test-cloudinit ] write_files: - path: /test-cloudinit/cloud-init.txt content: | Created by cloud-init append: true --// Content-Type: text/x-shellscript; charset="us-ascii" MIME-Version: 1.0 Content-Transfer-Encoding: 7bit Content-Disposition: attachment; filename="userdata.txt" #!/bin/bash mkdir test-userscript touch /t
