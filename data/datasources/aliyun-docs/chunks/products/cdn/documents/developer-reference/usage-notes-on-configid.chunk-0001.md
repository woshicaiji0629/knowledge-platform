## ConfigId使用说明

| 功能 | 接口调用说明 |
| --- | --- |
| 生成 ConfigId | 调用 [BatchSetCdnDomainConfig](../api-batchsetcdndomainconfig.md) 、 [SetCdnDomainStagingConfig](../api-setcdndomainstagingconfig.md) ，配置完成后生成 ConfigId。 |
| 查询 ConfigId | 调用 [DescribeCdnDomainConfigs](../api-describecdndomainconfigs.md) 、 [DescribeCdnDomainStagingConfig](../api-describecdndomainstagingconfig.md) ，查询结果返回对应配置的 ConfigId。 |
| 通过 ConfigId 更新配置项 | 调用 [BatchSetCdnDomainConfig](../api-batchsetcdndomainconfig.md) 、 [SetCdnDomainStagingConfig](../api-setcdndomainstagingconfig.md) ，通过指定 ConfigId 更新配置项。 |
| 通过 ConfigId 删除配置项 | 调用 [DeleteSpecificConfig](../api-deletespecificconfig.md) 、 [DeleteSpecificStagingConfig](../api-deletespecificstagingconfig.md) ，通过指定 ConfigId 删除配置项。 |
