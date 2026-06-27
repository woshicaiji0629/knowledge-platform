## Linux 实例
在 Linux 操作系统的实例中，云助手的主要文件和目录位于 /usr/local/share/aliyun-assist/。
/usr/local/share/aliyun-assist/
2.x.x.xxx/ (例如: 2.2.4.965) -云助手具体版本安装目录
acs-plugin-manager: 云助手插件管理器程序。
aliyun_assist_update: 云助手升级程序。
aliyun_installer: 早期的组件安装器（已废弃，功能由 acs-plugin-manager 替代）。
aliyun-service: 云助手 Agent 的主程序。
assist_daemon: 云助手守护进程，确保主程序 aliyun-service 的稳定运行。
config/: 配置文件目录。
GlobalSignRootCA.crt: 用于与云助手服务端进行 HTTPS 安全通信的根证书文件。
hash_file: 程序文件的哈希记录，用于文件一致性校验，确保核心文件未被篡改。
init/: 安装及卸载脚本目录。
clean: 清理脚本，用于移除云助手相关配置和文件。
install: 安装脚本。
uninstall: 卸载脚本。
version: 记录当前云助手客户端版本信息的文件。
log/: 日志文件目录。
aliyun_assist_main.log: 记录云助手当天的运行日志。
aliyun_assist_main.log.YYYYMMDD: 历史日志文件，按日期归档。
plugin/: 预装插件目录。
ACS-ECS-SysInfoGatherer: 云助手数据采集插件。
cache/: 缓存文件目录。
state_configs.json: 云助手Agent 本地缓存的运维与配置OOS Inventory 采集配置文件。
config/: 全局配置文件目录。
task_sign_certs/: 云助手Agent 本地缓存的、用于校验任务签名的公钥。
hybrid/: 托管实例注册信息目录。
hardwareHash: 当实例注册为托管实例时，由云助手 Agent 生成的用于标识机器的硬件信息记录文件。
plugin/: 云助手插件目录。
installed_plugins.db: 记录插件的数据信息。
work/: 执行文件存放目录。
script/: 云助手执行文件存放目录。
注意：从 2.x.3.704 版本开始，为增强安全性，云助手默认不再将执行脚本自动落盘。您需要手动开启相关配置，才能在此目录下看到执行的脚本文件。
region-id: 记录当前实例所处地域（Region）信息的文件。
