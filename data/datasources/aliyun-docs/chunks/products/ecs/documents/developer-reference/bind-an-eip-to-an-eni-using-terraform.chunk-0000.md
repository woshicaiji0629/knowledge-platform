# 通过Terraform为弹性网卡绑定EIP
弹性公网IP（Elastic IP Address）是可以独立购买和持有的公网IP地址资源，当EIP和云资源绑定后，云资源可以通过EIP与公网通信。例如在单个ECS实例上托管多个应用时，可以通过为每个应用分配独立的辅助弹性网卡并绑定独立的弹性公网IP（EIP），实现每个应用对外呈现一个独立的公网IP地址。本文将为您介绍如何为辅助弹性网卡绑定弹性公网IP。
说明
本教程所含示例代码支持一键运行，您可以直接运行代码。[一键运行](https://api.aliyun.com/terraform?spm=api-workbench.home.0.0.5f4de85cHYWAyq&provider=1.246.0&product=ECS&resource=alicloud_auto_provisioning_group&example=201-use-case-bind-eip-to-ecs-eni&activeTab=code)
