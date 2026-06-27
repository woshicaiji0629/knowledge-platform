## API
调用[ModifyInstanceMetadataOptions](../developer-reference/api-ecs-2014-05-26-modifyinstancemetadataoptions.md)，设置HttpEndpoint=enabled、HttpTokens=required切换实例元数据访问模式为仅加固模式。
切换完成后，建议持续监控实例的元数据访问情况和应用运行状态，确保业务平稳运行，避免因遗漏改造的应用而导致服务中断。若出现异常，建议先切换回普通模式和加固模式，优先恢复业务，然后重新进一步[步骤一：排查并升级代码及依赖项](view-instance-metadata.md)。
