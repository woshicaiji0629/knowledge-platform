## 步骤六：跨账号采集需检查用户标识
重要
服务器类型不是ECS，或使用的ECS和Project属于不同阿里云账号，必须检查是否存在正确的用户标识。
用户标识必须是阿里云账号ID（主账号ID）。具体操作请参见[配置用户标识](configure-a-user-identifier.md)。
您可以通过指定目录下的用户标识文件判断是否存在用户标识。如果返回结果为空，则您需要查看指定路径中是否已有用户标识文件。用户标识的作用在于标识这台服务器有权限被该账号访问。
说明
用户标识文件路径如下：
Linux系统：/etc/ilogtail/users/
Windows系统：C:\LogtailData\users\
如果指定路径下无用户标识文件或用户标识文件配置错误，请按照如下方法解决。
Linux系统：执行cd /etc/ilogtail/users/ && touch <uid>命令，创建用户标识文件。其中<uid>为Project所属的阿里云账号ID。
Windows系统：进入C:\LogtailData\users\目录，创建一个名为<uid>的空文件。其中<uid>为Project所属的阿里云账号ID。
如果指定路径下存在以当前Project所属的阿里云账号ID命名的文件，则说明用户标识配置正确。
