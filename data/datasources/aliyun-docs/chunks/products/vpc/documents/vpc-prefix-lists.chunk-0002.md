### 控制台
创建前缀列表
前往专有网络控制台[VPC](https://vpc.console.aliyun.com/vpc/cn-hangzhou/prefix-lists)[前缀列表](https://vpc.console.aliyun.com/vpc/cn-hangzhou/prefix-lists)页面。先在顶部菜单栏左上处选择目标地域，再单击创建VPC前缀列表。
在创建VPC前缀列表面板中：
选择IP版本（IPv4/IPv6）。
设置最大条目数：该数值会占用VPC路由表和安全组的配额，创建后可修改。
例如，即使前缀列表实际只包含20个条目，但只要最大条目数设置为50，在VPC路由表或安全组中引用时，仍会占用50条路由或50条安全组规则的配额。
配额参考：单个VPC路由表支持的自定义路由条目数[默认为](understanding-vpc-quotas-in-alibaba-cloud.md)[200](understanding-vpc-quotas-in-alibaba-cloud.md)，单个安全组支持的规则数[默认为](../../ecs/documents/user-guide/security-faq.md)[200](../../ecs/documents/user-guide/security-faq.md)。
配置前缀列表条目，支持逐条录入、批量录入、从其他前缀列表克隆（支持跨地域克隆，但不支持从来自共享的前缀列表或系统前缀列表进行克隆）。
增加或删除条目
在目标前缀列表的基本信息的条目页签下：
增加条目：单击创建VPC前缀列表条目。
删除条目：在目标条目的操作列单击删除，或多选后单击批量删除。
查看引用前缀列表的资源
在目标前缀列表的基本信息页面，单击关联页签查看。
删除前缀列表
在目标前缀列表的操作列或详情页单击删除。
删除前，请确保前缀列表未被其他资源引用，且未被共享。
