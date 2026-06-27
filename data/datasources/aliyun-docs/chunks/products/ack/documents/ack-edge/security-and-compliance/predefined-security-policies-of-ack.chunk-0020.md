示例：
Constraint：
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKProtectCoreDNS metadata: name: coredns-protect-rule spec: enforcementAction: deny match: kinds: - apiGroups: ["*"] kinds: ["Deployment", "Service", "Scale", "ConfigMap" ] scope: "Namespaced" namespaces: ["kube-system"] parameters: min_replicas: 2
Allowed：
apiVersion: apps/v1 kind: Deployment metadata: name: coredns namespace: kube-system spec: replicas: 3 selector: matchLabels: k8s-app: kube-dns template: metadata: labels: k8s-app: kube-dns spec: containers: - name: coredns image: registry-cn-hangzhou-vpc.ack.aliyuncs.com/acs/coredns:latest imagePullPolicy: IfNotPresent
Disallowed：
apiVersion: apps/v1 kind: Deployment metadata: name: coredns namespace: kube-system spec: replicas: 1 selector: matchLabels: k8s-app: kube-dns template: metadata: labels: k8s-app: kube-dns spec: containers: - name: coredns image: registry-cn-hangzhou-vpc.ack.aliyuncs.com/acs/coredns:latest imagePullPolicy: IfNotPresent --- apiVersion: v1 data: Corefile: "" kind: ConfigMap metadata: name: coredns namespace: kube-system --- apiVersion: v1 kind: Service metadata: labels: k8s-app: kube-dns kubernetes.io/cluster-service: "true" kubernetes.
