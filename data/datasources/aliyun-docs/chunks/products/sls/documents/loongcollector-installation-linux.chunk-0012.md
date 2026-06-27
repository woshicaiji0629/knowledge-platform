ll ${region_id}-acceleration
查看启动状态：执行命令，返回loongcollector is running表示启动成功。
sudo /etc/init.d/loongcollectord status
配置用户ID：用户ID文件包含Project所属阿里云主账号的ID信息，用于标识该账号有权限访问、采集这台服务器的日志。
只有在采集非本账号ECS、自建服务器、其他云厂商服务器日志时需要配置用户ID。多个账号对同一台服务器进行日志采集时，支持在同一台服务器上创建多个用户ID文件。
登录[日志服务控制台](https://sls.console.aliyun.com/)，鼠标悬浮在右上角用户头像上，在弹出的标签页中查看并复制账号ID。注意需要复制主账号ID。
在安装了LoongCollector的服务器上，以主账号ID作为文件名，创建用户ID文件。
touch /etc/ilogtail/users/{阿里云账号ID} # 如果/etc/ilogtail/users目录不存在，请手动创建目录。用户ID文件只需配置文件名，无需配置文件后缀。
配置机器组：日志服务通过机器组发现用户自定义标识并与主机上的LoongCollector建立心跳连接。
在服务器上将自定义字符串user-defined-test-1写入用户自定义标识文件，该字符串将在后续步骤中使用。
#向指定文件写入自定义字符串，若目录不存在需手动创建。文件路径和名称由日志服务固定，不可自定义。 echo "user-defined-test-1" > /etc/ilogtail/user_defined_id
登录[日志服务控制台](https://sls.console.aliyun.com/)。在Project列表中，单击目标Project。
单击资源，单击机器组。
单击机器组右侧的，单击创建机器组。
进行如下配置后单击确定。
设置机器组名称：名称Project内唯一，必须以小写字母或数字开头和结尾，且只能包含小写字母、数字、连字符（-）和下划线（_），长度为3~128字符。
机器组标识：选择用户自定义标识。
用户自定义标识：输入配置的用户自定义标识，需要与服务器用户自定义标识文件中自定义字符串内容一致。此例为user-defined-test-1。
机器组创建完成后，在机器组列表单击目标机器组，在机器组状态中查看心跳状态，若为FAIL，请等待两分钟左右并手动刷新。如果心跳为OK则表示创建成功。
安装完成后若需要采集日志还需进行[采集配置](host-text-log-collection-auto-install.md)。
