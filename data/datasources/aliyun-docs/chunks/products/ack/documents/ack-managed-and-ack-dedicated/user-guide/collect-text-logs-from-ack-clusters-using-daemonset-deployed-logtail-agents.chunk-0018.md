| 字段 | 说明 | 示例 | 注意事项 |
| --- | --- | --- | --- |
| aliyun_logs_{key} | 必选项。{key}只能包含小写字母、数字和-。 若不存在 aliyun_logs_{key}_logstore，则默认创建并采集到名为{key}的 logstore。 当值为 stdout 时表示采集容器的标准输出；其他值为容器内的日志路径。 | - name: aliyun_logs_catalina value: stdout - name: aliyun_logs_access-log value: /var/log/nginx/access.log | 默认采集方式为极简模式。如需解析日志内容，建议使用日志服务控制台，或者 CRD 进行配置。 {key}表示日志服务中 LoongCollector 采集配置的名称，需保持在 K8s 集群内唯一。 |
| aliyun_logs_{key}_tags | 可选。值为{tag-key}={tag-value}类型，用于对日志进行标识。 | - name: aliyun_logs_catalina_tags value: app=catalina | 不涉及。 |
| aliyun_logs_{key}_project | 可选。值为指定的日志服务 Project。当不存在该环境变量时，为您安装时所选的 Project。 | - name: aliyun_logs_catalina_project value: my-k8s-project | Project 需与您的 LoongCollector 工作所在的 Region 一致。 |
| aliyun_logs_{key}_logstore | 可选。值为指定的日志服务 Logstore。当不存在该环境变量时，Logstore 和{key}一致。 | - name: aliyun_logs_catalina_logstore value: my-logstore | 不涉及。 |
| aliyun_logs_{key}_shard | 可选。值为创建 Logstore 时的 shard 数，取值范围为[1 , 10]。当不存在该环境变量时，值为 2。 说明 若 logstore 已经存在，则该参数不生效。 | - name: aliyun_logs_catalina_shard value: '4' | 不涉及。 |
| aliyun_logs_{key}_ttl | 可选。值为指定的日志保存时间，取值范围为[1 , 3650]。 当取值为 3650 时，指定日志的保存时间为永久保存。 当不存在该环境变量时，默认指定日志的保存时间为 90 天。 说明 若 Logstore 已经存在，则该参数不生效。 | - na
