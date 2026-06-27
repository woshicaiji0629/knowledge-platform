### 验证共享存储
在一个Pod中创建文件，然后在另一个Pod中查看，以验证共享存储特性。
查看Pod信息，在输出中获取Pod名称。
kubectl get pod -l app=nginx
在一个Pod中创建tmpfile文件。 以名为oss-workload-66fbb85b67-d****的Pod为例：
ReadWriteMany：在/data路径下创建tmpfile文件。
kubectl exec oss-workload-66fbb85b67-d**** -- touch /data/tmpfile
ReadOnlyMany：通过[OSS](https://oss.console.aliyun.com/bucket)[控制台](https://oss.console.aliyun.com/bucket)、[cp（上传文件）](../../../../oss/documents/developer-reference/upload-objects-6.md)等方式上传tmpfile文件至OSS Bucket对应的路径。
在另一个Pod挂载路径下查看文件。
以名为oss-workload-66fbb85b67-l****、挂载路径为data的Pod为例。
kubectl exec oss-workload-66fbb85b67-l**** -- ls /data | grep tmpfile
预期输出如下，Pod挂载路径下均存在此文件，表明两个Pod可共享数据。
tmpfile若无预期输出，请确认[CSI](../../product-overview/csi-plugin.md)[组件](../../product-overview/csi-plugin.md)版本是否为v1.20.7及以上版本。
