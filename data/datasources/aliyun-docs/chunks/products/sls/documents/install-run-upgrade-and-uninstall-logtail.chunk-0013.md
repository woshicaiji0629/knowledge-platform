### 批量安装Logtail
批量安装Logtail有如下两种方式：
OOS编排：适合有权限要求场景，并发度较高，适合大规模批量操作。具体请参考[使用](best-practice-use-oos-to-batch-install-or-upgrade-logtail.md)[OOS](best-practice-use-oos-to-batch-install-or-upgrade-logtail.md)[批量安装或升级](best-practice-use-oos-to-batch-install-or-upgrade-logtail.md)[Logtail](best-practice-use-oos-to-batch-install-or-upgrade-logtail.md)。
ECS云助手功能：简单易用，直接通过命令的方式执行临时任务。具体操作步骤如下：
访问[ECS](https://ecs.console.aliyun.com/cloud-assistant/region)[控制台-云助手](https://ecs.console.aliyun.com/cloud-assistant/region)。
在页面左侧顶部，选择目标资源所在的资源组和地域。
在ECS 云助手页面右上角，单击创建/执行命令。
在创建执行命令面板中，命令内容输入安装命令（此处以公网安装方式为例，更多安装命令，请参见[安装](install-run-upgrade-and-uninstall-logtail.md)[Logtail](install-run-upgrade-and-uninstall-logtail.md)）。
此处用到的安装命令如下所示：
#!/bin/bash region_id='cn-hangzhou' wget http://logtail-release-${region_id}.oss-${region_id}.aliyuncs.com/linux64/logtail.sh -O logtail.sh chmod +x logtail.sh ./logtail.sh install ${region_id}-internet
重要
安装Logtail后，如果ECS的网络由经典网络切换至VPC，则需要更新Logtail配置。更多信息，请参见[ECS](update-a-logtail-configuration-after-i-switch-the-network-type-to-vpc.md)[经典网络切换为](update-a-logtail-configuration-after-i-switch-the-network-type-to-vpc.md)[VPC](update-a-logtail-configuration-after-
