# 域名配置功能函数
调用BatchSetCdnDomainConfig、SetCdnDomainStagingConfig可批量配置域名功能，本文为您介绍该API可以配置哪些功能及功能参数用法。
说明
本文中介绍的功能均能够被以下接口引用：
生产环境：[BatchSetCdnDomainConfig](../api-batchsetcdndomainconfig.md)、[DescribeCdnDomainConfigs](../api-describecdndomainconfigs.md)、[BatchDeleteCdnDomainConfig](../api-batchdeletecdndomainconfig.md)和[DescribeCdnUserDomainsByFunc](../api-describecdnuserdomainsbyfunc.md)。
模拟环境：[SetCdnDomainStagingConfig](../api-setcdndomainstagingconfig.md)、[DescribeCdnDomainStagingConfig](../api-describecdndomainstagingconfig.md)、[RollbackStagingConfig](../api-rollbackstagingconfig.md)和[PublishStagingConfigToProduction](../api-publishstagingconfigtoproduction.md)。
调用BatchSetCdnDomainConfig、SetCdnDomainStagingConfig可以实现域名的批量配置，并生成唯一的ConfigId，通过ConfigId可以实现对指定配置的更新和删除。具体使用方法，请参见[ConfigId](usage-notes-on-configid.md)[使用说明](usage-notes-on-configid.md)。
