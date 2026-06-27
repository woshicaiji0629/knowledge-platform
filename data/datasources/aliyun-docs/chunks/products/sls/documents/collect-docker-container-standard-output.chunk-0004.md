# 启动Logtail容器，替换${region_id}，${aliyun_account_id}，${user_defined_id} docker run -d \ -v /:/logtail_host:ro \ -v /var/run/docker.sock:/var/run/docker.sock \ --env ALIYUN_LOGTAIL_CONFIG=/etc/ilogtail/conf/${region_id}/ilogtail_config.json \ --env ALIYUN_LOGTAIL_USER_ID=${aliyun_account_id} \ --env ALIYUN_LOGTAIL_USER_DEFINED_ID=${user_defined_id} \ registry.${region_id}.aliyuncs.com/log-service/logtail:v2.1.11.0-aliyun
重要
如果您要自定义配置Logtail容器的启动参数，只需保证以下前提条件。
启动时，必须配置3个环境变量ALIYUN_LOGTAIL_CONFIG，ALIYUN_LOGTAIL_USER_ID和ALIYUN_LOGTAIL_USER_DEFINED_ID。
将宿主机上的/var/run目录挂载到Logtail容器的/var/run目录。
将宿主机根目录挂载到Logtail容器的/logtail_host目录。
如果Logtail日志（/usr/local/ilogtail/ilogtail.LOG）中出现The parameter is invalid : uuid=none的错误日志，请在宿主机上创建一个product_uuid文件，在其中输入任意合法UUID（例如169E98C9-ABC0-4A92-B1D2-AA6239C0D261），并把该文件挂载到Logtail容器的/sys/class/dmi/id/product_uuid目录。
输入docker ps查看容器是否启动成功。
创建用户自定义标识机器组
登录[日志服务控制台](https://sls.console.aliyun.com)，在Project列表，单击打开目标Project。
左侧导航栏中，选择资源>机器组。在打开的机器组页面中，选择机器组右侧的>创建机器组。
在创建机器组页面填写名称，机器组标识选择用户自定义标识，并在用户自定义标识中填入步骤一中参数${user_defined_id}的值，本例为user-defined-docker-1。
