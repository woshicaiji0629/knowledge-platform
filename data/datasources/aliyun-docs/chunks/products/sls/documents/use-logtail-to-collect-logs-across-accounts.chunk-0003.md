## 步骤二：创建用户自定义标识机器组
在ECS服务器上创建机器组的自定义用户标识文件。
重要
您需要在ECS集群B的每台ECS服务器中创建机器组的用户自定义标识文件。
登录阿里云账号B下的ECS服务器。
在指定目录下创建/etc/ilogtail/user_defined_id文件并添加用户自定义标识。
例如配置用户自定义标识为application_b，则在文件中输入application_b，并保存。文件路径说明，请参见[创建用户自定义标识机器组](create-a-user-defined-identity-machine-group.md)。
在日志服务控制台上创建机器组。
使用阿里云账号A登录[日志服务控制台](https://sls.console.aliyun.com)。
在Project列表区域，单击目标Project。
在左侧导航栏中，选择资源>机器组。
选择机器组右侧的>创建机器组。
在创建机器组对话框中，配置如下参数，然后单击确定。
其中用户自定义标识需设置为您在步骤[1](use-logtail-to-collect-logs-across-accounts.md)中设置的用户自定义标识。其他参数说明，请参见[创建用户自定义标识机器组](create-a-user-defined-identity-machine-group.md)。设置名称为group-b，机器组标识选择用户自定义标识，用户自定义标识填写application_b。
检查机器组中的服务器心跳都为OK。
在机器组列表中，单击目标机器组。
在机器组配置页面，查看使用了相同用户自定义标识的ECS服务器及其心跳状态。
心跳为OK表示ECS服务器与日志服务的连接正常。如果显示FAIL请参见[Logtail](troubleshoot-the-errors-related-to-logtail-machine-groups.md)[机器组无心跳](troubleshoot-the-errors-related-to-logtail-machine-groups.md)。确认机器组中共4台机器的心跳状态均显示为OK，表示所有机器已正常连接至日志服务。
