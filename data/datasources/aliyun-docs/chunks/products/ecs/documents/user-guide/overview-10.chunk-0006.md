## Windows 实例
在 Windows 操作系统的实例中，云助手的主要文件和目录位于 C:\ProgramData\aliyun\assist\。
C:\ProgramData\aliyun\assist\
2.x.x.xxx/ (例如: 2.1.4.965) -云助手具体版本安装目录
acs-plugin-manager.exe: 云助手插件管理器程序。
aliyun_assist_update.exe: 云助手升级程序。
aliyun_installer.exe: 云助手安装程序。
aliyun_assist_service.exe: 云助手服务的主程序。
install.bat: 云助手安装脚本。
install.exe: 云助手安装程序。
PatchGo.dll: 针对 Windows Server 2008 环境的补丁，用于避免 Go 语言运行时导致的时钟跳变问题。
version.ini: 记录云助手版本信息。
config/: 配置文件目录。
GlobalSignRootCA.crt: 云助手服务端通信所需的证书文件。
hash_file: 程序文件的哈希记录，用于文件一致性验证。
log/: 日志文件目录。
aliyun_assist_main.log: 当天的运行日志。
aliyun_assist_main.log.YYYYMMDD: 历史日志文件，按日期归档。
plugin/: 预装及已安装插件目录。
ACS-ECS-SysInfoGatherer: 数据采集插件。
SessionManager: 实现免密登录功能的插件。
installed_plugins.db: 云助手插件的信息。
cache/: 缓存文件目录。
state_configs.json: 云助手Agent 本地缓存的 OOS Inventory 采集配置文件。
config/: 配置文件目录。
task_sign_certs/: 云助手Agent 本地缓存的任务签名校验公钥。
hybrid/: 托管实例信息目录。
plugin/: 插件数据目录。
installed_plugins.db: 插件的数据信息。
work/: 执行文件存放目录。
script/: 云助手执行的脚本文件存放目录。
注意：从 2.x.3.704 版本开始，默认不自动保存脚本文件到此目录，需手动开启。
config.ini: 记录云助手版本等配置信息的文件。
region-id: 记录实例所处地域信息的文件。
version: 记录当前云助手版本信息的文件。
