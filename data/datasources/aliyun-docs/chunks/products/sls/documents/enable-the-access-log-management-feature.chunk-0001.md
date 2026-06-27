## 操作步骤
重要
如果您使用RAM用户开通访问日志功能，则需先为RAM用户授权。具体操作，请参见[RAM](common-operations-on-logs-of-alibaba-cloud-services.md)[用户授权](common-operations-on-logs-of-alibaba-cloud-services.md)。
登录[负载均衡控制台](https://slb.console.aliyun.com/slb)负载均衡控制台。
在页面左上角，选择地域。
在左侧导航栏，选择传统型负载均衡CLB>日志管理>访问日志。
根据页面提示，授权传统型负载均衡使用AliyunLogArchiveRole角色访问日志服务。
该操作仅在首次配置时需要，且需要由阿里云账号完成。
警告
请勿取消授权或删除AliyunLogArchiveRole角色，否则将导致日志无法正常推送到日志服务。
在访问日志（7层）页面，单击目标实例右侧的设置。
在日志设置页面，选择可用的项目Project和日志库LogStore，并单击确定。
配置完成后，日志服务默认为该LogStore创建索引。如果LogStore已有索引，则原有索引将被覆盖。
