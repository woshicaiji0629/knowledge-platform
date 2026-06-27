## 1.26之前版本
创建一个Workload模板为Deployment的UnitedDeployment部署实例。
完整的YAML示例模板如下：
apiVersion: apps.kruise.io/v1alpha1 kind: UnitedDeployment metadata: name: example namespace: default spec: revisionHistoryLimit: 5 selector: matchLabels: app: example template: deploymentTemplate: metadata: creationTimestamp: null labels: app: example spec: selector: matchLabels: app: example template: metadata: creationTimestamp: null labels: app: example spec: containers: - image: nginx:1.19.3 imagePullPolicy: Always name: nginx dnsPolicy: ClusterFirst restartPolicy: Always topology: subsets: - name: cloud nodeSelectorTerm: matchExpressions: - key: alibabacloud.com/nodepool-id operator: In values: - np4b9781c40f0e46c581b2cf2b6160**** replicas: 2 - name: edge nodeSelectorTerm: matchExpressions: - key: alibabacloud.com/nodepool-id operator: In values: - np47832359db2e4843aa13e8b76f83**** replicas: 2 tolerations: - effect: NoSchedule key: apps.openyurt.io/taints operator: Exists
相关字段的解释如下表所示：
