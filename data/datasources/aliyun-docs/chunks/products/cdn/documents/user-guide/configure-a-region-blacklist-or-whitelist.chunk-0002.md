## 配置示例
封禁来自安道尔的以HTTP协议访问/image路径的请求。
在[规则引擎](rules-engine.md)中配置如下规则：以HTTP协议访问/image路径的资源。
规则名称设置为rule，条件为协议类型等于http并且URI包含其中任意一个/image/*，单击提交完成配置。
在区域封禁中设置封禁规则：封禁来自安道尔的以HTTP协议访问/image路径的请求。
规则条件：选择步骤1创建的规则。
封禁类型：选择黑名单。
区域设置：选择安道尔。
封禁效果：当请求命中规则时，会出现403 Forbidden，并且提示denied by region block。
403 Forbidden You don't have permission to access the URL on this server. denied by region block Powered by Tengine CDN Request Id: dcbxxx5555e
该文章对您有帮助吗？
反馈
