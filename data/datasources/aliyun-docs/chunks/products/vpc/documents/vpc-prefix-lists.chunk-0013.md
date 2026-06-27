### 控制台
开启共享此处仅介绍将前缀列表共享给任意账户的方式。针对资源目录方式，请参考[仅在资源目录内共享资源](https://help.aliyun.com/zh/resource-management/resource-sharing/getting-started/share-resources-with-objects-in-a-resource-directory)。
登录前缀列表所有者的账号，前往资源管理控制台的[资源共享-我的共享](https://resourcemanager.console.aliyun.com/resource-shares/cn-hangzhou/owned)页面。先在顶部菜单栏左上处，选择共享资源所在的地域，再单击创建共享单元，在打开的页面中：
第一步：输入共享单元名称，在资源面板的下拉列表中选择VPC前缀列表，然后选中需要共享的前缀列表。
第二步：系统会默认选择AliyunRSDefaultPermissionPrefixList权限。
第三步：资源使用者范围选择允许共享给任意账号，添加方式选择手动添加，使用者ID输入前缀列表使用者的[阿里云账号](https://help.aliyun.com/zh/resource-management/resource-directory/support/how-do-i-view-the-id-of-an-alibaba-cloud-account)[ID](https://help.aliyun.com/zh/resource-management/resource-directory/support/how-do-i-view-the-id-of-an-alibaba-cloud-account)，并点击添加。
第四步：检查无误后，在页面底部单击确定。
登录前缀列表使用者的账号，接受共享邀请：
前往资源管理控制台的[资源共享-共享给我](https://resourcemanager.console.aliyun.com/resource-shares/cn-hangzhou/shared)页面。
在顶部菜单栏左上处，选择共享资源所在的地域，再单击目标共享单元状态列的接受。
接受后，使用者就可以访问共享的前缀列表，且后续该共享单元新增的共享资源将默认接受共享邀请。
前往专有网络控制台VPC前缀列表页面，在顶部菜单栏选择共享前缀列表所在的地域后，您可以看到收到的前缀列表（拥有者列被标记为来自共享）。
接下来您可以参考[引用前缀列表](vpc-prefix-lists.md)，在VPC路由表、TR路由表、ECS安全组中进行引用。
管理共享前缀列表和使用者
前缀列表所有者可参考如下步骤，查看或增删共享前缀列表及其使用者。
登录前缀列表所有者的账号，前往资源管理控制台的[
