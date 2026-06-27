### 控制台
此处仅介绍将交换机共享给任意账户的方式。针对资源目录方式，请参考[仅在资源目录内共享资源](https://help.aliyun.com/zh/resource-management/resource-sharing/getting-started/share-resources-with-objects-in-a-resource-directory)。
共享资源发现
业务账号将[创建的资源发现](use-ipam-to-create-a-vpc.md)共享给网络管理员：
前往[IPAM 控制台 - 资源发现](https://ipam.console.aliyun.com/cn-hangzhou/resource)，在页面上方选择目标资源发现所在地域。单击目标资源发现实例ID或操作列的管理，在共享管理页签，单击创建资源共享。
在创建共享单元页面，按照步骤指引完成资源共享配置。
将资源修改为IPAM资源发现，并选择要共享的IPAM资源发现。
对于IPAM资源发现，关联权限为AliyunRSDefaultPermissionIpamResourceDiscovery。
资源使用者范围选择允许共享给任意账号，添加方式选择手动添加，使用者ID输入地址池使用者的[阿里云账号](https://help.aliyun.com/zh/resource-management/resource-directory/support/how-do-i-view-the-id-of-an-alibaba-cloud-account)[ID](https://help.aliyun.com/zh/resource-management/resource-directory/support/how-do-i-view-the-id-of-an-alibaba-cloud-account)，并点击添加。
检查无误后，在页面底部单击确定。
登录网络管理员账号，接受共享邀请：
前往资源管理控制台的[资源共享-共享给我](https://resourcemanager.console.aliyun.com/resource-shares/cn-hangzhou/shared)页面。
在顶部菜单栏左上处，选择共享资源所在的地域，再单击目标共享单元状态列的接受。
共享成功后，网络管理员可分别查看各业务账号下的资源与地址利用率等信息。
网络管理员将共享的资源发现与托管地域一致的IPAM关联：
前往[IPAM 控制台 - IPAM](https://ipam.console.aliyun.com/cn-hangzhou/ipam)，在页面上方选择目标IPAM所在地域。单击目标IPAM实例ID或操作列的管理，在关联资源发现页签，单击关联资源发现，选择业务账号共享的资源发现。
关联完
