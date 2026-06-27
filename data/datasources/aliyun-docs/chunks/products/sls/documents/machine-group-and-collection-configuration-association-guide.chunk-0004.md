### Linux系统
在/etc/ilogtail/users目录下，创建日志服务所属的阿里云账号ID文件。
touch /etc/ilogtail/users/{阿里云账号ID}
重要
如果/etc/ilogtail/users目录不存在，请手动创建目录。
新增、删除用户标识后，1分钟之内即可生效。
当您使用多个阿里云账号下的日志服务Project对同一台服务器进行日志采集时，您可以在同一台服务器上创建多个阿里云账号ID文件。例如：
touch /etc/ilogtail/users/{阿里云账号ID 1} touch /etc/ilogtail/users/{阿里云账号ID 2}
