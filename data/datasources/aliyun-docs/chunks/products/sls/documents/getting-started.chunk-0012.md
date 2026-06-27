## 资源清理
为避免产生不必要的费用，完成操作后，务必按照以下步骤清理所有已创建的资源。
停止日志生成脚本
登录ECS实例，执行以下命令停止后台运行的日志生成脚本。
kill $(ps aux | grep '[g]enerate_nginx_logs.sh' | awk '{print $2}')
卸载LoongCollector（可选）
示例代码中${region_id}可使用cn-hangzhou替换，若想加快执行速度，请将${region_id}替换为ECS所属[地域](loongcollector-installation-linux.md)。
wget https://aliyun-observability-release-${region_id}.oss-${region_id}.aliyuncs.com/loongcollector/linux64/latest/loongcollector.sh -O loongcollector.sh;
执行卸载命令。
chmod +x loongcollector.sh; sudo ./loongcollector.sh uninstall;
删除Project。
在[日志服务控制台](https://sls.console.aliyun.com)Project列表页面，找到已创建的Project（例如nginx-quickstart-xxx）。
在右侧操作列单击删除。
在删除面板中，输入Project名称，选择删除原因。
单击确定，删除Project将同时删除其下的LogStore、采集配置、仪表盘、告警规则等所有关联资源。
警告
删除Project后，其管理的所有日志数据及配置信息都会被释放且不可恢复。删除前请慎重确认，避免数据丢失。
