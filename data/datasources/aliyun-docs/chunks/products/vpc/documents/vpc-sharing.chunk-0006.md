### 控制台
一、开启共享此处仅介绍将交换机共享给任意账户的方式。针对资源目录方式，请参考[仅在资源目录内共享资源](https://help.aliyun.com/zh/resource-management/resource-sharing/getting-started/share-resources-with-objects-in-a-resource-directory)。
登录交换机所有者的账号，前往资源管理控制台的[资源共享-我的共享](https://resourcemanager.console.aliyun.com/resource-shares/cn-hangzhou/owned)页面。先在顶部菜单栏左上处，选择共享资源所在的地域，再单击创建共享单元，在打开的页面中：
第一步：输入共享单元名称，然后选中需要共享的交换机。
第二步：系统会默认选择AliyunRSDefaultPermissionVSwitch权限。
第三步：资源使用者范围选择允许共享给任意账号，添加方式选择手动添加，使用者ID输入交换机使用者的[阿里云账号](https://help.aliyun.com/zh/resource-management/resource-directory/support/how-do-i-view-the-id-of-an-alibaba-cloud-account)[ID](https://help.aliyun.com/zh/resource-management/resource-directory/support/how-do-i-view-the-id-of-an-alibaba-cloud-account)，并点击添加。
第四步：检查无误后，在页面底部单击确定。
登录交换机使用者的账号，接受共享邀请：
前往资源管理控制台的[资源共享-共享给我](https://resourcemanager.console.aliyun.com/resource-shares/cn-hangzhou/shared)页面。
在顶部菜单栏左上处，选择共享资源所在的地域，再单击目标共享单元状态列的接受。
接受后，交换机使用者就可以访问共享的交换机，且后续该共享单元新增的共享资源将默认接受共享邀请。
二、在共享交换机创建云资源
登录交换机使用者的账号：
前往专有网络控制台[交换机](https://vpc.console.aliyun.com/vpc/cn-hangzhou/switches)页面，在顶部状态栏选择共享交换机的地域后，您可以看到共享交换机（被标记为来自共享）。
针对ECS、RDS、SLB实例，您可以在目标共享交换机的操作列，单击添加云产品进行创建。
其他[支持在共享交换机下创建的云资源类型](vpc-sharing.md)，请在创建
