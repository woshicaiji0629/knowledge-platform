### Kubernetes原生配置相关
请勿擅自修改Kubernetes的关键配置，例如以下文件的路径、链接和内容：
/var/lib/kubelet
/var/lib/docker
/etc/kubernetes
/etc/kubeadm
/var/lib/containerd
在YAML模板中请勿使用Kubernetes集群预留的Annotation，否则会造成资源不可用、申请失败、异常等问题。以kubernetes.io/和k8s.io/开头的Annotation为核心组件预留标签。违规示例：pv.kubernetes.io/bind-completed: "yes"。
