.objects.objectName> # parameters.objects.objectName 名称，当指定别名时，使用别名 key: <Kubernetes Secret Data Key> # Kubernetes Secret Data Key 字段名称
secretObjects通常包含以下三个参数：

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| secretName | 必选 | 指定将在集群中创建的 Kubernetes Secret 的名称。 |
| type | 必选 | 定义所创建的 Secret 的类型。可取值： Opaque 、 kubernetes.io/basic-auth 、 bootstrap.kubernetes.io/token 、 kubernetes.io/dockerconfigjson 、 kubernetes.io/dockercfg 、 kubernetes.io/ssh-auth 、 kubernetes.io/service-account-token 、 kubernetes.io/tls |
| data | 必选 | 定义如何将从外部获取的密钥映射到 Secret 的 data 字段中。其子字段包括： objectName : 必选，引用 parameters.objects 中定义的密钥名称（ objectName ）。如果设置了别名，则引用其别名 objectAlias 。 key : 必选，指定该密钥内容在 Secret 的 data 字段中所使用的键（Key）。 |
