### API
共享资源发现
将资源发现共享给任意账户
使用业务账号的身份凭证，调用[CreateResourceShare](https://help.aliyun.com/zh/resource-management/resource-sharing/developer-reference/api-resourcesharing-2020-01-10-createresourceshare)创建共享单元，并确保将AllowExternalTargets参数设为True。
使用网络管理员的身份凭证，先调用[ListResourceShareInvitations](https://help.aliyun.com/zh/resource-management/resource-sharing/developer-reference/api-resourcesharing-2020-01-10-listresourceshareinvitations)查询收到的资源共享邀请，再调用[AcceptResourceShareInvitation](https://help.aliyun.com/zh/resource-management/resource-sharing/developer-reference/api-resourcesharing-2020-01-10-acceptresourceshareinvitation)接受共享。
仅在资源目录内共享资源发现
使用资源目录管理账号的身份凭证，调用[EnableSharingWithResourceDirectory](https://help.aliyun.com/zh/resource-management/resource-sharing/developer-reference/api-resourcesharing-2020-01-10-enablesharingwithresourcedirectory)启用资源目录组织共享。
使用业务账号的身份凭证，调用[CreateResourceShare](https://help.aliyun.com/zh/resource-management/resource-sharing/developer-reference/api-resourcesharing-2020-01-10-createresourceshare)创建共享单元，并确保将AllowExternalTargets参数设为True。
使用业务账号的身份凭证，调用[DeleteResourceShare](https://help.aliyun.com/zh/resource-management/resource-sharing/developer-reference/api-reso
