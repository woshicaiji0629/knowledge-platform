## 标准输出
Kubernetes集群的每条日志默认上传的字段如下所示。

| 字段名称 | 说明 |
| --- | --- |
| _time_ | 日志采集时间。 |
| _source_ | 日志源类型，stdout 或 stderr。 |
| _image_name_ | 镜像名 |
| _container_name_ | 容器名 |
| _pod_name_ | Pod 名 |
| _namespace_ | Pod 所在的命名空间 |
| _pod_uid_ | Pod 的唯一标识 |
