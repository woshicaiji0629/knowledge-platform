# 无法连接Linux实例的排查方法-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/troubleshooting-guidelines-when-you-cannot-remotely-log-on-to-a-linux-instance-through-ssh

# 无法连接Linux实例的排查方法
本文主要介绍无法远程登录Linux实例的排查方法。
重要
应急登录Linux实例：如果您遇到紧急情况，需要尽快登录Linux实例执行运维操作，您可以先使用VNC的方式登录实例，具体操作，请参见[通过](user-guide/log-on-to-an-instance-by-using-vnc.md)[VNC](user-guide/log-on-to-an-instance-by-using-vnc.md)[连接实例](user-guide/log-on-to-an-instance-by-using-vnc.md)。
## 问题原因
SSH远程登录失败的原因可能包括PAM安全框架、安全组、SSH配置等。请根据实际情况，通过相应的排查方法，排查并解决无法远程连接Linux实例的问题。
[没有明确的报错信息](troubleshooting-guidelines-when-you-cannot-remotely-log-on-to-a-linux-instance-through-ssh.md)
[存在明确的报错信息](troubleshooting-guidelines-when-you-cannot-remotely-log-on-to-a-linux-instance-through-ssh.md)
## 没有明确的报错信息
### 使用诊断工具
阿里云的诊断工具可以帮助您快速检测安全组配置、实例内部防火墙以及常见应用端口监听状态，并给出明确的诊断报告。
单击一键诊断进入诊断页面，并切换至目标地域。
诊断报告将展示异常项清单及详情，例如提示安全组入方向常用端口未放开，并列出方向、协议（如 ICMP）、端口、策略（未放通）及影响说明，同时提供修改安全组规则的修复建议链接。
如果诊断工具未能定位您的问题，请继续下面的步骤进行手动排查。
### 手动排查问题
在远程连接失败时，如果您没有收到系统返回的报错信息，您可以根据以下步骤手动排查问题：
步骤一：使用阿里云Workbench工具测试远程登录
通过阿里云提供的Workbench工具进行远程登录，Workbench工具在远程登录出现异常时会返回具体的错误信息及解决方案。测试步骤如下：
访问[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)。
在页面左侧顶部，选择目标资源所在的资源组和地域。
单击目标实例ID进入实例详情页，单击远程连接。
在弹出的远程连接对话框中，单击通过Workbench远程连接对应的立即登录。
测试是否可以远程登录。
Workbench工具将自动填充登录目标实例所需的基本信息，请确认基本信息的正确性并输入登录的用户名和认证信息。并根据以下结果进行处理：通过Workbench远程登录Linux实例的具体操作，请参见[通过](user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[Workbench](user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[远程登录](user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[Linux](user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[实例](user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)。
如仍然无法登录，Workbench工具会返回错误提示和解决方案，请根据提示进行处理。处理完毕后重新使用Workbench工具进行远程登录测试。为了便于您解决问题，列举Workbench工具使用时常见的异常问题：[通过](through-vnc-instance-remote-connection-problems.md)[VNC](through-vnc-instance-remote-connection-problems.md)[远程连接实例的问题](through-vnc-instance-remote-connection-problems.md)
如可以通过Workbench工具正常登录，说明目标实例上的SSH服务正常运行，即排除SSH服务端异常的可能性，继续执行[步骤二：检查网络](troubleshooting-guidelines-when-you-cannot-remotely-log-on-to-a-linux-instance-through-ssh.md)进行排查。
步骤二：检查网络
无法正常远程连接Linux实例时，需要先检查网络是否正常。
用其他网络环境中，不同网段或不同运营商的电脑连接对比测试，判断是本地网络问题还是服务器端的问题。
如果是本地网络问题或运营商问题，请联系本地IT人员或运营商解决。
如果是网卡驱动存在异常，请重新安装。
在本地客户端使用ping命令测试与实例的网络连通性。
网络异常时，请进行抓取数据包进行分析，具体操作，请参见[使用抓包工具进行网络数据包抓取](user-guide/how-to-grab-data-packets-when-the-network-is-abnormal.md)。
当出现ping丢包或ping不通时，可以通过tracert或mtr等工具进行链路测试来判断问题根源。具体操作，请参见[使用](user-guide/use-mtr-tool-for-network-analysis.md)[MTR](user-guide/use-mtr-tool-for-network-analysis.md)[工具进行网络链路分析](user-guide/use-mtr-tool-for-network-analysis.md)。
系统内核没有禁ping的情况下，使用ping命令测试ECS服务器，发现网络不通，可能是服务器系统内部防火墙对客户端进行了drop策略。
具体操作，请参见[无法](troubleshooting-for-ping-attempts-to-pass-the-server-and-port-disconnection.md)[ping](troubleshooting-for-ping-attempts-to-pass-the-server-and-port-disconnection.md)[通](troubleshooting-for-ping-attempts-to-pass-the-server-and-port-disconnection.md)[ECS](troubleshooting-for-ping-attempts-to-pass-the-server-and-port-disconnection.md)[实例公网](troubleshooting-for-ping-attempts-to-pass-the-server-and-port-disconnection.md)[IP](troubleshooting-for-ping-attempts-to-pass-the-server-and-port-disconnection.md)[的排查方法](troubleshooting-for-ping-attempts-to-pass-the-server-and-port-disconnection.md)。
步骤三：检查端口和安全组
检查安全组配置是否允许远程连接的端口。
访问[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)。
在页面左侧顶部，选择目标资源所在的资源组和地域。
在实例列表页面，单击对应的实例ID。
在安全组页签下，单击安全组操作列的管理规则。
在安全组详情页面，在访问规则区域的入方向页签下，单击增加规则，按以下参数添加规则。
授权策略：允许
优先级：1（代表安全规则中优先级最高，数字越小优先级越高）
协议：自定义 TCP
访问来源：设置为本机IP，可以访问[https://cip.cc/](https://cip.cc/)获取本机IP
访问目的(本实例)：选择SSH(22)
使用以下命令，进行端口测试，判断端口是否正常。
telnet [$IP] [$Port]
说明
[$IP]指Linux实例的IP地址。
[$Port]指Linux实例的RDP端口号。
系统显示类似如下，比如执行telnet 192.168.0.1 22命令，正常情况下返回结果类似如下。
Trying 192.168.0.1 ... Connected to 192.168.0.1. Escape character is '^]'
如果端口测试失败，请参见[能](troubleshoot-the-issue-that-an-instance-can-be-pinged-but-the-required-port-cannot.md)[ping](troubleshoot-the-issue-that-an-instance-can-be-pinged-but-the-required-port-cannot.md)[通](troubleshoot-the-issue-that-an-instance-can-be-pinged-but-the-required-port-cannot.md)[ECS](troubleshoot-the-issue-that-an-instance-can-be-pinged-but-the-required-port-cannot.md)[实例但端口不通的排查方法](troubleshoot-the-issue-that-an-instance-can-be-pinged-but-the-required-port-cannot.md)进行排查。
步骤四：检查CPU负载、带宽及内存使用情况
无法正常远程连接时，可能是因为CPU负载、带宽不足或内存不足导致。
根据是否存在CPU负载过高情况，选择相应操作。
存在CPU负载过高情况。
若应用程序有大量的磁盘访问、网络访问行为、高计算需求，CPU负载过高是正常结果。建议您升配实例规格来解决资源瓶颈问题，具体操作，请参见[升降配方式概述](user-guide/overview-of-instance-configuration-changes.md)。
说明
CPU负载过高的解决方法，请参见[Linux](support/query-and-case-analysis-linux-cpu-load.md)[系统](support/query-and-case-analysis-linux-cpu-load.md)[CPU](support/query-and-case-analysis-linux-cpu-load.md)[负载的查询和案例分析](support/query-and-case-analysis-linux-cpu-load.md)。
说明
排查是否感染病毒：排除正常业务后，CPU资源仍被异常占满，可能是实例感染挖矿病毒。挖矿程序会恶意抢占CPU等资源，导致实例卡顿、响应缓慢，严重时无法远程连接，具体排查与处理请参见[挖矿病毒处理和防护指南](user-guide/mining-virus-protection-and-handling-guide.md)；如果实例感染勒索病毒，系统文件被加密锁定，同样可能导致无法正常登录，具体请参见[提升实例防勒索能力的指南](user-guide/enhance-anti-ransomware-capabilities-for-instances.md)。
不存在CPU负载过高情况，请继续下一步排查。
排查是否存在公网带宽不足问题。
无法远程连接可能是公网带宽不足导致的，具体排查方法如下。
访问[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)。
在页面左侧顶部，选择目标资源所在的资源组和地域。
在实例列表，单击对应的实例ID，在配置信息区域，查看公网带宽。
如果服务器带宽为0 Mbps，说明购买实例时没有购买公网带宽，您可以通过升级带宽解决，具体操作，请参见[修改公网带宽峰值](user-guide/overview-of-instance-configuration-changes.md)。
排查是否存在内存不足问题。
远程连接Linux实例后，不能正常显示桌面并直接退出，也没有错误信息提示。这种情况可能是服务器内存不足导致，需要检查服务器的内存使用情况。具体操作如下。
使用VNC方式登录Linux实例。
具体操作，请参见[通过密码认证登录](user-guide/log-on-to-an-instance-by-using-vnc.md)[Linux](user-guide/log-on-to-an-instance-by-using-vnc.md)[实例](user-guide/log-on-to-an-instance-by-using-vnc.md)。
查看内存使用情况，如果存在内存不足情况，建议您升配实例规格来解决资源瓶颈问题，具体操作，请参见[升降配方式概述](user-guide/overview-of-instance-configuration-changes.md)。
## 存在明确的报错信息
远程登录失败时，系统通常会返回报错信息。您可以根据报错信息，快速定位问题原因及解决方案。
### PAM安全框架
Linux系统的PAM安全框架可以加载相关安全模块，对云服务器的账户策略、登录策略等进行访问控制。如果相关配置存在异常，或触发了相关策略，就可能会导致SSH登录失败。常见案例：
[使用正确的密码无法登录](you-cannot-log-on-to-the-ecs-instance-of-the-linux-by-using-the-correct-password.md)[Linux](you-cannot-log-on-to-the-ecs-instance-of-the-linux-by-using-the-correct-password.md)[系统的](you-cannot-log-on-to-the-ecs-instance-of-the-linux-by-using-the-correct-password.md)[ECS](you-cannot-log-on-to-the-ecs-instance-of-the-linux-by-using-the-correct-password.md)[实例](you-cannot-log-on-to-the-ecs-instance-of-the-linux-by-using-the-correct-password.md)
[使用](what-do-i-do-when-i-cannot-log-on-to-a-linux-instance-after-the-pam-authentication-module-is-enabled.md)[SSH](what-do-i-do-when-i-cannot-log-on-to-a-linux-instance-after-the-pam-authentication-module-is-enabled.md)[登录](what-do-i-do-when-i-cannot-log-on-to-a-linux-instance-after-the-pam-authentication-module-is-enabled.md)[Linux](what-do-i-do-when-i-cannot-log-on-to-a-linux-instance-after-the-pam-authentication-module-is-enabled.md)[系统的](what-do-i-do-when-i-cannot-log-on-to-a-linux-instance-after-the-pam-authentication-module-is-enabled.md)[ECS](what-do-i-do-when-i-cannot-log-on-to-a-linux-instance-after-the-pam-authentication-module-is-enabled.md)[实例时提示“requirement "uid >= 1000" not met by user "root"”错误](what-do-i-do-when-i-cannot-log-on-to-a-linux-instance-after-the-pam-authentication-module-is-enabled.md)
[SSH](multiple-consecutive-incorrect-password-accesses-to-linux-instances-through-ssh.md)[登录](multiple-consecutive-incorrect-password-accesses-to-linux-instances-through-ssh.md)[Linux](multiple-consecutive-incorrect-password-accesses-to-linux-instances-through-ssh.md)[实例时多次连续错误输入密码导致用户锁定](multiple-consecutive-incorrect-password-accesses-to-linux-instances-through-ssh.md)
### Linux实例系统环境配置
Linux内的系统环境，例如中毒、账户配置、环境变量配置等，如果出现异常，也可能会导致SSH登录失败。常见案例：
[SSH](the-ssh-exchange-identification-read-connection-reset-by-peer-error-is-displayed-when-you-log-on-to-an-ecs-instance-through-ssh.md)[登录](the-ssh-exchange-identification-read-connection-reset-by-peer-error-is-displayed-when-you-log-on-to-an-ecs-instance-through-ssh.md)[ECS](the-ssh-exchange-identification-read-connection-reset-by-peer-error-is-displayed-when-you-log-on-to-an-ecs-instance-through-ssh.md)[实例提示“ssh_exchange_identification: read: Connection reset by peer”错误](the-ssh-exchange-identification-read-connection-reset-by-peer-error-is-displayed-when-you-log-on-to-an-ecs-instance-through-ssh.md)
[病毒引发](the-system-prompts-fatal-mm-request-send-write-broken-pipe-error-when-the-ssh-service-runs-abnormally-caused-by-viruses.md)[SSH](the-system-prompts-fatal-mm-request-send-write-broken-pipe-error-when-the-ssh-service-runs-abnormally-caused-by-viruses.md)[服务运行异常系统提示“fatal: mm_request_send: write: Broken pipe”错误](the-system-prompts-fatal-mm-request-send-write-broken-pipe-error-when-the-ssh-service-runs-abnormally-caused-by-viruses.md)
[SSH](main-process-exited-code-exited-error-when-ssh-service-is-started.md)[服务启动时报“main process exited, code=exited”错误](main-process-exited-code-exited-error-when-ssh-service-is-started.md)
[Linux](a-system-exception-occurs-on-linux-instances-after-ssh-logon-due-to-ulimit.md)[实例由于](a-system-exception-occurs-on-linux-instances-after-ssh-logon-due-to-ulimit.md)[Ulimit](a-system-exception-occurs-on-linux-instances-after-ssh-logon-due-to-ulimit.md)[限制原因导致](a-system-exception-occurs-on-linux-instances-after-ssh-logon-due-to-ulimit.md)[SSH](a-system-exception-occurs-on-linux-instances-after-ssh-logon-due-to-ulimit.md)[登录后系统异常](a-system-exception-occurs-on-linux-instances-after-ssh-logon-due-to-ulimit.md)
[使用](an-error-is-reported-when-you-log-on-to-an-ecs-instance-of-the-linux-system-by-using-ssh-commands.md)[SSH](an-error-is-reported-when-you-log-on-to-an-ecs-instance-of-the-linux-system-by-using-ssh-commands.md)[命令登录](an-error-is-reported-when-you-log-on-to-an-ecs-instance-of-the-linux-system-by-using-ssh-commands.md)[Linux](an-error-is-reported-when-you-log-on-to-an-ecs-instance-of-the-linux-system-by-using-ssh-commands.md)[系统的](an-error-is-reported-when-you-log-on-to-an-ecs-instance-of-the-linux-system-by-using-ssh-commands.md)[ECS](an-error-is-reported-when-you-log-on-to-an-ecs-instance-of-the-linux-system-by-using-ssh-commands.md)[实例时出现报错](an-error-is-reported-when-you-log-on-to-an-ecs-instance-of-the-linux-system-by-using-ssh-commands.md)
[Linux](an-ssh-remote-connection-exception-occurs-in-a-linux-instance-because-the-selinux-service-is-enabled.md)[实例中由于](an-ssh-remote-connection-exception-occurs-in-a-linux-instance-because-the-selinux-service-is-enabled.md)[SELinux](an-ssh-remote-connection-exception-occurs-in-a-linux-instance-because-the-selinux-service-is-enabled.md)[服务开启导致](an-ssh-remote-connection-exception-occurs-in-a-linux-instance-because-the-selinux-service-is-enabled.md)[SSH](an-ssh-remote-connection-exception-occurs-in-a-linux-instance-because-the-selinux-service-is-enabled.md)[远程连接异常](an-ssh-remote-connection-exception-occurs-in-a-linux-instance-because-the-selinux-service-is-enabled.md)
### SSH服务及参数配置
SSH服务的默认配置文件为/etc/ssh/sshd_config。配置文件中的相关参数配置异常，或启用了相关特性或策略，也可能会导致SSH登录失败。常见案例：
[SSH](the-disconnected-no-supported-authentication-methods-available-error-occurs-when-you-log-on-to-a-linux-instance-by-ssh.md)[登录](the-disconnected-no-supported-authentication-methods-available-error-occurs-when-you-log-on-to-a-linux-instance-by-ssh.md)[Linux](the-disconnected-no-supported-authentication-methods-available-error-occurs-when-you-log-on-to-a-linux-instance-by-ssh.md)[实例时出现"Disconnected:No supported authentication methods available"错误](the-disconnected-no-supported-authentication-methods-available-error-occurs-when-you-log-on-to-a-linux-instance-by-ssh.md)
[使用](the-user-root-not-allowed-because-not-listed-in-error-occurs-when-you-log-on-to-a-linux-instance-by-using-ssh-commands.md)[SSH](the-user-root-not-allowed-because-not-listed-in-error-occurs-when-you-log-on-to-a-linux-instance-by-using-ssh-commands.md)[命令登录](the-user-root-not-allowed-because-not-listed-in-error-occurs-when-you-log-on-to-a-linux-instance-by-using-ssh-commands.md)[Linux](the-user-root-not-allowed-because-not-listed-in-error-occurs-when-you-log-on-to-a-linux-instance-by-using-ssh-commands.md)[实例时出现“User root not allowed because not listed in”错误](the-user-root-not-allowed-because-not-listed-in-error-occurs-when-you-log-on-to-a-linux-instance-by-using-ssh-commands.md)
[使用](how-to-fix-the-permission-denied-please-try-again-error-when-you-log-on-to-a-linux-instance-using-ssh.md)[root](how-to-fix-the-permission-denied-please-try-again-error-when-you-log-on-to-a-linux-instance-using-ssh.md)[用户通过](how-to-fix-the-permission-denied-please-try-again-error-when-you-log-on-to-a-linux-instance-using-ssh.md)[SSH](how-to-fix-the-permission-denied-please-try-again-error-when-you-log-on-to-a-linux-instance-using-ssh.md)[登录](how-to-fix-the-permission-denied-please-try-again-error-when-you-log-on-to-a-linux-instance-using-ssh.md)[Linux](how-to-fix-the-permission-denied-please-try-again-error-when-you-log-on-to-a-linux-instance-using-ssh.md)[实例时报“Permission denied, please try again”的错误](how-to-fix-the-permission-denied-please-try-again-error-when-you-log-on-to-a-linux-instance-using-ssh.md)
[使用](the-too-many-authentication-failures-for-root-error-occurs-when-you-log-on-to-an-instance-through-ssh.md)[SSH](the-too-many-authentication-failures-for-root-error-occurs-when-you-log-on-to-an-instance-through-ssh.md)[登录实例时出现“Too many authentication failures for root”错误](the-too-many-authentication-failures-for-root-error-occurs-when-you-log-on-to-an-instance-through-ssh.md)
[启动](the-error-while-loading-shared-libraries-error-occurs-when-you-start-the-ssh-service.md)[SSH](the-error-while-loading-shared-libraries-error-occurs-when-you-start-the-ssh-service.md)[服务时出现“error while loading shared libraries”错误](the-error-while-loading-shared-libraries-error-occurs-when-you-start-the-ssh-service.md)
[在](in-linux-ecs-instances-the-following-error-fatal-cannot-bind-any-address-occurs-when-the-ssh-service-is-started.md)[Linux](in-linux-ecs-instances-the-following-error-fatal-cannot-bind-any-address-occurs-when-the-ssh-service-is-started.md)[系统的](in-linux-ecs-instances-the-following-error-fatal-cannot-bind-any-address-occurs-when-the-ssh-service-is-started.md)[ECS](in-linux-ecs-instances-the-following-error-fatal-cannot-bind-any-address-occurs-when-the-ssh-service-is-started.md)[实例中](in-linux-ecs-instances-the-following-error-fatal-cannot-bind-any-address-occurs-when-the-ssh-service-is-started.md)[SSH](in-linux-ecs-instances-the-following-error-fatal-cannot-bind-any-address-occurs-when-the-ssh-service-is-started.md)[服务启动时出现如下错误“fatal: Cannot bind any address”](in-linux-ecs-instances-the-following-error-fatal-cannot-bind-any-address-occurs-when-the-ssh-service-is-started.md)
[启动](the-bad-configuration-options-error-occurs-when-the-ssh-service-is-started.md)[SSH](the-bad-configuration-options-error-occurs-when-the-ssh-service-is-started.md)[服务时出现“Bad configuration options”错误](the-bad-configuration-options-error-occurs-when-the-ssh-service-is-started.md)
[SSH](using-usedns-to-enable-ssh-slows-down-ssh-logon-or-data-transfer.md)[启用](using-usedns-to-enable-ssh-slows-down-ssh-logon-or-data-transfer.md)[UseDNS](using-usedns-to-enable-ssh-slows-down-ssh-logon-or-data-transfer.md)[导致](using-usedns-to-enable-ssh-slows-down-ssh-logon-or-data-transfer.md)[SSH](using-usedns-to-enable-ssh-slows-down-ssh-logon-or-data-transfer.md)[登录或数据传输速度变慢](using-usedns-to-enable-ssh-slows-down-ssh-logon-or-data-transfer.md)
### SSH服务关联目录或文件配置
SSH服务基于安全性考虑，在运行时，会对相关目录或文件的权限配置、属组等进行检查。过高或过低的权限配置，都可能会引发服务运行异常，进而导致客户端登录失败。常见案例：
[使用](the-no-supported-key-exchange-algorithms-error-occurs-when-you-log-on-to-a-linux-instance-by-using-ssh-commands.md)[SSH](the-no-supported-key-exchange-algorithms-error-occurs-when-you-log-on-to-a-linux-instance-by-using-ssh-commands.md)[命令登录](the-no-supported-key-exchange-algorithms-error-occurs-when-you-log-on-to-a-linux-instance-by-using-ssh-commands.md)[Linux](the-no-supported-key-exchange-algorithms-error-occurs-when-you-log-on-to-a-linux-instance-by-using-ssh-commands.md)[实例时出现“No supported key exchange algorithms”错误](the-no-supported-key-exchange-algorithms-error-occurs-when-you-log-on-to-a-linux-instance-by-using-ssh-commands.md)
[SSH](what-should-i-do-if-the-must-be-owned-by.md)[服务启动时系统提示“must be owned by root and not group or word-writable”错误](what-should-i-do-if-the-must-be-owned-by.md)
### SSH服务密钥配置
SSH服务采用非对称加密技术，对所传输的数据进行加密。客户端及服务端会交换和校验相关密钥信息的有效性。常见案例：
[使用](the-system-prompts-host-key-verification-failed-when-logging-on-to-the-ecs-instance-over-ssh.md)[SSH](the-system-prompts-host-key-verification-failed-when-logging-on-to-the-ecs-instance-over-ssh.md)[登录](the-system-prompts-host-key-verification-failed-when-logging-on-to-the-ecs-instance-over-ssh.md)[ECS](the-system-prompts-host-key-verification-failed-when-logging-on-to-the-ecs-instance-over-ssh.md)[实例时提示“Host key verification failed”错误](the-system-prompts-host-key-verification-failed-when-logging-on-to-the-ecs-instance-over-ssh.md)
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
