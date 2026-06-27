## 1. 开通容器服务并为角色授权
在创建ACK集群之前，您需要免费开通相应服务。如果您在创建ACK集群前没有开通容器服务ACK，可能会导致集群无法创建或创建失败。建议按照以下操作开通容器服务，并为容器服务默认角色授权。
开通容器服务ACK
首次开通容器服务ACK时，您需要登录[容器服务](https://common-buy.aliyun.com/?spm=5176.2020520152.0.0.75a361b1SJ9jQT&commodityCode=csk_propayasgo_public_cn)[ACK](https://common-buy.aliyun.com/?spm=5176.2020520152.0.0.75a361b1SJ9jQT&commodityCode=csk_propayasgo_public_cn)[开通页面](https://common-buy.aliyun.com/?spm=5176.2020520152.0.0.75a361b1SJ9jQT&commodityCode=csk_propayasgo_public_cn)，阅读并选中容器服务ACK服务协议，单击立即开通。
在集群类型区域选择ACK Pro版或ACK 基础版，选择ACK Pro版将同时开通ACK Pro版和ACK基础版。
角色授权
首次登录容器服务ACK时，为了您账号的ACK集群云资源的访问安全，您需要授权阿里云账号创建容器服务默认角色，授权该默认角色是为了确保ACK能够正常调用相关的云服务资源，从而实现集群的创建、管理和维护等功能。角色授权操作步骤如下。
登录[容器服务管理控制台](https://cs.console.aliyun.com)，然后单击前往RAM进行授权进入[访问控制快速授权](https://ram.console.aliyun.com/role/authorize?request=%7B%22ReturnUrl%22%3A%22https%3A%2F%2Fcs.console.aliyun.com%2F%22%2C%22Services%22%3A%5B%7B%22Roles%22%3A%5B%7B%22RoleName%22%3A%22AliyunCSManagedLogRole%22%2C%22TemplateId%22%3A%22AliyunCSManagedLogRole%22%7D%2C%7B%22RoleName%22%3A%22AliyunCSManagedCmsRole%22%2C%22TemplateId%22%3A%22AliyunCSManagedCmsRole%22%7D%2C%7B%22RoleName%22%3A%22AliyunCSManagedCsiRole%22%2C%22TemplateId%22%
