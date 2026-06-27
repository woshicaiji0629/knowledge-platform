## OpenAPI方式
使用[RunInstances](../developer-reference/api-ecs-2014-05-26-runinstances.md)创建ECS实例时，通过PrivatePoolOptions.MatchCriteria参数设置实例的私有池类型。
Open：开放模式。将自动匹配开放类型的私有池容量。如果没有符合条件的私有池容量，则使用公共池资源启动。该模式下无需设置PrivatePoolOptions.Id参数。
Target：指定模式。使用指定的私有池容量启动实例，如果该私有池容量不可用，则实例会启动失败。该模式下必须指定私有池 ID，即PrivatePoolOptions.Id参数为必填项。
None：不使用模式。实例启动将不使用私有池容量。
