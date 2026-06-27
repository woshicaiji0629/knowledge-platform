## Bucket 拥有者配置请求者付费
步骤一：开启请求者付费
登录[OSS](https://oss.console.aliyun.com/)[管理控制台](https://oss.console.aliyun.com/)。
单击Bucket 列表，然后单击目标Bucket名称。
在左侧导航栏，选择Bucket 配置>请求者付费。
在请求者付费页面，打开请求者付费开关。
在弹出的对话框，单击确定。
步骤二：为请求者授予访问权限
通过 Bucket Policy 为请求者授权访问，否则请求者将无法访问数据。
在[Bucket](https://oss.console.aliyun.com/bucket/)[列表](https://oss.console.aliyun.com/bucket/)，单击目标Bucket名称。
在左侧导航栏，选择权限控制>Bucket 授权策略。
在Bucket 授权策略页面的按图形策略添加页签，单击新增授权。
在新增授权面板，填写授权策略。其中，授权用户选择其他账号，填写请求者的账号ID或RAM角色ARN（格式为arn:sts::{RoleOwnerUid}:assumed-role/{RoleName}/{RoleSessionName}）。
单击确定。
