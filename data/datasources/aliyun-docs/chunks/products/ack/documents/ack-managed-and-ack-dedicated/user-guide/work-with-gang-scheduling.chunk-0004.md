# PodGroup CRD spec apiVersion: scheduling.sigs.k8s.io/v1alpha1 kind: PodGroup metadata: name: nginx spec: scheduleTimeoutSeconds: 10 minMember: 3 --- # 为容器添加标签“pod-group.scheduling.sigs.k8s.io/name”。 labels: pod-group.scheduling.sigs.k8s.io/name: nginx
在创建的Pod处通过设置annotations的形式设置min-available和name。不支持koordinator API中的total-number和mode参数。
annotations: gang.scheduling.koordinator.sh/name: "gang-example" gang.scheduling.koordinator.sh/min-available: "2"
说明
属于同一个PodGroup的Pod必须保持相同的优先级。
