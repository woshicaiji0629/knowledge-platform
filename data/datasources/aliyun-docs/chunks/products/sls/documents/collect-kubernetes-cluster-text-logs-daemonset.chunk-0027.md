### 常见问题排查
机器组心跳连接为fail
检查用户标识：如果您的服务器类型不是ECS，或使用的ECS和Project属于不同阿里云账号，请根据如下表格检查指定目录下是否存在正确的用户标识。
Linux：执行cd /etc/ilogtail/users/ && touch <uid>命令，创建用户标识文件。
Windows：进入C:\LogtailData\users\目录，创建一个名为<uid>的空文件。
如果指定路径下存在以当前Project所属的阿里云账号ID命名的文件，则说明用户标识配置正确。
检查机器组标识：如果您使用了用户自定义标识机器组，请检查指定目录下是否存在user_defined_id文件，如果存在请检查该文件中的内容是否与机器组配置的自定义标识一致。
Linux：
