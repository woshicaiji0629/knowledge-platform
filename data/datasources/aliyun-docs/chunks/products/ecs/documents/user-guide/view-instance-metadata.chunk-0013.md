| 分类 | 元数据 | 说明 | 示例 |
| --- | --- | --- | --- |
| 实例基本信息 | instance-id | 实例 ID。 | i-bp13znx0m0me8cquu**** |
| instance/instance-name | 实例名称。 | iZbp1bfqfsvqzxhmnd5**** |  |
| hostname | 实例的主机名。 | iZbp13znx0m0me8cquu**** |  |
| instance/instance-type | 实例规格。 | ecs.g6e.large |  |
| serial-number | 实例所对应的序列号。 | 4acd2b47-b328-4762-852f-998**** |  |
| region-id | 实例所属地域 ID。 | cn-hangzhou |  |
| zone-id | 实例所属可用区。 | cn-hangzhou-i |  |
| owner-account-id | 实例拥有者的阿里云账号 ID。 | 1609**** |  |
| tags/instance/[tagKey] | 用于获取实例的指定标签值，其中 [tagKey] 为要查询的标签键。 使用此功能，需先调用 [ModifyInstanceMetadataOptions](../developer-reference/api-ecs-2014-05-26-modifyinstancemetadataoptions.md) 接口，将实例的 InstanceMetadataTags 参数设置为 enabled ，以启用此功能。 | dev |  |
| 镜像信息 | image-id | 创建实例时所使用的镜像 ID。 | aliyun_3_x64_20G_alibase_20210425.vhd |
| image/market-place/product-code | 云市场镜像的商品码。 | cmjj01**** |  |
| image/market-place/charge-type | 云市场镜像的计费方式。 | PrePaid |  |
| source-address | 镜像库地址，主要为 yum 源或者 apt 源，供 Linux 实例的包管理软件获取更新。 | http://mirrors.cloud.aliyuncs.com |  |
| 基础网络配置 | network-type | 网络类型，只支持 VPC 类型实例。 | vpc |
| vpc-id | 实例所属 VPC ID。 | vpc-bp1e0g399hkd7c8q**** |  |
| vpc-cidr-block | 实例所属 VPC CIDR 段。 | 192.168.XX.X
