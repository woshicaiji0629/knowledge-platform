om" # 需要替换<your region id>为您OSS的地域ID，例如华北2（北京）地域为：oss-cn-beijing-internal.aliyuncs.com。 otherOpts: "-o umask=022 -o max_stat_cache_size=1000000 -o allow_other" path: "/" #挂载bucket根目录，也可以设置此参数挂载bucket下子目录，例如: path: "testdir/testdir1" --- apiVersion: v1 kind: PersistentVolumeClaim metadata: name: pvc-oss namespace: default spec: accessModes: - ReadWriteMany resources: requests: storage: 5Gi selector: matchLabels: alicloud-pvname: pv-oss
可选参数：
您可以为OSS存储卷输入定制化参数，格式为-o *** -o ***，例如-o umask=022 -o max_stat_cache_size=1000000 -o allow_other。
umask：用于更改ossfs读文件的权限。例如，设置umask=022后，ossfs文件的权限都会变更为755。通过SDK、OSS控制台等其他方式上传的文件在ossfs中默认权限均为640。因此，建议您在读写分离场景中配置umask权限。
max_stat_cache_size：用于指定文件元数据的缓存空间，可缓存多少个文件的元数据。默认值为100,000，缓存约占内存40MB。
元数据缓存可明显加快数据的遍历与读取速度，但若通过其他例如OSS、SDK、控制台、ossutil等方式修改文件，可能会导致元数据未被及时更新。若您的业务有强数据一致性需求，可将该值调整为0，关闭元数据缓存。
allow_other：赋予计算机上其他用户访问挂载目录的权限，但不包含目录内的文件。
更多可选参数，请参见[选项列表](../../../../oss/documents/developer-reference/common-options.md)。
将下方示例保存到oss-workflow.yaml，执行kubectl apply -f oss-workflow.yaml创建工作流使用存储卷。
展开查看在工作流中挂载使用OSS存储卷的YAML示例代码
apiVersion: argoproj.io/v1alpha1 kind: Workflow metadata: generateName: volumes-existing- namespace: default spec: entrypoint: volu
