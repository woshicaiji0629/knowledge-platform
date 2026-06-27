## 创建加密云盘
创建加密云盘。
重要
加密操作不可逆，云盘一旦被加密，无法再转为非加密状态。
控制台
创建云盘分为以下场景。
云盘通过非共享而来的加密快照创建：默认使用该快照所使用的加密密钥进行加密，可下拉列表更换KMS密钥。
云盘通过共享而来的加密快照创建：默认使用服务密钥进行加密，可下拉列表更换KMS密钥。
在已开启块存储账号级默认加密的地域创建：默认使用指定的账号级密钥进行加密，可下拉列表更换KMS密钥。
其他情况：可在设置中勾选加密后，下拉列表选择KMS密钥。默认使用服务密钥进行加密。
KMS密钥分为以下两种类型。
服务密钥：由云产品为 ECS 服务自动创建和管理的密钥，别名为alias/acs/ecs。满足基本的数据加密需求，操作简便，无需管理密钥生命周期。
主密钥：在 KMS 中自行导入/创建的拥有完全控制权的密钥。适用于对数据安全有更高要求，需要自行管理密钥的轮转、禁用、删除等生命周期。
首次选择主密钥加密时，需要依照界面提示为ECS授权AliyunECSDiskEncryptDefaultRole角色，以允许访问KMS资源。
API
创建ECS实例时加密系统盘及数据盘。
调用API接口[RunInstances](../developer-reference/api-ecs-2014-05-26-runinstances.md)创建ECS实例时，通过设置系统盘或数据盘的Encrypted值和KMSKeyId值实现加密。
单独创建加密数据盘。
调用API接口[CreateDisk](../developer-reference/api-ecs-2014-05-26-createdisk.md)创建数据盘时，通过设置Encrypted值和KMSKeyId值实现加密。
后续步骤。
系统盘：创建后即可使用，无需额外操作。
数据盘：
随实例创建：
Windows：创建后即可使用，无需额外操作。
Linux：需要完成[初始化](initialize-a-data-disk.md)后才可使用。
单独创建：需要将其[挂载至](attach-a-data-disk.md)[ECS](attach-a-data-disk.md)[实例](attach-a-data-disk.md)并完成[初始化](initialize-a-data-disk.md)后才可使用。
