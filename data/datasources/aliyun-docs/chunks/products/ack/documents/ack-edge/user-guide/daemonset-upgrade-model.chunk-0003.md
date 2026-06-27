### AdvancedRollingUpdate升级模型
以下示例代码为AdvancedRollingUpdate升级示例，在示例中创建了一个名为nginx-daemonset的DaemonSet，使用AdvancedRollingUpdate升级模型，并且在滚动升级过程中最多允许30%的Pod不可用。
cat <<EOF | kubectl apply -f - apiVersion: apps/v1 kind: DaemonSet metadata: name: nginx-daemonset annotations: apps.openyurt.io/update-strategy: AdvancedRollingUpdate apps.openyurt.io/max-unavailable: 30% spec: selector: matchLabels: app: nginx updateStrategy: type: OnDelete template: metadata: labels: app: nginx spec: containers: - name: nginx image: nginx:1.19.4 EOF
