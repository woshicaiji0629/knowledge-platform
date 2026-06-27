### 4. 变量说明

| 变量 | 说明 |
| --- | --- |
| ${your_aliyun_user_id} | 设置为您的阿里云账号（主账号）ID。更多信息，请参见 [配置用户标识](configure-a-user-identifier.md) 。 |
| ${your_machine_group_user_defined_id} | 自定义设置机器组的自定义标识，用于创建自定义机器组。例如 nginx-log-sidecar 。 重要 请确保该标识在您的 Project 所在地域内唯一。 |
| ${your_region_config} | 请根据日志服务 Project 所在地域和访问的网络类型填写。其中，地域信息请参见 [开服地域](sls-supported-regions1.md) 。 示例：若 Project 位于华东 1（杭州），则以阿里云内网访问时为 cn-hangzhou ，公网访问时使用 cn-hangzhou-internet 。 |
| ${shared_volume_name} | 自定义设置卷的名称。 重要 volumeMounts 节点下的 name 参数与 volumes 节点下的 name 参数需设置为一致，即确保 LoongCollector 容器和业务容器挂载相同的卷上。 |
| ${dir_containing_your_files} | 设置挂载路径，即容器待采集文本日志所在目录。 |
