## 文本日志
K8s每条容器文本日志默认包含的字段如下表所示。

| 字段名称 | 说明 |
| --- | --- |
| __tag__:__hostname__ | 容器宿主机的名称。 |
| __tag__:__path__ | 容器内日志文件的路径。 |
| __tag__:_container_ip_ | 容器的 IP 地址。 |
| __tag__:_image_name_ | 容器使用的镜像名称。 说明 若存在多个相同 Hash 但名称或 Tag 不同的镜像，采集配置将根据 Hash 选择其中一个名称进行采集，无法确保所选名称与 YAML 文件中定义的一致。 |
| __tag__:_pod_name_ | Pod 的名称。 |
| __tag__:_namespace_ | Pod 所属的命名空间。 |
| __tag__:_pod_uid_ | Pod 的唯一标识符（UID）。 |
