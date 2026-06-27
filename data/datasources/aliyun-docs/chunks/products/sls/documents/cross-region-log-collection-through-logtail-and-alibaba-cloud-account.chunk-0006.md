## 步骤二：在地域A的ECS实例中配置用户自定义标识
在指定目录下建立用户自定义标识文件user_defined_id并配置用户自定义标识。
重要
同一机器组中不允许同时存在Linux和Windows服务器，请勿在Linux和Windows服务器上配置相同的用户自定义标识。
一个服务器可配置多个用户自定义标识，标识之间以换行符分割。
Linux环境
登录已安装Logtail的Linux服务器，使用以下命令配置用户自定义标识。
说明
如果目录/etc/ilogtail/不存在，请先手动创建该目录。
echo "user-defined-1" > /etc/ilogtail/user_defined_id
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
