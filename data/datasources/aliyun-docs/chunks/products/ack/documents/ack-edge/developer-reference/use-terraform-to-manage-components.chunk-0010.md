连接。 | addons { name = "ack-virtual-node" } |
| aesm | 其他 | Intel® SGX Architectural Enclave Service Manager (Intel® SGX AESM) 是 Intel® SGX 的系统组件，主要提供了 SGX Enclave 启动支持，密钥配置、远程认证等服务。 | addons { name = "aesm" } |
| aliyun-acr-acceleration-suite | 其他 | 提供镜像按需加载加速能力的客户端插件，以 DaemonSet 形式部署在 Worker 节点上。 | addons { name = "aliyun-acr-acceleration-suite" } |
| migrate-controller | 其他 | 基于开源项目 Velero 开发的一个 Kubernetes 应用迁移的组件。 | addons { name = "migrate-controller" } |
| resource-controller | 其他 | 实现动态控制 Pod 资源的关键组件，使用 ACK Pro 集群的 CPU 拓扑感知调度需要安装此组件。 | addons { name = "resource-controller" } |
| sandboxed-container-controller | 其他 | 安全沙箱运行时提供的专用控制器组件，旨在增强和扩展安全沙箱的基本功能。 | addons { name = "sandboxed-container-controller" } |
| sandboxed-container-helper | 其他 | 为安全沙箱提供诊断和运维的组件。 | addons { name = "sandboxed-container-helper" } |
| sgx-device-plugin | 其他 | 由阿里云容器服务团队和蚂蚁金服安全计算团队针对 Intel SGX 联合开发的 Kubernetes Device Plugin，可以让您更方便地在容器中使用 SGX。 | addons { name = "sgx-device-plugin" } |
