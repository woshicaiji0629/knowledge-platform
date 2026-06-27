### 容器路径映射文件（docker_path_config.json）
docker_path_config.json文件只有在采集容器日志时才会创建，用于记录容器文件和宿主机文件的路径映射关系。文件类型为JSON。
如果在诊断采集错误时，如果提示DOCKER_FILE_MAPPING_ALARM错误，表示添加Docker文件映射失败，可以通过docker_path_config.json文件排查。
说明
docker_path_config.json文件为记录文件，任何修改操作均不会生效。删除后会自动创建，不影响业务的正常运行。
因采集容器日志异常而提交[工单](https://selfservice.console.aliyun.com/ticket/category/sls/today)时，请在工单中上传此文件。
文件路径
/usr/local/ilogtail/docker_path_config.json
文件示例
$cat /usr/local/ilogtail/docker_path_config.json { "detail" : [ { "config_name" : "##1.0##k8s-log-c12ba2028cfb444238cd9ac1286939f0b$nginx", "container_id" : "df19c06e854a0725ea7fca7e0378b0450f7bd3122f94fe3e754d8483fd330d10", "params" : "{\n \"ID\" : \"df19c06e854a0725ea7fca7e0378b0450f7bd3122f94fe3e754d8483fd330d10\",\n \"Path\" : \"/logtail_host/var/lib/docker/overlay2/947db346695a1f65e63e582ecfd10ae1f57019a1b99260b6c83d00fcd1892874/diff/var/log\",\n \"Tags\" : [\n \"nginx-type\",\n \"access-log\",\n \"_image_name_\",\n \"registry.cn-hangzhou.aliyuncs.com/log-service/docker-log-test:latest\",\n \"_container_name_\",\n \"nginx-log-demo\",\n \"_pod_name_\",\n \"nginx-log-demo-h2lzc\",\n \"_namespace_\",\n \"default\",\n \"_pod_uid_\",\n \"87e56ac3-b65b-11e8-b172-00163f0
