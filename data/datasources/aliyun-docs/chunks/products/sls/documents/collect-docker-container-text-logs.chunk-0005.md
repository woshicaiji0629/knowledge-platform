# LoongCollector镜像地址 docker pull aliyun-observability-release-registry.${region_id}.cr.aliyuncs.com/loongcollector/loongcollector:v3.0.12.0-25723a1-aliyun # Logtail镜像地址 docker pull registry.${region_id}.aliyuncs.com/log-service/logtail:v2.1.11.0-aliyun
启动LoongCollector容器
运行以下命令启动容器，确保正确挂载目录并设置必要环境变量：
docker run -d \ -v /:/logtail_host:ro \ -v /var/run/docker.sock:/var/run/docker.sock \ --env ALIYUN_LOGTAIL_CONFIG=/etc/ilogtail/conf/${sls_upload_channel}/ilogtail_config.json \ --env ALIYUN_LOGTAIL_USER_ID=${aliyun_account_id} \ --env ALIYUN_LOGTAIL_USER_DEFINED_ID=${user_defined_id} \ aliyun-observability-release-registry.${region_id}.cr.aliyuncs.com/loongcollector/loongcollector:v3.0.12.0-25723a1-aliyun
参数说明：
${sls_upload_channel}：日志上传通道，由Project所在[地域](collect-docker-container-text-logs.md)-网络传输类型构成。示例：

| 传输类型 | 配置值格式 | 示例 | 适用场景 |
| --- | --- | --- | --- |
| 内网传输 | regionId | cn-hangzhou | ECS 与 Project 同地域 |
| 公网传输 | regionId-internet | cn-hangzhou-internet | ECS 和 Project 属于不同地域 服务器为其他云厂商服务器或自建 IDC |
| 传输加速 | regionId-acceleration | cn-hangzhou-acceleration | 国内外跨区域通信 |
