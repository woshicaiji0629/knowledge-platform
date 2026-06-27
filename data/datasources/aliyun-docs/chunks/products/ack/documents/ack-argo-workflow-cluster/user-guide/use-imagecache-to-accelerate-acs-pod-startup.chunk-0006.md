## 使用镜像缓存

| Pod 注解 | 说明 |
| --- | --- |
| image.alibabacloud.com/enable-image-cache: "true" | 为 Pod 开启镜像缓存匹配能力。 |

功能开启后，Pod将自动匹配使用最优的镜像缓存：
镜像匹配度：选择镜像名完全匹配的镜像缓存。
创建时间：优先选择创建时间最近且可用的镜像缓存。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择工作负载>容器组，然后单击使用YAML创建资源。
使用以下YAML创建Pod并添加注解开启镜像缓存匹配能力。
请确保网络配置和密钥信息能够访问到所配置的镜像仓库，目前支持的imagePullPolicy为Always。apiVersion: v1 kind: Pod metadata: labels: name: hello-pod name: hello-pod annotations: image.alibabacloud.com/enable-image-cache: "true" spec: containers: - image: egs-registry.cn-hangzhou.cr.aliyuncs.com/egs/vllm:0.9.0.1-pytorch2.7-cu128-20250612 # 请替换为实际镜像地址 command: ["/bin/sleep", "infinity"] imagePullPolicy: Always name: hello-pod ports: - containerPort: 8080 protocol: TCP resources: {} securityContext: capabilities: {} privileged: false terminationMessagePath: /dev/termination-log dnsPolicy: ClusterFirst restartPolicy: Always
创建成功后，单击Pod名称进入基本信息页面。开启镜像缓存匹配能力之后，创建的Pod会根据镜像名称尝试匹配镜像缓存，匹配成功的Pod会自动追加当前匹配的镜像缓存的注解。

| 功能 | 参数 | 示例值 | 说明 |
| --- | --- | --- | --- |
| 镜像缓存命中信息 | image.alibabacloud.com/matched-image-caches | [{"imageCacheId":"imc-*****t15xuii6tz*****","size":30}] | 命中的镜像缓存 ID 及大小（GiB）。 |

该文章对您有帮助吗？
反馈
