### 机器组心跳连接为fail
检查用户标识：如果您的服务器类型不是ECS，或ECS和Project属于不同阿里云账号，请检查指定目录下是否存在正确的用户标识，如不存在请参考如下命令手动创建。
Linux：执行cd /etc/ilogtail/users/ && touch <uid>命令，创建用户标识文件。
Windows：进入C:\LogtailData\users\目录，创建一个名为<uid>的空文件。
检查机器组标识：如果您在创建机器组时使用了用户自定义标识，请检查指定目录下是否存在user_defined_id文件，如果存在请检查该文件中的内容是否与机器组配置的自定义标识一致。
Linux：
