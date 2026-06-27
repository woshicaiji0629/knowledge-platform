AMD实例。具体规格请参见[适用实例](booster-extensions.md)。
镜像：选择Alibaba Cloud Linux 3镜像。
扩展程序：
驱动：如需配置eRDMA，请选中eRDMA驱动，系统会自动安装。
性能加速：选择需要安装的应用（如Nginx、MySQL、Memcached等），默认版本及性能提升请参见[默认安装的应用版本及性能提升](booster-extensions.md)。
说明
支持安装的应用，以页面实际呈现为准。
Intel实例
实例：选择Intel实例。具体规格请参见[适用实例](booster-extensions.md)。
镜像：选择Alibaba Cloud Linux 3镜像。
扩展程序：
驱动：如需配置eRDMA，请选中eRDMA驱动，系统会自动安装。
性能加速：仅支持选择安装MySQL应用。
默认安装的应用版本及性能提升说明请参见[默认安装的应用版本及性能提升](booster-extensions.md)。
实例创建成功后，系统会自动安装选择的应用，并使用KeenTune针对该应用的业务特点进行全栈性能调优。
关闭性能加速能力
购买实例之后，如果不需要性能加速能力，可以单独卸载KeenTune关闭性能加速，保留已安装的应用。
重要
性能加速主要针对单一应用部署场景，如果您是混合部署场景，建议您在使用混合部署方式之前，参考如下命令关闭性能加速能力。
关闭性能加速能力后，会同步关闭eRDMA透明替换能力。
sudo bash /etc/keentune/target/scripts/set_xps_rps.sh eth0 rps disable sudo keentune profile rollback sudo systemctl stop keentune-target keentuned sudo yum remove keentune-target keentuned
卸载默认安装的应用
购买实例后，如果不需要默认安装的应用程序，可以卸载它们，性能加速能力将保留。重新安装后，程序仍具有性能加速能力。
sudo systemctl stop <APP_Name> sudo yum remove <APP_Name>
说明
<APP_Name>请替换为实际的应用名称（如Nginx）。
