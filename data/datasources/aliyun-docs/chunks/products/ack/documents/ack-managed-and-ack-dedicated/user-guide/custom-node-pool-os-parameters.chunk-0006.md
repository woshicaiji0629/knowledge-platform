### 通过配置文件配置
ACK允许将自定义参数写入至/etc/sysctl.d/99-user-customized.conf，该文件是节点初始化和重启时预留的可供自定义配置的文件。写入到该配置文件的 sysctl 参数会在节点重启时优先生效，覆盖操作系统默认值和通过节点池自定义 sysctl 配置功能写入的参数值。
重要
调整 sysctl 参数会改变 Linux 内核的运作方式，可能导致节点性能恶化或不可用，影响业务正常运行。请在操作前请充分评估变更风险。
对于节点池中的存量节点，可[登录节点](../../../../ecs/documents/user-guide/connect-to-instance.md)修改该自定义参数配置文件，同时手动执行sysctl -p /etc/sysctl.d/99-user-customized.conf命令使配置生效。
对于节点池未来扩容的节点，可将对自定义参数配置文件的写入脚本配置到节点池实例预自定义数据中，以确保新增节点可默认使用这些自定义参数值。方式如下。
在节点池配置中的实例预自定义数据中配置echo '${sysctl_key}=${sysctl_value}' > /etc/sysctl.d/99-user-customized.conf（${sysctl_key}和${sysctl_value}需替换实际值），将自定义配置写入/etc/sysctl.d/目录下的配置文件。
操作入口，请参见[创建和管理节点池](create-a-node-pool.md)。
