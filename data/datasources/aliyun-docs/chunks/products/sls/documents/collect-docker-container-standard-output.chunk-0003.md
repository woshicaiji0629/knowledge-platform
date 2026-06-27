## 步骤一：安装Logtail容器并创建机器组
拉取Logtail镜像
登录宿主机，根据日志服务Project所在地域，获取对应的${region_id}。替换${region_id}后，使用以下命令拉取Logtail镜像。
重要
各地域对应的${region_id}请参见[开服地域](sls-supported-regions1.md)，例如华东 1（杭州）对应的${region_id}为cn-hangzhou。
#拉取Logtail镜像： docker pull registry.${region_id}.aliyuncs.com/log-service/logtail:v2.1.11.0-aliyun #如果您的服务器处于阿里云VPC网络中，请使用如下命令行拉取Logtail镜像： docker pull registry-vpc.${region_id}.aliyuncs.com/log-service/logtail:v2.1.11.0-aliyun
启动Logtail容器
参数说明

| 参数 | 参数说明 |
| --- | --- |
| ${region_id} | 根据 日志服务 Project 所在地域，获取对应的 ${region_id} ，各地域对应的 ${region_id} 请参见 [开服地域](sls-supported-regions1.md) 。网络类型选择请参见 [Logtail](select-a-network-type.md) [网络类型，启动参数与配置文件](select-a-network-type.md) 。 示例：若 Project 位于华东 1（杭州），则以阿里云内网访问时 ${region_id} 为 cn-hangzhou ，公网访问时使用 cn-hangzhou-internet 。 |
| ${aliyun_account_id} | 日志服务 所在的阿里云账号（主账号）ID。获取方法，请参见 [获取日志服务所在的阿里云账号（主账号）ID](configure-a-user-identifier.md) 。 |
| ${user_defined_id} | 设置机器组的用户自定义标识，例如 user-defined-docker-1 。该标识在 Project 所在地域内必须唯一。 |

根据参数说明，替换命令模板中的3个参数：${region_id}、${aliyun_account_id}和${user_defined_id}，然后执行以下命令启动Logtail容器。
