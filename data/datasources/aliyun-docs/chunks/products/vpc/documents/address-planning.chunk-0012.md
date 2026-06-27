### 控制台
此处仅介绍将交换机共享给任意账户的方式。针对资源目录方式，请参考[仅在资源目录内共享资源](https://help.aliyun.com/zh/resource-management/resource-sharing/getting-started/share-resources-with-objects-in-a-resource-directory)。
共享 IPAM 地址池
使用地址池所有者账号，前往[IPAM](https://ipam.console.aliyun.com/cn-hangzhou/pool)[控制台 - IPAM](https://ipam.console.aliyun.com/cn-hangzhou/pool)[地址池](https://ipam.console.aliyun.com/cn-hangzhou/pool)，在页面上方选择目标地址池所在的地域。单击目标地址池实例ID或操作列的管理，在共享管理页签，单击创建资源共享。
在创建共享单元页面，按照步骤指引完成资源共享配置。
将资源修改为IPAM地址池，并选择要共享的IPAM地址池资源。
对于IPAM地址池资源，关联权限为AliyunRSDefaultPermissionIpamPool。
资源使用者范围选择允许共享给任意账号，添加方式选择手动添加，使用者ID输入地址池使用者的[阿里云账号](https://help.aliyun.com/zh/resource-management/resource-directory/support/how-do-i-view-the-id-of-an-alibaba-cloud-account)[ID](https://help.aliyun.com/zh/resource-management/resource-directory/support/how-do-i-view-the-id-of-an-alibaba-cloud-account)，并点击添加。
检查无误后，在页面底部单击确定。
登录地址池使用者的账号，接受共享邀请：
前往资源管理控制台的[资源共享-共享给我](https://resourcemanager.console.aliyun.com/resource-shares/cn-hangzhou/shared)页面。
在顶部菜单栏左上处，选择共享资源所在的地域，再单击目标共享单元状态列的接受。
共享成功后，地址池使用者可以在IPAM地址池页面共享给我的池页签中查看，可使用该地址池[结合](use-ipam-to-create-a-vpc.md)[IPAM](use-ipam-to-create-a-vpc.md)[规划并创建专有网络](use-ipam-to-create-a-vpc.md)或[结合]
