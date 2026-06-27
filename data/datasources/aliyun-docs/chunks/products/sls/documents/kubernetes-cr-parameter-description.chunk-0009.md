自动把日志来源设备的公网 IP 地址和日志到达服务端的时间添加到日志的 Tag 字段中。 false ：不开启记录外网 IP 和日志接收时间功能。 |
| enableTracking | bool | 否 | 是否启用 WebTracking 功能。默认值为 false。 |
| encryptConf | object | 否 | [加密配置数据结构](developer-reference/api-sls-2020-12-30-struct-encryptconf.md) ，包含参数 enable 、 encrypt_type 、 user_cmk_info 。默认值为空。 |
| meteringMode | string | 否 | [计费模式](billing-methods.md) 。更多信息，请参见 [管理](manage-a-logstore.md) [LogStore](manage-a-logstore.md) 。默认值为空，可选值： ChargeByFunction ：按功能计费 ChargeByDataIngest ：按写入量计费。 说明 如果 LogStore 的 queryMode 为 query，只支持按功能计费。 如果账号未开通写入量计费，无法配置为 ChargeByDataIngest。 |
| index | object | 否 | 指定索引（仅限 LogStore 创建时生效），格式参考通用数据格式 [index](developer-reference/api-sls-2020-12-30-struct-index.md) 。该参数需要 loongcollector-operator 组件版本号大于等于 1.0.6 有效。 |
