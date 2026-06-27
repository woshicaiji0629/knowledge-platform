### Cloud Lens服务日志
注意事项
警告
CloudLens功能要求云账号下必须存在至少一个Project。
在用户开通和使用CloudLens功能时，日志服务会检测账号下是否存在Project，具体逻辑如下。
检测逻辑
用户第一次开通CloudLens功能，日志服务会自动检测您当前的阿里云账号下是否存在任意Project，如果没有Project，则会在华南2（河源）地域创建一个名称为aliyun-product-data-阿里云账号ID-cn-heyuan的Project。
用户开通CloudLens功能后进入CloudLens，日志服务只会自动检测您当前的阿里云账号下是否存在任意Project，不会在华南2（河源）地域创建Project，用户可以手动创建任意Project，创建Project的步骤请参见[管理](manage-a-project.md)[Project](manage-a-project.md)。
删除Project
如果您要删除aliyun-product-data-阿里云账号ID-cn-heyuan这个Project，可以打开[云命令行](https://shell.aliyun.com/)，执行以下命令进行删除，请根据实际情况替换阿里云账号ID。
aliyunlog log delete_project --project_name=aliyun-product-data-阿里云账号ID-cn-heyuan --region-endpoint=cn-heyuan.log.aliyuncs.com
删除其他Project和LogStore的步骤，请参见[管理](manage-a-logstore.md)[LogStore](manage-a-logstore.md)和[管理](manage-a-project.md)[Project](manage-a-project.md)。
