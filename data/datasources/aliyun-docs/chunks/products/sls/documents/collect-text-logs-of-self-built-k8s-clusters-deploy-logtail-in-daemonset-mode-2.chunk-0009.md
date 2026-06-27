# ===================== 必需要补充的内容 ===================== # 管理采集日志的Project名，例如 k8s-log-custom-sd89ehdq。 projectName: "" # Project所属地域，例如上海：cn-shanghai region: "" # Project所属主账号uid，请用引号包围，例如"123456789" aliUid: "" # 使用网络，可选参数：公网Internet，内网Intranet，默认使用公网 net: Internet # 主账号或者子账号的AK，SK，需具备AliyunLogFullAccess系统策略权限 accessKeyID: "" accessKeySecret: "" # 自定义集群ID，命名只支持大小写，数字，短划线(-)。 clusterID: ""
在loongcollector-custom-k8s-package目录下执行如下命令，安装LoongCollector及其他依赖组件：
bash k8s-custom-install.sh install
安装完成后，查看组件运行状态。
若Pod未成功启动，请确认values.yaml配置是否正确，相关镜像拉取是否成功。
