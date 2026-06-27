## 方式二：通过命令行配置Service流量拓扑
新建一个使用节点池拓扑域的Service，YAML样例如下。
apiVersion: v1 kind: Service metadata: annotations: openyurt.io/topologyKeys: kubernetes.io/zone name: my-service-nodepool namespace: default spec: ports: - port: 80 protocol: TCP targetPort: 8080 selector: app: nginx sessionAffinity: None type: ClusterIP
该文章对您有帮助吗？
反馈
