## 功能已知影响
数据完整性风险
并发写一致性风险：为提升写操作稳定性，建议[升级](install-and-upgrade-the-csi-plug-in.md)[CSI](install-and-upgrade-the-csi-plug-in.md)[组件](install-and-upgrade-the-csi-plug-in.md)至v1.28及以上版本。但对于单文件并发写场景，OSS的“覆盖上传”特性仍可能导致数据覆盖，需在应用层保障数据一致性。
数据同步与误删风险：挂载状态下，在应用Pod或宿主机上对挂载路径下的文件删除或变更操作会直接同步到OSS Bucket源文件。为避免数据误删除，建议为OSS Bucket开启[版本控制](../../../../oss/documents/user-guide/overview-78.md)。
应用稳定性风险
OOM风险：初次对大量文件（如超10万，具体取决于节点内存）进行readdir操作时（如Shell脚本中的ls命令），ossfs会因一次性加载全部元信息而消耗大量内存，可能导致进程OOM Killed，并引发挂载点不可用。
建议挂载OSS Bucket子目录或优化目录层级来规避此风险。
挂载时间延长：在应用中配置securityContext.fsgroup会导致kubelet在挂载存储卷时递归修改文件权限（chmod/chown）。若文件数量庞大，将显著延长挂载时间，可能导致 Pod 启动严重延迟。
配置此参数时，如需减少挂载时间，请参见[OSS](faq-about-oss-volumes-1.md)[存储卷挂载时间延长](faq-about-oss-volumes-1.md)。
密钥失效风险（AccessKey鉴权方式）：若PV引用的AccessKey失效或权限变更，关联应用会立即失去访问权限。
恢复访问需更新Secret中的凭证，并重启应用Pod以强制重新挂载（将导致业务中断），请在维护窗口期执行。详见[解决方案](faq-about-oss-volumes-1.md)。
成本风险
碎片成本：当传输文件大于10 MB时，ossfs会将文件分片上传。若上传因业务自身重启等特殊原因意外中断，请[手动删除碎片](../../../../oss/documents/user-guide/delete-parts.md)或[通过生命周期规则删除碎片](../../../../oss/documents/user-guide/lifecycle-rules-based-on-the-last-modified-time.md)，避免碎片占用存储空间并产生费用。
