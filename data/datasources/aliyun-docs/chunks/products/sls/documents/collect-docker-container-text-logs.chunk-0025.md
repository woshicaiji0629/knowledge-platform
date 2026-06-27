### 常见问题排查
机器组心跳连接为fail
检查用户标识：如果您的服务器类型不是ECS，或使用的ECS和Project属于不同阿里云账号，请根据如下表格检查指定目录下是否存在正确的用户标识。
Linux：执行cd /etc/ilogtail/users/ && touch <uid>命令，创建用户标识文件。
Windows：进入C:\LogtailData\users\目录，创建一个名为<uid>的空文件。
如果指定路径下存在以当前Project所属的阿里云账号ID命名的文件，则说明用户标识配置正确。
检查机器组标识：如果您使用了用户自定义标识机器组，请检查指定目录下是否存在user_defined_id文件，如果存在请检查该文件中的内容是否与机器组配置的自定义标识一致。

| 系统 | 指定目录 | 解决方法 |
| --- | --- | --- |
| Linux | /etc/ilogtail/user_defined_id | # 配置用户自定义标识,如目录不存在请手动创建 echo "user-defined-1" > /etc/ilogtail/user_defined_id |
| Windows | C:\LogtailData\user_defined_id | 在 C:\LogtailData 目录下新建 user_defined_id 文件，并写入用户自定义标识。（如目录不存在，请手动创建） |
