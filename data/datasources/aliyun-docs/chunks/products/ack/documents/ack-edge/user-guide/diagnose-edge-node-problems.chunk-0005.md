## 如何收集ACK Edge集群节点的诊断信息？
当ACK Edge集群的节点出现异常时，您可以参见以下步骤收集集群节点的诊断信息，以供数据分析使用。
登录到ACK Edge集群的异常节点。
执行如下命令，下载诊断脚本。
curl -o /usr/local/bin/diagnose_edge_node.sh https://aliacs-k8s-cn-hangzhou.oss-cn-hangzhou.aliyuncs.com/public/diagnose/diagnose_k8s.sh
执行如下命令，给诊断脚本添加执行权限。
chmod u+x /usr/local/bin/diagnose_edge_node.sh
执行如下命令，进入指定目录。
cd /usr/local/bin/
执行如下命令，运行诊断脚本。
./diagnose_edge_node.sh
预期输出如下。每次执行诊断脚本产生的诊断信息文件名称不同，本示例以diagnose_1578310147.tar.gz为例，具体以实际环境为准。
...... + echo 'please get diagnose_1578310147.tar.gz for diagnostics' please get diagnose_1578310147.tar.gz for diagnostics + echo '请提交 diagnose_1578310147.tar.gz 给技术支持' 请提交 diagnose_1578310147.tar.gz 给技术支持
执行ll命令，确认存在diagnose_1578310147.tar.gz诊断信息文件。
该文章对您有帮助吗？
反馈
