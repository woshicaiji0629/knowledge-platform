# 使用存储卷-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/distributed-cloud-container-platform-for-kubernetes/user-guide/use-volumes

# 使用存储卷
本文介绍如何在工作流集群中挂载使用存储卷。
## 使用说明
在工作流集群中支持使用OSS存储卷、NAS存储卷和CPFS2.0存储卷。
## 使用OSS存储卷
使用以下示例代码，创建OSS存储卷。
更多信息，请参见[使用](../../ack-managed-and-ack-dedicated/user-guide/mount-statically-provisioned-oss-volumes.md)[ossfs 1.0](../../ack-managed-and-ack-dedicated/user-guide/mount-statically-provisioned-oss-volumes.md)[静态存储卷](../../ack-managed-and-ack-dedicated/user-guide/mount-statically-provisioned-oss-volumes.md)。如果使用其他类型存储卷，请替换对应的参数。
展开查看使用OSS存储卷的YAML示例代码
apiVersion: v1 kind: Secret metadata: name: oss-secret namespace: default stringData: akId: <yourAccessKey ID> # akId需要替换为您的AccessKey ID。 akSecret: <yourAccessKey Secret> # akSecret需要替换为您的AccessKey Secret。 --- apiVersion: v1 kind: PersistentVolume metadata: name: pv-oss labels: alicloud-pvname: pv-oss spec: capacity: storage: 5Gi accessModes: - ReadWriteMany persistentVolumeReclaimPolicy: Retain csi: driver: ossplugin.csi.alibabacloud.com volumeHandle: pv-oss # 需要和PV名字一致。 nodePublishSecretRef: name: oss-secret namespace: default volumeAttributes: bucket: <your bucket name> # 需要替换为您的Bucket名称。 url: "oss-<your region id>-internal.aliyuncs.com" # 需要替换<your region id>为您OSS的地域ID，例如华北2（北京）地域为：oss-cn-beijing-internal.aliyuncs.com。 otherOpts: "-o umask=022 -o max_stat_cache_size=1000000 -o allow_other" path: "/" #挂载bucket根目录，也可以设置此参数挂载bucket下子目录，例如: path: "testdir/testdir1" --- apiVersion: v1 kind: PersistentVolumeClaim metadata: name: pvc-oss namespace: default spec: accessModes: - ReadWriteMany resources: requests: storage: 5Gi selector: matchLabels: alicloud-pvname: pv-oss
可选参数：
您可以为OSS存储卷输入定制化参数，格式为-o *** -o ***，例如-o umask=022 -o max_stat_cache_size=1000000 -o allow_other。
umask：用于更改ossfs读文件的权限。例如，设置umask=022后，ossfs文件的权限都会变更为755。通过SDK、OSS控制台等其他方式上传的文件在ossfs中默认权限均为640。因此，建议您在读写分离场景中配置umask权限。
max_stat_cache_size：用于指定文件元数据的缓存空间，可缓存多少个文件的元数据。默认值为100,000，缓存约占内存40MB。
元数据缓存可明显加快数据的遍历与读取速度，但若通过其他例如OSS、SDK、控制台、ossutil等方式修改文件，可能会导致元数据未被及时更新。若您的业务有强数据一致性需求，可将该值调整为0，关闭元数据缓存。
allow_other：赋予计算机上其他用户访问挂载目录的权限，但不包含目录内的文件。
更多可选参数，请参见[选项列表](../../../../oss/documents/developer-reference/common-options.md)。
使用以下示例代码，创建工作流使用存储卷。
展开查看在工作流中挂载使用OSS存储卷的YAML示例代码
apiVersion: argoproj.io/v1alpha1 kind: Workflow metadata: generateName: volumes-existing- namespace: default spec: entrypoint: volumes-existing-example volumes: # Pass my-existing-volume as an argument to the volumes-existing-example template. # Same syntax as k8s Pod spec. - name: workdir persistentVolumeClaim: claimName: pvc-oss templates: - name: volumes-existing-example steps: - - name: generate template: whalesay - - name: print template: print-message - name: whalesay container: image: docker/whalesay:latest command: [sh, -c] args: ["echo generating message in volume; cowsay hello world | tee /mnt/vol/hello_world.txt"] volumeMounts: - name: workdir mountPath: /mnt/vol - name: print-message container: image: alpine:latest command: [sh, -c] args: ["echo getting message from volume; find /mnt/vol; cat /mnt/vol/hello_world.txt"] volumeMounts: - name: workdir mountPath: /mnt/vol
## 使用NAS存储卷
使用以下示例代码，创建静态NAS共享卷。
展开查看使用NAS共享卷的YAML示例代码
apiVersion: v1 kind: PersistentVolume metadata: name: pv-nas labels: alicloud-pvname: pv-nas spec: capacity: storage: 100Gi accessModes: - ReadWriteMany csi: driver: nasplugin.csi.alibabacloud.com volumeHandle: pv-nas # 必须与PV Name保持一致。 volumeAttributes: server: "<your nas filesystem id>.cn-beijing.nas.aliyuncs.com" path: "/" mountOptions: - nolock,tcp,noresvport - vers=3 --- kind: PersistentVolumeClaim apiVersion: v1 metadata: name: pvc-nas spec: accessModes: - ReadWriteMany resources: requests: storage: 100Gi selector: matchLabels: alicloud-pvname: pv-nas
使用以下示例代码，在工作流中挂载和使用NAS。
展开查看在工作流中挂载使用NAS共享卷的YAML示例代码
apiVersion: argoproj.io/v1alpha1 kind: Workflow metadata: generateName: volumes-existing- namespace: default spec: entrypoint: volumes-existing-example volumes: # Pass my-existing-volume as an argument to the volumes-existing-example template. # Same syntax as k8s Pod spec. - name: workdir persistentVolumeClaim: claimName: pvc-nas templates: - name: volumes-existing-example steps: - - name: generate template: whalesay - - name: print template: print-message - name: whalesay container: image: docker/whalesay:latest command: [sh, -c] args: ["echo generating message in volume; cowsay hello world | tee /mnt/vol/hello_world.txt"] volumeMounts: - name: workdir mountPath: /mnt/vol - name: print-message container: image: alpine:latest command: [sh, -c] args: ["echo getting message from volume; find /mnt/vol; cat /mnt/vol/hello_world.txt"] volumeMounts: - name: workdir mountPath: /mnt/vol
## 使用CPFS2.0存储卷
执行以下命令，创建CPFS2.0共享卷。
展开查看使用CPFS2.0共享卷的YAML示例代码
cat << EOF | kubectl apply -f - apiVersion: v1 kind: PersistentVolume metadata: name: pv-cpfs labels: alicloud-pvname: pv-cpfs spec: accessModes: - ReadWriteOnce capacity: storage: 1000Gi csi: driver: nasplugin.csi.alibabacloud.com volumeAttributes: mountProtocol: cpfs-nfs # 挂载时，使用NFS协议进行挂载。 path: "/share" # 挂载目录必须以/share为前缀。 volumeAs: subpath server: "<your cpfs id, e.g cpfs-****>.<regionID>.cpfs.aliyuncs.com" # 为挂载点前面的域名。 volumeHandle: pv-cpfs # 必须与PV Name保持一致。 mountOptions: - rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport - vers=3 --- apiVersion: v1 kind: PersistentVolumeClaim metadata: name: pvc-cpfs spec: accessModes: - ReadWriteOnce resources: requests: storage: 1000Gi selector: matchLabels: alicloud-pvname: pv-cpfs EOF
使用以下示例代码，在工作流中挂载和使用CPFS2.0。
展开查看在工作流中挂载使用CPFS2.0共享卷的YAML示例代码
apiVersion: argoproj.io/v1alpha1 kind: Workflow metadata: generateName: volumes-existing- namespace: default spec: entrypoint: volumes-existing-example volumes: # Pass my-existing-volume as an argument to the volumes-existing-example template. # Same syntax as k8s Pod spec. - name: workdir persistentVolumeClaim: claimName: pvc-cpfs templates: - name: volumes-existing-example steps: - - name: generate template: whalesay - - name: print template: print-message - name: whalesay container: image: docker/whalesay:latest command: [sh, -c] args: ["echo generating message in volume; cowsay hello world | tee /mnt/vol/hello_world.txt"] volumeMounts: - name: workdir mountPath: /mnt/vol - name: print-message container: image: alpine:latest command: [sh, -c] args: ["echo getting message from volume; find /mnt/vol; cat /mnt/vol/hello_world.txt"] volumeMounts: - name: workdir mountPath: /mnt/vol
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
