# 如何在Linux系统安装LoongCollector-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/loongcollector-installation-linux

# 安装采集器
LoongCollector是日志服务提供的采集器。采集Linux服务器上的日志需要先在服务器上安装LoongCollector客户端，请根据服务器与日志服务Project的关系选择合适的安装方式。
## 使用限制
支持的Linux系统版本
支持如下版本的Linux x86-64（64位）服务器。
Alibaba Cloud Linux 2、3
Anolis OS 7、8
CentOS Linux 6、7、8
Debian GNU/Linux 8、9、10、11、12
RedHat Enterprise 6、7、8、9
OpenSUSE 15.1、15.2、42.3
SUSE Linux Enterprise Server 11、12、15
Ubuntu 14.04、16.04、18.04、20.04、22.04、24.0
其他基于glibc 2.6及以上版本的Linux操作系统
CPU支持sse4_2和avx指令集
支持如下版本的Linux ARM（64位）服务器。
Alibaba Cloud Linux 3.2 ARM版
Anolis OS 8.2 ARM版及以上版本
CentOS 8.4 ARM版
Debian 11.2、12.2 ARM版
Ubuntu 20.04、22.04、24.04 ARM版
CPU架构要求最低为ARMv8.2-A
## 前提条件
权限须知
如果您使用阿里云主账号登录，默认拥有所有操作权限，可直接进行相关操作。
若您使用RAM用户登录，请根据需要向主账号使用者申请如下系统策略以获得管理日志服务、ECS与OOS资源的权限。
AliyunLogFullAccess：授予管理日志服务的权限。
AliyunOOSFullAccess：授予管理OOS的权限，可执行OOS自动编排安装loongcollector。
AliyunECSFullAccess：授予管理ECS的权限，可执行ECS云助手命令批量安装loongcollector。
当系统策略无法满足您的需求，您可以参考下表通过[创建自定义权限策略](../../ram/documents/create-a-custom-policy.md)实现精细化权限管理。
请将Resource中的${projectName}替换为您需要访问的Project名称。{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": [ "ecs:DescribeTagKeys", "ecs:DescribeTags", "ecs:DescribeInstances", "ecs:DescribeInvocationResults", "ecs:RunCommand", "ecs:DescribeInvocations", "ecs:InvokeCommand" ], "Resource": "*" }, { "Effect": "Allow", "Action": [ "oos:ListTemplates", "oos:StartExecution", "oos:ListExecutions", "oos:GetExecutionTemplate", "oos:ListExecutionLogs", "oos:ListTaskExecutions" ], "Resource": "*" }, { "Effect": "Allow", "Action": [ "log:ListProject", "log:GetAcceleration", "log:ListDomains", "log:GetLogging", "log:ListTagResources" ], "Resource": [ "acs:log:*:*:project/*" ] }, { "Effect": "Allow", "Action": [ "log:GetProject" ], "Resource": [ "acs:log:*:*:project/${projectName}" ] }, { "Effect": "Allow", "Action": [ "log:ListLogStores", "log:GetLogStore", "log:GetLogStoreHistogram", "log:GetIndex", "log:CreateIndex", "log:UpdateIndex", "log:ListShards", "log:GetCursorOrData", "log:ListSavedSearch", "log:GetLogStoreLogs", "log:ListDashboard", "log:GetLogStoreContextLogs" ], "Resource": [ "acs:log:*:*:project/${projectName}/*" ] }, { "Effect": "Allow", "Action": [ "log:*" ], "Resource": [ "acs:log:*:*:project/${projectName}/logtailconfig/*", "acs:log:*:*:project/${projectName}/machinegroup/*" ] } ] }
创建Project
若您无可用Project，请参考此处步骤创建一个基础Project，如需详细了解创建配置请参见[管理](manage-a-project.md)[Project](manage-a-project.md)。
登录[日志服务控制台](https://sls.console.aliyun.com)，单击创建Project完成下述基础配置，其他配置保持默认即可：
所属地域：请根据日志来源等信息选择合适的阿里云地域，创建后不可修改。
Project名称：设置名称，名称在阿里云地域内全局唯一，创建后不可修改。
创建LogStore
若您无可用LogStore，请参考此处步骤创建一个基础LogStore，如需详细了解创建配置请参见[管理](manage-a-logstore.md)[LogStore](manage-a-logstore.md)。
登录[日志服务控制台](https://sls.console.aliyun.com)，在Project列表中单击目标Project。
在日志存储的日志库页签中，单击+图标。
填写Logstore名称，其余配置保持默认无需修改。
服务器网络要求
安装LoongCollector的机器需在出口方向开放80（HTTP）端口和443（HTTPS）端口，供LoongCollector上传数据。
安装LoongCollector的机器至少需要保证能够连通下列地址：
登录[日志服务控制台](https://sls.console.aliyun.com)，在Project列表中，单击目标Project。
单击Project名称右侧的进入项目概览页面。
在访问域名中可查看当前Project的域名信息，替换后执行命令。
当安装方式选择：[同账号同地域](loongcollector-installation-linux.md)、[不同账号同地域](loongcollector-installation-linux.md)时，数据传输方式为内网传输，替换${project名称}为Project名称，${域名信息}为私网域名。
当安装方式选择：[同账号不同地域](loongcollector-installation-linux.md)、[其他云/自建服务器](loongcollector-installation-linux.md)时，数据传输方式为公网传输，替换${project名称}为Project名称，${域名信息}为公网域名。
curl https://${project名称}.${域名信息}
返回类似信息{"Error":{"Code":"OLSInvalidMethod","Message":"The script name is invalid : /","RequestId":"5D****09"}}，说明网络畅通。否则检查目标地址是否被拦截以及其他网络方面的检查（例如DNS配置、安全组等）。
返回Error信息是因为访问链接缺少必要参数。当前测试仅验证网络连通性，未使用完整链接，因此在网络正常的情况下会显示Error的提示信息。
## 选择合适的安装方式
| 安装方式 | 适用场景 |
| --- | --- |
| [同账号同地域](loongcollector-installation-linux.md) | 仅当服务器为阿里云 ECS，且 ECS 与 Project 属于同一个阿里云账号，所属 [地域](loongcollector-installation-linux.md) 也相同时适用。 |
| [同账号不同地域](loongcollector-installation-linux.md) | 当服务器为阿里云 ECS，且 ECS 与 Project 属于同一个阿里云账号，但不属于同一个 [地域](loongcollector-installation-linux.md) 时适用。 |
| [不同账号同地域](loongcollector-installation-linux.md) | 当服务器为阿里云 ECS，且 ECS 与 Project 属于同一个 [地域](loongcollector-installation-linux.md) ，但不属于同一个阿里云账号时适用。 |
| [其他云/自建服务器](loongcollector-installation-linux.md) | 当服务器不是阿里云 ECS，例如自建服务器或其他云服务器时适用。 当服务器为阿里云 ECS，但 ECS 与 Project 不属于同一个阿里云账号，也不在同一个 [地域](loongcollector-installation-linux.md) 时，可视为自建服务器。 |
### 同账号同地域
仅当服务器为阿里云ECS，且ECS与Project属于同一个阿里云账号，所属[地域](loongcollector-installation-linux.md)也相同时，日志服务可一键在ECS中安装LoongCollector，借助OOS编排能力，无需登录ECS手动执行安装步骤。
一键安装能力已集成到日志服务的接入模板中，日志服务提供了正则、单行、多行等多种文本日志接入模板，各模板之间仅[处理插件](processing-plug-ins.md)不同；模板内支持添加、删除处理插件。请根据采集日志的特点选择模板，或任意选择文本日志模板后再根据日志特点进行处理插件配置。
具体操作如下：
登录[日志服务控制台](https://sls.console.aliyun.com/)，在Project列表中，单击目标Project。
单击日志存储，在日志库中单击目标LogStore前的，展开LogStore。
单击数据接入后的，在弹框中选择单行 - 文本日志接入模板，单击立即接入。
单击创建机器组，选择与Project同地域的ECS实例后（可选择多台ECS实例），单击安装并创建为机器组。
等待安装完成，填写名称后即可单击确定。若无法安装成功，请单击重建安装任务，并重新选择ECS，选择时需确认ECS地域与Project地域相同。
单击下一步，如果心跳为FAIL，单击自动重试后等待两分钟左右直到心跳变为OK。
至此一键安装完成。单击下一步，将进行[采集配置](host-text-log-collection-auto-install.md)。
### 同账号不同地域
当服务器为阿里云ECS，且ECS与Project属于同一个阿里云账号，但不属于同一个[地域](loongcollector-installation-linux.md)，此时需要手动下载安装包，并在安装命令中使用[公网传输方式或传输加速](loongcollector-installation-linux.md)。
具体操作如下：
下载安装包：在服务器上执行下载命令，示例代码中${region_id}可使用cn-hangzhou替换，若想加快安装包下载速度，请参考[RegionID](loongcollector-installation-linux.md)替换${region_id}为ECS所属地域。
wget https://aliyun-observability-release-${region_id}.oss-${region_id}.aliyuncs.com/loongcollector/linux64/latest/loongcollector.sh -O loongcollector.sh;
选择传输方式并执行安装命令：替换${region_id}为Project所属地域的[RegionID](loongcollector-installation-linux.md)。
公网：适用于大多数场景，常见于跨地域或其他云/自建服务器，但受带宽限制且可能不稳定。
chmod +x loongcollector.sh; ./loongcollector.sh install ${region_id}-internet
传输加速：用于跨地域（如中国内地到海外），通过CDN加速提升性能，避免公网延迟高，传输不稳定问题，但流量需额外计费。
需要先打开Project的[日志跨域传输加速](manage-a-project.md)功能，再执行安装命令。chmod +x loongcollector.sh; ./loongcollector.sh install ${region_id}-acceleration
查看启动状态：执行命令，返回loongcollector is running表示启动成功。
sudo /etc/init.d/loongcollectord status
配置机器组：日志服务通过机器组发现用户自定义标识并与主机上的LoongCollector建立心跳连接。
在服务器上将自定义字符串user-defined-test-1写入用户自定义标识文件，该字符串将在后续步骤中使用。
#向指定文件写入自定义字符串，若目录不存在需手动创建。文件路径和名称由日志服务固定，不可自定义。 echo "user-defined-test-1" > /etc/ilogtail/user_defined_id
登录[日志服务控制台](https://sls.console.aliyun.com/)。在Project列表中，单击目标Project。
单击资源，单击机器组。
单击机器组右侧的，单击创建机器组。
进行如下配置后单击确定。
设置机器组名称：名称Project内唯一，必须以小写字母或数字开头和结尾，且只能包含小写字母、数字、连字符（-）和下划线（_），长度为3~128字符。
机器组标识：选择用户自定义标识。
用户自定义标识：输入配置的用户自定义标识，需要与服务器用户自定义标识文件中自定义字符串内容一致。此例为user-defined-test-1。
机器组创建完成后，在机器组列表单击目标机器组，在机器组状态中查看心跳状态，若为FAIL，请等待两分钟左右并手动刷新。如果心跳为OK则表示创建成功。
安装完成后若需要采集日志还需进行[采集配置](host-text-log-collection-auto-install.md)。
### 不同账号同地域
当服务器为阿里云ECS，且ECS与Project属于同一个[地域](loongcollector-installation-linux.md)，但不属于同一个阿里云账号时，需要手动下载安装包，并在安装命令中使用[内网传输方式](loongcollector-installation-linux.md)，且需要配置用户ID。
具体操作如下：
下载安装包：在服务器上执行下载命令，示例代码中${region_id}可使用cn-hangzhou替换，若想加快安装包下载速度，请参考[RegionID](loongcollector-installation-linux.md)替换${region_id}为ECS所属地域。
wget https://aliyun-observability-release-${region_id}.oss-${region_id}.aliyuncs.com/loongcollector/linux64/latest/loongcollector.sh -O loongcollector.sh;
执行安装命令：${region_id}需替换为Project所属地域的[RegionID](loongcollector-installation-linux.md)。
若发生连接超时，可能是${region_id}替换错误，不同地域内网传输无法建立连接，因而超时。需修改后重新执行安装命令。chmod +x loongcollector.sh; ./loongcollector.sh install ${region_id}
查看启动状态：执行命令，返回loongcollector is running表示启动成功。
sudo /etc/init.d/loongcollectord status
配置用户ID：用户ID文件包含Project所属阿里云主账号的ID信息，用于标识该账号有权限访问、采集这台服务器的日志。
只有在采集非本账号ECS、自建服务器、其他云厂商服务器日志时需要配置用户ID。多个账号对同一台服务器进行日志采集时，支持在同一台服务器上创建多个用户ID文件。
登录[日志服务控制台](https://sls.console.aliyun.com/)，鼠标悬浮在右上角用户头像上，在弹出的标签页中查看并复制账号ID。注意需要复制主账号ID。
在安装了LoongCollector的服务器上，以主账号ID作为文件名，创建用户ID文件。
touch /etc/ilogtail/users/{阿里云账号ID} # 如果/etc/ilogtail/users目录不存在，请手动创建目录。用户ID文件只需配置文件名，无需配置文件后缀。
配置机器组：日志服务通过机器组发现用户自定义标识并与主机上的LoongCollector建立心跳连接。
在服务器上将自定义字符串user-defined-test-1写入用户自定义标识文件，该字符串将在后续步骤中使用。
#向指定文件写入自定义字符串，若目录不存在需手动创建。文件路径和名称由日志服务固定，不可自定义。 echo "user-defined-test-1" > /etc/ilogtail/user_defined_id
登录[日志服务控制台](https://sls.console.aliyun.com/)。在Project列表中，单击目标Project。
单击资源，单击机器组。
单击机器组右侧的，单击创建机器组。单击右上角的四格图标，在下拉菜单中选择创建机器组。
进行如下配置后单击确定。
设置机器组名称：名称Project内唯一，必须以小写字母或数字开头和结尾，且只能包含小写字母、数字、连字符（-）和下划线（_），长度为3~128字符。
机器组标识：选择用户自定义标识。
用户自定义标识：输入配置的用户自定义标识，需要与服务器用户自定义标识文件中自定义字符串内容一致。此例为user-defined-test-1。
机器组创建完成后，在机器组列表单击目标机器组，在机器组状态中查看心跳状态，若为FAIL，请等待两分钟左右并手动刷新。如果心跳为OK则表示创建成功。
安装完成后若需要采集日志还需进行[采集配置](host-text-log-collection-auto-install.md)。
### 其他云/自建服务器
当服务器是其他云服务器或自建服务器时（若服务器为阿里云ECS，但ECS与Project不属于同一个阿里云账号，也不在同一个[地域](loongcollector-installation-linux.md)时，也可视为自建服务器），需要手动下载安装包，并在安装命令中使用[公网传输方式或传输加速](loongcollector-installation-linux.md)，且需要配置用户ID。
说明
服务器使用限制请参考[支持的](loongcollector-installation-linux.md)[Linux](loongcollector-installation-linux.md)[系统版本](loongcollector-installation-linux.md)。
具体操作如下：
下载安装包：在服务器上执行下载命令，示例代码中${region_id}可使用cn-hangzhou替换，若想加快安装包下载速度，请参考[RegionID](loongcollector-installation-linux.md)替换${region_id}为ECS所属地域。
wget https://aliyun-observability-release-${region_id}.oss-${region_id}.aliyuncs.com/loongcollector/linux64/latest/loongcollector.sh -O loongcollector.sh;
选择传输方式并执行安装命令：替换${region_id}为Project所属地域的[RegionID](loongcollector-installation-linux.md)。
公网：适用于大多数场景，常见于跨地域或其他云/自建服务器，但受带宽限制且可能不稳定。
chmod +x loongcollector.sh; ./loongcollector.sh install ${region_id}-internet
传输加速：用于跨地域（如中国内地到海外），通过CDN加速提升性能，避免公网延迟高，传输不稳定问题，但流量需额外计费。
需要先打开Project的[日志跨域传输加速](manage-a-project.md)功能，再执行安装命令。chmod +x loongcollector.sh; ./loongcollector.sh install ${region_id}-acceleration
查看启动状态：执行命令，返回loongcollector is running表示启动成功。
sudo /etc/init.d/loongcollectord status
配置用户ID：用户ID文件包含Project所属阿里云主账号的ID信息，用于标识该账号有权限访问、采集这台服务器的日志。
只有在采集非本账号ECS、自建服务器、其他云厂商服务器日志时需要配置用户ID。多个账号对同一台服务器进行日志采集时，支持在同一台服务器上创建多个用户ID文件。
登录[日志服务控制台](https://sls.console.aliyun.com/)，鼠标悬浮在右上角用户头像上，在弹出的标签页中查看并复制账号ID。注意需要复制主账号ID。
在安装了LoongCollector的服务器上，以主账号ID作为文件名，创建用户ID文件。
touch /etc/ilogtail/users/{阿里云账号ID} # 如果/etc/ilogtail/users目录不存在，请手动创建目录。用户ID文件只需配置文件名，无需配置文件后缀。
配置机器组：日志服务通过机器组发现用户自定义标识并与主机上的LoongCollector建立心跳连接。
在服务器上将自定义字符串user-defined-test-1写入用户自定义标识文件，该字符串将在后续步骤中使用。
#向指定文件写入自定义字符串，若目录不存在需手动创建。文件路径和名称由日志服务固定，不可自定义。 echo "user-defined-test-1" > /etc/ilogtail/user_defined_id
登录[日志服务控制台](https://sls.console.aliyun.com/)。在Project列表中，单击目标Project。
单击资源，单击机器组。
单击机器组右侧的，单击创建机器组。
进行如下配置后单击确定。
设置机器组名称：名称Project内唯一，必须以小写字母或数字开头和结尾，且只能包含小写字母、数字、连字符（-）和下划线（_），长度为3~128字符。
机器组标识：选择用户自定义标识。
用户自定义标识：输入配置的用户自定义标识，需要与服务器用户自定义标识文件中自定义字符串内容一致。此例为user-defined-test-1。
机器组创建完成后，在机器组列表单击目标机器组，在机器组状态中查看心跳状态，若为FAIL，请等待两分钟左右并手动刷新。如果心跳为OK则表示创建成功。
安装完成后若需要采集日志还需进行[采集配置](host-text-log-collection-auto-install.md)。
## 批量安装LoongCollector
ECS与Project同账号同地域场景下，自动安装功能中支持选择多台ECS。
其余场景下需借助ECS云助手来直接通过命令的方式执行临时任务，实现在ECS机器中批量执行LoongCollector安装命令的功能。
下载与安装命令请参考上述安装场景选择，如何使用ECS云助手请参考[创建/执行命令](../../ecs/documents/user-guide/use-the-immediate-execution-feature.md)。
## 版本升级与回滚
重要
LoongCollector在升级时停止运行，升级完成后自动启动。升级仅覆盖必要文件，配置文件和Checkpoint文件将被保留，确保升级期间日志不会丢失。
### LoongCollector版本升级/Logtail升级到LoongCollector
在服务器上执行下载命令获取最新安装包，示例代码中${region_id}可使用cn-hangzhou替换，若想加快安装包下载速度，请参考[地域](loongcollector-installation-linux.md)替换${region_id}为ECS所属地域。
wget https://aliyun-observability-release-${region_id}.oss-${region_id}.aliyuncs.com/loongcollector/linux64/latest/loongcollector.sh -O loongcollector.sh;
执行升级命令：升级请使用upgrade命令。若使用install命令，将执行覆盖安装，丢失原配置。
chmod +x loongcollector.sh; sudo ./loongcollector.sh upgrade;
若显示以下信息，则表示升级成功。
Upgrade loongcollector files successfully. Starting loongcollector ... Upgrade loongcollector successfully.
### LoongCollector回滚到Logtail
说明
必须要重新下载logtail.sh脚本，不能使用原来的logtail.sh脚本。
在服务器上执行下载命令获取安装包，示例代码中${region_id}可使用cn-hangzhou替换，若想加快安装包下载速度，请参考[地域](loongcollector-installation-linux.md)替换${region_id}为ECS所属地域。
wget https://logtail-release-${region_id}.oss-${region_id}.aliyuncs.com/linux64/logtail.sh -O logtail.sh;
执行回滚命令。如需指定版本，如指定 1.8.7 版本，参考注释，根据实际情况替换版本号。
chmod +x logtail.sh; sudo ./logtail.sh upgrade; #chmod +x logtail.sh; sudo ./logtail.sh upgrade -v 1.8.7;
## 指定版本安装
指定版本通过-v参数实现，参考如下命令根据实际情况替换版本号。
LoongCollector
chmod +x loongcollector.sh; sudo ./loongcollector.sh install ${region_id} -v 3.2.6;
Logtail
chmod +x logtail.sh; sudo ./logtail.sh install ${region_id} -v 1.8.7;
## 卸载LoongCollector
示例代码中${region_id}可使用cn-hangzhou替换，若想加快执行速度，请参考[地域](loongcollector-installation-linux.md)替换${region_id}为ECS所属地域。
wget https://aliyun-observability-release-${region_id}.oss-${region_id}.aliyuncs.com/loongcollector/linux64/latest/loongcollector.sh -O loongcollector.sh;
执行卸载命令。
chmod +x loongcollector.sh; sudo ./loongcollector.sh uninstall;
## 常见问题
### 服务器无法连接外部网络时如何安装
在需要安装LoongCollector的服务器上执行uname -m查看系统架构后，在可以访问公网的服务器上选择对应下载命令执行：${region_id}需替换为Project所属地域的[RegionID](loongcollector-installation-linux.md)。
ARM架构：
wget https://aliyun-observability-release-${region_id}.oss-${region_id}.aliyuncs.com/loongcollector/linux64/latest/loongcollector.sh;wget http://aliyun-observability-release-${region_id}.oss-${region_id}.aliyuncs.com/loongcollector/linux64/latest/aarch64/main/loongcollector-linux64.tar.gz;
x86-64架构：
wget https://aliyun-observability-release-${region_id}.oss-${region_id}.aliyuncs.com/loongcollector/linux64/latest/loongcollector.sh;wget http://aliyun-observability-release-${region_id}.oss-${region_id}.aliyuncs.com/loongcollector/linux64/latest/x86_64/main/loongcollector-linux64.tar.gz;
将下载的安装脚本和安装包拷贝至需要安装LoongCollector的服务器上，执行如下命令：${region_id}需替换为Project所属地域的[RegionID](loongcollector-installation-linux.md)。
chmod +x loongcollector.sh; ./loongcollector.sh install-local ${region_id}-internet
执行查看命令，返回loongcollector is running表示启动成功。
sudo /etc/init.d/loongcollectord status
由于服务器无法访问公网，你还需要通过[配置代理](how-do-i-collect-logs-from-servers-in-a-corporate-intranet.md)的方式与公网建立连接。
### 服务器无法连接外部网络时如何升级
在需要升级LoongCollector的服务器上执行uname -m查看系统架构后，在可以访问公网的服务器上选择对应命令执行：${region_id}需替换为Project所属地域的[地域](loongcollector-installation-linux.md)。
ARM架构：
wget https://aliyun-observability-release-${region_id}.oss-${region_id}.aliyuncs.com/loongcollector/linux64/latest/loongcollector.sh;wget http://aliyun-observability-release-${region_id}.oss-${region_id}.aliyuncs.com/loongcollector/linux64/latest/aarch64/main/loongcollector-linux64.tar.gz;
x86-64架构：
wget https://aliyun-observability-release-${region_id}.oss-${region_id}.aliyuncs.com/loongcollector/linux64/latest/loongcollector.sh;wget http://aliyun-observability-release-${region_id}.oss-${region_id}.aliyuncs.com/loongcollector/linux64/latest/x86_64/main/loongcollector-linux64.tar.gz;
将安装脚本和安装包拷贝至需要升级LoongCollector的服务器上后，执行命令：
chmod +x loongcollector.sh;./loongcollector.sh upgrade-local;
### 一键安装失败
自动安装仅支持ECS与Project同账号同地域情况，若不满足请选择其他安装方式，若满足请检查[前提条件](loongcollector-installation-linux.md)中权限与网络要求是否满足。
### 无心跳/心跳为FAIL如何解决
心跳为FAIL时，可能是初次建立心跳需要花费一些时间，请等待两分钟左右后刷新心跳状态，若仍为FAIL，请按如下步骤检查：
请确认服务器与日志服务Project的关联关系，不同关系对应不同的安装流程。
若发现流程选择错误，在服务器上执行chmod +x loongcollector.sh; sudo ./loongcollector.sh uninstall;卸载命令，再重新选择正确的流程执行即可。
若流程选择正确但心跳为FAIL，请查看安装LoongCollector的服务器上/usr/local/ilogtail/ilogtail_config.json文件中region信息是否与日志服务Project地域的[RegionID](loongcollector-installation-linux.md)一致。
若不一致，请替换安装命令中的${region_id}后重新执行安装命令，LoongCollector将更新上述文件中内容。
此方式将会执行覆盖安装，丢失原配置，慎用于已经进行采集配置的服务器。
若信息一致或重新安装后心跳仍为FAIL，请继续执行后续检查步骤。
若流程中需要设置用户ID文件（即跨账号情况），请检查：
用户ID的值必须为主账号ID，否则请修改。
该主账号ID应为日志服务Project所属的主账号ID，而非ECS服务器所属的主账号ID。
请检查日志服务控制台的机器组中配置的用户自定义标识内容，与服务器用户自定义标识文件中的内容是否一致。若不一致，修改任意一处的内容以保持一致。
若心跳仍然为FAIL，请检查是否满足[前提条件](loongcollector-installation-linux.md)中的网络要求。
## 相关参考
### 地域
登录[日志服务控制台](https://sls.console.aliyun.com/?spm=a2c4g.11186623.0.0.70905a3dccueNa)，在Project列表中，单击目标Project。
单击Project名称右侧的进入项目概览页面。
在基础信息中可查看当前Project的地域名称，地域名称对应RegionID请参考下表。
地域代表云服务资源的物理数据中心所在的地理位置，RegionID 是云服务地域的唯一标识符。
地域RegionID映射表
| 地域名称 | RegionID |
| --- | --- |
| 华北 1（青岛） | cn-qingdao |
| 华北 2（北京） | cn-beijing |
| 华北 3（张家口） | cn-zhangjiakou |
| 华北 5（呼和浩特） | cn-huhehaote |
| 华北 6（乌兰察布） | cn-wulanchabu |
| 华东 1（杭州） | cn-hangzhou |
| 华东 2（上海） | cn-shanghai |
| 华东 5（南京-本地地域-关停中） | cn-nanjing |
| 华东 6（福州-本地地域-关停中） | cn-fuzhou |
| 华南 1（深圳） | cn-shenzhen |
| 华南 2（河源） | cn-heyuan |
| 华南 3（广州） | cn-guangzhou |
| 菲律宾（马尼拉） | ap-southeast-6 |
| 韩国（首尔） | ap-northeast-2 |
| 马来西亚（吉隆坡） | ap-southeast-3 |
| 日本（东京） | ap-northeast-1 |
| 泰国（曼谷） | ap-southeast-7 |
| 西南 1（成都） | cn-chengdu |
| 新加坡 | ap-southeast-1 |
| 印度尼西亚（雅加达） | ap-southeast-5 |
| 中国香港 | cn-hongkong |
| 德国（法兰克福） | eu-central-1 |
| 美国（弗吉尼亚） | us-east-1 |
| 美国（硅谷） | us-west-1 |
| 英国（伦敦） | eu-west-1 |
| 阿联酋（迪拜） | me-east-1 |
| 沙特（利雅得） | me-central-1 |
### LoongCollector网络传输类型
服务入口（Endpoint）表示日志服务对外服务的访问域名，是访问一个项目（Project）及其内部日志数据的URL，与Project所在的地域相关。日志服务提供私网域名、公网域名与传输加速域名。可通过如下操作查看域名：
登录[日志服务控制台](https://sls.console.aliyun.com)，在Project列表中，单击目标Project。
单击Project名称右侧的进入项目概览页面。
在访问域名中可查看当前Project的域名信息，不同的网络传输方式对应不同的域名。合适的网络传输方式有利于日志数据的传输更快速稳定。
| 网络类型 | 对应域名类型 | 描述 | 适用场景 |
| --- | --- | --- | --- |
| 阿里云内网 | 私网域名 | 阿里云内网为千兆共享网络，日志数据通过阿里云内网传输比公网传输更快速、稳定，内网包括 VPC 和经典网络。 | ECS 实例和日志服务 Project 属于同一地域或 [自建服务器打通内网](../../ecs/documents/user-guide/manage-servers-that-are-not-provided-by-alibaba-cloud.md) 的情况。 说明 推荐在 ECS 所在地域创建日志服务 Project，通过阿里云内网采集 ECS 中日志，不消耗公网带宽。 |
| 公网 | 公网域名 | 使用公网传输日志数据，不仅会受到网络带宽的限制，还可能会因网络抖动、延迟、丢包等影响数据采集的速度和稳定性。 | 以下两种情况，可以选择公网传输数据。 ECS 实例和日志服务 Project 属于不同地域。 服务器为其他云厂商服务器或自建 IDC。 |
| 传输加速 | 传输加速域名 | 利用阿里云 CDN 边缘节点进行日志采集加速，相对公网采集在网络延迟、稳定性上具有很大优势，但流量需额外计费。 | 如果业务服务器、日志服务 Project 分别属于国内地域和国外地域，使用公网传输数据可能会出现网络延迟高、传输不稳定等问题，您可以选择传输加速传输数据。更多信息，请参见 [传输加速](select-a-network-type.md) 。 |
该文章对您有帮助吗？
反馈
### 为什么选择阿里云
[什么是云计算](https://www.aliyun.com/about/what-is-cloud-computing)[全球基础设施](https://infrastructure.aliyun.com/)[技术领先](https://www.aliyun.com/why-us/leading-technology)[稳定可靠](https://www.aliyun.com/why-us/reliability)[安全合规](https://www.aliyun.com/why-us/security-compliance)[分析师报告](https://www.aliyun.com/analyst-reports)
### 大模型
[千问大模型](https://www.aliyun.com/product/tongyi)[大模型服务](https://bailian.console.aliyun.com/?tab=model#/model-market)[AI应用构建](https://bailian.console.aliyun.com/app-center?tab=app#/app-center)
### 产品和定价
[全部产品](https://www.aliyun.com/product/list)[免费试用](https://free.aliyun.com/)[产品动态](https://www.aliyun.com/product/news/)[产品定价](https://www.aliyun.com/price/detail)[配置报价器](https://www.aliyun.com/price/cpq/list)[云上成本管理](https://www.aliyun.com/price/cost-management)
### 技术内容
[技术解决方案](https://www.aliyun.com/solution/tech-solution)[帮助文档](https://help.aliyun.com/)[开发者社区](https://developer.aliyun.com/)[天池大赛](https://tianchi.aliyun.com/)[阿里云认证](https://edu.aliyun.com/)
### 权益
[免费试用](https://free.aliyun.com/)[解决方案免费试用](https://www.aliyun.com/solution/free)[高校计划](https://university.aliyun.com/)[5亿算力补贴](https://www.aliyun.com/benefit/form/index)[推荐返现计划](https://dashi.aliyun.com/?ambRef=shouYeDaoHang2&pageCode=yunparterIndex)
### 服务
[基础服务](https://www.aliyun.com/service)[企业增值服务](https://www.aliyun.com/service/supportplans)[迁云服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_cloudmigration_public_cn)[官网公告](https://www.aliyun.com/notice/)[健康看板](https://status.aliyun.com/)[信任中心](https://security.aliyun.com/trust-center)
### 关注阿里云
关注阿里云公众号或下载阿里云APP，关注云资讯，随时随地运维管控云服务
联系我们：4008013260
[法律声明](https://help.aliyun.com/product/67275.html)[Cookies 政策](https://terms.alicdn.com/legal-agreement/terms/platform_service/20220906101446934/20220906101446934.html)[廉正举报](https://aliyun.jubao.alibaba.com/)[安全举报](https://report.aliyun.com/)[联系我们](https://www.aliyun.com/contact)[加入我们](https://careers.aliyun.com/)
### 友情链接
[阿里巴巴集团](https://www.alibabagroup.com/cn/global/home)[淘宝网](https://www.taobao.com/)[天猫](https://www.tmall.com/)[全球速卖通](https://www.aliexpress.com/)[阿里巴巴国际交易市场](https://www.alibaba.com/)[1688](https://www.1688.com/)[阿里妈妈](https://www.alimama.com/index.htm)[飞猪](https://www.fliggy.com/)[阿里云计算](https://www.aliyun.com/)[万网](https://wanwang.aliyun.com/)[高德](https://mobile.amap.com/)[UC](https://www.uc.cn/)[友盟](https://www.umeng.com/)[优酷](https://www.youku.com/)[钉钉](https://www.dingtalk.com/)[支付宝](https://www.alipay.com/)[达摩院](https://damo.alibaba.com/)[淘宝海外](https://world.taobao.com/)[阿里云盘](https://www.aliyundrive.com/)[淘宝闪购](https://www.ele.me/)
© 2009-现在 Aliyun.com 版权所有 增值电信业务经营许可证：[浙B2-20080101](http://beian.miit.gov.cn/)域名注册服务机构许可：[浙D3-20210002](https://domain.miit.gov.cn/域名注册服务机构/互联网域名/阿里云计算有限公司 )
[浙公网安备 33010602009975号](http://www.beian.gov.cn/portal/registerSystemInfo)[浙B2-20080101-4](https://beian.miit.gov.cn/)
