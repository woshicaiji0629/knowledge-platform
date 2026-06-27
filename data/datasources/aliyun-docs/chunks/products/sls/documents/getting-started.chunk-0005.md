## 创建Project和LogStore
Project是日志服务的资源管理单元，用于隔离不同项目的数据；LogStore是日志数据的存储单元。
登录[日志服务控制台](https://sls.console.aliyun.com)。
单击创建Project：
所属地域：选择与ECS实例相同的地域，即可通过阿里云内网采集日志，加快日志采集速度。
Project名称：输入一个在阿里云内全局唯一的名称，例如nginx-quickstart-abc。
[其他配置](manage-a-project.md)保持默认，单击创建。
在Project创建成功页面，单击创建Logstore。
输入Logstore名称（例如nginx-access-log），[其他配置](manage-a-logstore.md)无需修改，单击确定。
默认情况下创建的是[标准型](manage-a-logstore.md)，[按写入数据量计费](billing-overview.md)的LogStore 。
