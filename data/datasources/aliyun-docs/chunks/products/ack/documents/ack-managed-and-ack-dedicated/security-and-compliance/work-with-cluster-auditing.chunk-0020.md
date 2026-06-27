ettings.k8s.io" - group: "storage.k8s.io" # 已知的Kunernetes API默认设置为RequestResponse，返回请求体和响应体。 - level: RequestResponse resources: - group: "" # core - group: "admissionregistration.k8s.io" - group: "apps" - group: "authentication.k8s.io" - group: "authorization.k8s.io" - group: "autoscaling" - group: "batch" - group: "certificates.k8s.io" - group: "extensions" - group: "networking.k8s.io" - group: "policy" - group: "rbac.authorization.k8s.io" - group: "settings.k8s.io" - group: "storage.k8s.io" # 其余请求都默认设置为Metadata。 - level: Metadata
说明
在收到请求后，日志不立即开始记录，等待返回体Header发送后才开始记录。
对于大量冗余的kube-proxy watch请求、kubelet和system:nodes对节点的Get请求、kube组件在kube-system下对于endpoint的操作、以及API Server对Namespaces的Get请求等，系统不进行审计。
对于authentication、rbac、certificates、autoscaling、storage等敏感接口，系统根据读写记录相应的请求体和返回体。
