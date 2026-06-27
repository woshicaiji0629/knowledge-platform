## 检查必须删除的资源
如果Bucket中残留文件、碎片、接入点、加速器或RTMP推流地址等一种或多种必须删除的资源没有清理，在删除 Bucket 时将出现“存储空间不为空”的报错。建议使用 OSS 控制台删除向导，可自动扫描并列出所有待清理项。
登录[OSS](https://oss.console.aliyun.com/)[管理控制台](https://oss.console.aliyun.com/)。
单击Bucket 列表，然后单击目标Bucket名称。
下滑左侧导航栏至底部，单击删除Bucket。
在删除Bucket页面，可以看到检测出的待清理项。
