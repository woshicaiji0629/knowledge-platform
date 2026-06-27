网域名时，不会产生外网读取流量费用。 | 当 Project 在华东 2（上海）地域时，不会产生外网读取流量费用。 | 部署在与 Project 相同地域的 ECS 上且使用日志服务私网域名时，不会产生外网读取流量费用。 |
| NAS 集成 | 无 | 无 | 必要时，手动配置 | 自动配置 | 必要时，手动配置 |

您也可以将日志投递到OSS，通过OSS进行下载。关于投递的具体操作，请参见[创建](create-oss-shipping-tasks-new-version.md)[OSS](create-oss-shipping-tasks-new-version.md)[投递任务（新版）](create-oss-shipping-tasks-new-version.md)。
下载权限配置（点击查看）
{ "Version": "1", "Statement": [ { "Action": [ "log:ListDownloadJobs", "log:CreateDownloadJob", "log:GetDownloadJob", "log:DeleteDownloadJob" ], "Resource": [ "acs:log:*:*:project/Project名称/downloadjob/*" ], "Effect": "Allow" } ] }
