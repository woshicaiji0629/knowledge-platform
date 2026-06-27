### 处理引用后出现的条目冲突
在VPC路由表或TR路由表引用前缀列表后，若前缀列表变更导致与路由表已有条目冲突，那么最新变更不会生效。
您可在前缀列表基本信息的关联页签下，查看冲突详情：发生冲突的引用方其状态为未关联到最新版本。将鼠标悬浮停在该状态上，查看ErrorMessage获取冲突的具体条目。
您有2种方法解决冲突：
警告
操作前，请您确保要修改的路由条目不会影响业务。
修改前缀列表：在前缀列表中删除导致冲突的条目，删除后系统自动重新下发前缀列表至所有引用方。
修改路由表：在路由表中删除导致冲突的路由条目，然后手动重新下发前缀列表，直至状态由未关联到最新版本变为下发成功。
下面讲述手动重新下发前缀列表的步骤。
控制台
前往专有网络控制台[VPC](https://vpc.console.aliyun.com/vpc/cn-hangzhou/prefix-lists)[前缀列表](https://vpc.console.aliyun.com/vpc/cn-hangzhou/prefix-lists)页面。先在顶部菜单栏左上处选择目标地域，再单击目标前缀列表的实例ID。
切换到关联页签，找到目标引用方，单击操作列的重试。
API
调用[RetryVpcPrefixListAssociation](developer-reference/api-vpc-2016-04-28-retryvpcprefixlistassociation.md)重新下发前缀列表。
Terraform
在不修改前缀列表条目的情况下，Terraform暂不支持重新下发前缀列表。
