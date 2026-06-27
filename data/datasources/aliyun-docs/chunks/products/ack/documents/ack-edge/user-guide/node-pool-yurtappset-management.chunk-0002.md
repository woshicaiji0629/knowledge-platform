## 1.26及之后版本
创建一个Workload模板为Deployment的YurtAppSet应用集实例。
完整的YAML示例模板如下：
apiVersion: apps.openyurt.io/v1beta1 kind: YurtAppSet metadata: name: example namespace: default spec: revisionHistoryLimit: 5 pools: - np1xxxxxx - np2xxxxxx nodepoolSelector: matchLabels: yurtappset.openyurt.io/type: "nginx" workload: workloadTemplate: deploymentTemplate: metadata: labels: app: example spec: replicas: 2 selector: matchLabels: app: example template: metadata: labels: app: example spec: containers: - image: nginx:1.19.1 imagePullPolicy: Always name: nginx workloadTweaks: - pools: - np2xxxxxx tweaks: replicas: 3 containerImages: - name: nginx targetImage: nginx:1.20.1 patches: - path: /metadata/labels/test operation: add value: test
相关字段的解释如下表所示：
