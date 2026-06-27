o "user-defined-1" > /etc/ilogtail/user_defined_id
（可选）使用以下命令检查用户自定义标识是否写入成功。如果返回user-defined-1，则表示写入成功。
cat /etc/ilogtail/user_defined_id
新增、删除、修改user_defined_id文件后，默认情况下，1分钟内生效。如果需要立即生效，请执行以下命令重启Logtail。
/etc/init.d/ilogtaild stop /etc/init.d/ilogtaild start
Windows环境
登录已安装Logtail的Windows服务器，在C:\LogtailData目录下新建user_defined_id文件并写入user-defined-1，完成后保存。
说明
如果目录C:\LogtailData不存在，请先手动创建该目录。
新增、删除、修改user_defined_id文件后，默认情况下，1分钟内生效。如需立即生效，请根据以下步骤重启Logtail。
选择开始>控制面板>管理工具>服务。
在服务对话框中，选择对应的服务。
如果是0.x.x.x版本，选择LogtailWorker服务。
如果是1.0.0.0及以上版本，选择LogtailDaemon服务。
右键单击重新启动使配置生效。
容器环境
用户自定义标识配置在Logtail容器的环境变量ALIYUN_LOGTAIL_USER_DEFINED_ID中，可通过docker inspect ${logtail_container_name} | grep ALIYUN_LOGTAIL_USER_DEFINED_ID命令查看。
登录[日志服务控制台](https://sls.console.aliyun.com)，在Project列表，单击打开目标Project。在左侧导航栏中，选择资源>机器组。在打开的机器组页面中，选择机器组右侧的>创建机器组。
在弹出的创建机器组页面，填写以下信息，并单击确定。
