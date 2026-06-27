S: KMSAuth: oidcProviderARN: acs:ram::<role-name>:oidc-provider/ack-rrsa-<cluster-id> serviceAccountRef: name: test-serviceaccount-auth namespace: test
spec字段说明

| crd 字段 | 描述 | 是否必选 |
| --- | --- | --- |
| conditions | 定义允许访问该资源的命名空间条件 | 是 |
| KMS | 连接 KMS 凭据管家服务获取密钥 | 否 |
| OOS | 连接 OOS 服务获取加密参数 | 否 |

conditions字段说明

| crd 字段 | 描述 | 是否必选 |
| --- | --- | --- |
| namespaceSelector | 使用标签选择器匹配允许访问的命名空间 | 是 |
| namespaces | 明确列出允许访问的命名空间名称列表 | 否 |
| namespaceRegexes | 使用正则表达式匹配允许访问的命名空间名称列表 | 否 |
