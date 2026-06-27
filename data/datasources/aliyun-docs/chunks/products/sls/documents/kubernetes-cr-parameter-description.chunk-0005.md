### spec.projecct
目标Project信息。
说明
project字段在CR创建后不允许更改，如需切换project请创建新的CR。

| 参数 | 数据类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 目标 Project 的名称，若不存在会自动创建。 |
| description | string | 否 | Project 的描述（仅在创建时生效）。 |
| endpoint | string | 否 | Project 所在地域的 [服务入口](developer-reference/service-entrance.md) ，默认值为集群所在的地域。 该参数仅控制采集配置的创建地域，不控制采集器数据投递目标。 如需跨地域采集，请配置 [config_server_address](logtail-configuration-files-and-record-files.md) [和](logtail-configuration-files-and-record-files.md) [data_server_list](logtail-configuration-files-and-record-files.md) 。 |
| uid | string | 否 | 目标 Project 所属的阿里云主账号的 uid。默认值为当前集群所属的主账号 uid。 该参数仅控制采集配置创建到哪个账号下。 如需跨账号采集日志，请同步配置 alibaba-log-controller 组件的环境变量： ALICLOUD_LOG_ACCOUNT_INFOS={"<uid>":{"accessKeyID":"<your_access_key_id>","accessKeySecret":"<your_access_key_secret>"}} 。 |
