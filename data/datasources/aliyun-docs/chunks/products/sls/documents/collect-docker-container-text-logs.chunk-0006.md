输 | regionId-internet | cn-hangzhou-internet | ECS 和 Project 属于不同地域 服务器为其他云厂商服务器或自建 IDC |
| 传输加速 | regionId-acceleration | cn-hangzhou-acceleration | 国内外跨区域通信 |

${aliyun_account_id}：阿里云主账号ID。
${user_defined_id}：机器组的用户自定义标识，用于绑定机器组（如user-defined-docker-1），需在地域内唯一。
重要
必须满足的启动条件：
正确配置三个关键环境变量：
ALIYUN_LOGTAIL_CONFIG、ALIYUN_LOGTAIL_USER_ID、ALIYUN_LOGTAIL_USER_DEFINED_ID。
挂载/var/run/docker.sock：用于监听容器生命周期事件。
挂载/→/logtail_host：用于访问宿主机文件系统。
验证容器运行状态
docker ps | grep loongcollector
预期输出示例：
6ad510001753 aliyun-observability-release-registry.cn-beijing.cr.aliyuncs.com/loongcollector/loongcollector:v3.0.12.0-25723a1-aliyun "/usr/local/ilogtail…" About a minute ago Up About a minute recursing_shirley
配置机器组
在左侧导航栏资源组>机器组，单击创建机器组，配置如下参数并单击确定：
名称：自定义机器组名称（如docker-host-group）。
机器组标识：：选择用户自定义标识。
用户自定义标识：输入启动容器时设置的${user_defined_id}。必须完全一致，否则无法关联成功。
验证机器组心跳状态
单击新建机器组名称，进入机器组详情页，查看机器组状态：
OK：表示LoongCollector 已成功连接到日志服务。
FAIL：请参考[心跳异常问题汇总](troubleshooting-of-abnormal-heartbeat-problems.md)排查。
