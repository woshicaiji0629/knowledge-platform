## 配置ossfs 2.0
在实际使用过程中，为满足不同场景下对存储空间（OSS Bucket）的挂载需求，需对ossfs 2.0配置文件进行针对性配置，然后在挂载存储空间（OSS Bucket）时，引用该配置文件即可完成挂载。
[创建拥有](../../../ram/documents/create-an-accesskey-pair-1.md)[OSS](../../../ram/documents/create-an-accesskey-pair-1.md)[管理权限的](../../../ram/documents/create-an-accesskey-pair-1.md)[RAM](../../../ram/documents/create-an-accesskey-pair-1.md)[用户](../../../ram/documents/create-an-accesskey-pair-1.md)[AccessKey](../../../ram/documents/create-an-accesskey-pair-1.md)。
通过ROS脚本快速创建具备OSS管理权限的RAM用户及其AccessKey
在资源编排ROS控制台的[创建资源栈](https://ros.console.aliyun.com/cn-hangzhou/stacks/create?templateUrl=https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20241114/itgrlo/createossadmin.yaml&step=1&hideTemplateSelector=false)页面的安全确认下，勾选确认，然后单击创建。
创建完成后，在输出中复制新创建的AccessKey。
输出关键字包括AccessKeyId和AccessKeySecret，分别复制对应的值。
配置用于访问对象存储OSS的凭证环境变量。
export OSS_ACCESS_KEY_ID=LTAI****************** export OSS_ACCESS_KEY_SECRET=8CE4**********************
您可按需自由设定ossfs 2.0配置文件的文件名与路径。例如，创建/etc/ossfs2.conf文件作为配置文件。
sudo touch /etc/ossfs2.conf
填写挂载信息。以只读方式挂载整个Bucket的配置为例。
说明
查看Bucket的Endpoint请进入[Bucket](https://oss.console.aliyun.com/bucket)[列表](https://oss.console.aliyun.com/bucket)页面，选择
