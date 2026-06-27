### 如何通过生命周期快速清理Bucket下的所有文件
Bucket未开启版本控制
对于未开启版本控制的Bucket，只需要配置一条生命周期规则，即可自动快速清理所有文件和碎片（Multipart Upload产生的未合并碎片）。
登录OSS管理控制台的[Bucket](https://oss.console.aliyun.com/bucket)[列表](https://oss.console.aliyun.com/bucket)页面，找到目标Bucket。
在左侧导航栏，选择数据安全>版本控制，确认Bucket未开启版本控制。
在左侧导航栏，选择数据管理>生命周期，设置生命周期规则，指定Bucket内所有文件在最后一次修改后1天自动删除，同时对生成时间早于1天的文件碎片，自动执行清理操作。
Bucket已开启版本控制
Bucket开启版本控制后，会产生当前版本文件、历史版本文件、碎片文件和删除标记。只需要配置一条生命周期规则，即可自动快速清理这些文件。
登录OSS管理控制台的[Bucket](https://oss.console.aliyun.com/bucket)[列表](https://oss.console.aliyun.com/bucket)页面，找到目标Bucket。
在左侧导航栏，选择数据安全>版本控制，确认Bucket已开启版本控制。
在左侧导航栏，选择数据管理>生命周期，设置生命周期规则，指定Bucket内所有当前版本、历史版本文件在最后一次修改后1天自动删除，同时对生成时间早于1天的文件碎片，自动执行清理操作。该规则会同步清理删除标记。
