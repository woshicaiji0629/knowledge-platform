### ACKRequiredNodeSelector
规则说明：限制集群中某些应用 Pod 必须配置指定的nodeSelector标签。
重要等级：low。
参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| nodeSelector | array | 包含以下取值。 key ：指定 Label Key。 allowedRegex ：Label Value 的正则表达式。 |
