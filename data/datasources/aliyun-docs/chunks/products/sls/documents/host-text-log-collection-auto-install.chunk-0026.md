### 如何将ECS服务器的日志传输到另一个阿里云账号的Project？
如果您尚未安装LoongCollector，请参考[安装采集器](loongcollector-installation-linux.md)选择合适的跨账号场景进行安装；
如果您已安装了LoongCollector，请参考如下步骤配置用户标识，用于标识这台服务器有权限被日志服务Project所属账号访问、采集日志。
只有在采集非本账号ECS、自建IDC、其他云厂商服务器日志时需要配置用户标识。
复制日志服务所属的主账号ID：鼠标悬浮在右上角用户头像上，在弹出的标签页中查看并复制账号ID。
登录需要采集日志的服务器，创建阿里云账号ID文件配置用户标识：
touch /etc/ilogtail/users/{阿里云账号ID} # 如果/etc/ilogtail/users目录不存在，请手动创建目录。用户标识配置文件只需配置文件名，无需配置文件后缀。
