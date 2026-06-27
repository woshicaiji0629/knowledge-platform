## 步骤七：如果是用户自定义标识机器组，检查是否已配置自定义标识
若您使用了用户自定义标识机器组，您可以通过指定目录下的user_defined_id文件判断是否已在服务器上配置用户自定义标识。
如果返回结果为空，您需要查看是否存在user_defined_id文件或该文件中是否已配置用户自定义标识。
说明
user_defined_id文件路径如下：
Linux系统：/etc/ilogtail/user_defined_id
Windows系统：C:\LogtailData\user_defined_id
如果user_defined_id文件不存在，则新增一个user_defined_id的文件，然后在文件中输入机器组的用户自定义标识。具体操作，请参见[配置用户自定义标识](create-a-user-defined-identity-machine-group.md)。
如果user_defined_id文件中无用户自定义标识或自定义标识配置错误，则在文件中新增一行，然后输入机器组的用户自定义标识。具体操作，请参见[配置用户自定义标识](create-a-user-defined-identity-machine-group.md)。
如果user_defined_id文件已包含您在机器组中设置的用户自定义标识，则说明用户自定义标识配置正确。
