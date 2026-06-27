### 同账号同地域
仅当服务器为阿里云ECS，且ECS与Project属于同一个阿里云账号，所属[地域](loongcollector-installation-linux.md)也相同时，日志服务可一键在ECS中安装LoongCollector，借助OOS编排能力，无需登录ECS手动执行安装步骤。
一键安装能力已集成到日志服务的接入模板中，日志服务提供了正则、单行、多行等多种文本日志接入模板，各模板之间仅[处理插件](processing-plug-ins.md)不同；模板内支持添加、删除处理插件。请根据采集日志的特点选择模板，或任意选择文本日志模板后再根据日志特点进行处理插件配置。
具体操作如下：
登录[日志服务控制台](https://sls.console.aliyun.com/)，在Project列表中，单击目标Project。
单击日志存储，在日志库中单击目标LogStore前的，展开LogStore。
单击数据接入后的，在弹框中选择单行 - 文本日志接入模板，单击立即接入。
单击创建机器组，选择与Project同地域的ECS实例后（可选择多台ECS实例），单击安装并创建为机器组。
等待安装完成，填写名称后即可单击确定。若无法安装成功，请单击重建安装任务，并重新选择ECS，选择时需确认ECS地域与Project地域相同。
单击下一步，如果心跳为FAIL，单击自动重试后等待两分钟左右直到心跳变为OK。
至此一键安装完成。单击下一步，将进行[采集配置](host-text-log-collection-auto-install.md)。
