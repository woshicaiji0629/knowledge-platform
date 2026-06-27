## 前提条件
由于阿里云账号（主账号）拥有资源的所有权限，其AccessKey一旦泄露风险巨大，所以建议您使用满足最小化权限需求的RAM用户的AccessKey。具体操作方式请参见[创建](https://help.aliyun.com/zh/ram/user-guide/create-an-accesskey-pair)[AccessKey](https://help.aliyun.com/zh/ram/user-guide/create-an-accesskey-pair)。
给RAM用户授予操作云服务器ECS相关资源的权限。本文提供的示例代码为查询示例，所以选择AliyunECSReadonlyAccess系统权限策略，您在使用的时候可以根据业务需求进行自定义授权。
使用自定义权限策略。
关于如何创建自定义权限策略，请参见[创建自定义权限策略](https://help.aliyun.com/zh/ram/create-a-custom-policy#task-glf-vwf-xdb)和[授权信息](api-ecs-2014-05-26-ram.md)。
云服务器ECS依据最佳实践提供了一些自定义权限策略示例，您可以参考这些示例以快速创建符合自身业务需求的自定义权限策略，具体详情请参见[云服务器](../user-guide/custom-policies-for-ecs.md)[ECS](../user-guide/custom-policies-for-ecs.md)[自定义权限策略参考](../user-guide/custom-policies-for-ecs.md)。
使用系统权限策略。
云服务器ECS支持的所有系统权限策略及其对应的权限描述，请参见[云服务器 ECS](../user-guide/ecs.md)[系统权限策略参考](../user-guide/ecs.md)。
在环境变量中配置AccessKey，具体操作步骤请参见[在](https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems)[Linux、macOS](https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems)[和](https://help.aliyun.com/zh/sdk/developer-referenc
