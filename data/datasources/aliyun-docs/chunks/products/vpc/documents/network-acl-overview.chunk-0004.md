### 控制台
创建网络ACL
前往[专有网络控制台-网络](https://vpc.console.aliyun.com/nacl/cn-hangzhou/nacls)[ACL](https://vpc.console.aliyun.com/nacl/cn-hangzhou/nacls)，在页面上方选择目标地域后，单击创建网络ACL。
配置所属专有网络，需选择计划与网络ACL关联的交换机所属的VPC。
关联交换机
单击实例ID或操作列的管理，进入已绑定资源页签，单击关联交换机，选择一个或多个目标交换机并确定关联。关联的交换机将按照网络ACL规则控制出入交换机的流量。如需解除控制，您可以在该页签下，单击目标交换机操作列的解绑。
您也可以在目标交换机详情页的网络ACL参数项，绑定、更换或解绑网络ACL。
删除网络ACL
需先确保已解除与交换机的关联。在目标网络ACL的操作列，单击删除。
