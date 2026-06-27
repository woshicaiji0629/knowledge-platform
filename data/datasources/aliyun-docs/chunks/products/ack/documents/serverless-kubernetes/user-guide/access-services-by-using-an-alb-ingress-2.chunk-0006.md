## 步骤二：部署服务
创建并拷贝以下内容到cafe-service.yaml文件中，用于部署两个名称分别为coffee和tea的Deployment，以及两个名称分别为coffee和tea的Service。
展开查看完整的YAML文件
apiVersion: apps/v1 kind: Deployment metadata: name: coffee spec: replicas: 2 selector: matchLabels: app: coffee template: metadata: labels: app: coffee spec: containers: - name: coffee image: registry.cn-hangzhou.aliyuncs.com/acs-sample/nginxdemos:latest ports: - containerPort: 80 --- apiVersion: v1 kind: Service metadata: name: coffee-svc spec: ports: - port: 80 targetPort: 80 protocol: TCP selector: app: coffee clusterIP: None --- apiVersion: apps/v1 kind: Deployment metadata: name: tea spec: replicas: 1 selector: matchLabels: app: tea template: metadata: labels: app: tea spec: containers: - name: tea image: registry.cn-hangzhou.aliyuncs.com/acs-sample/nginxdemos:latest ports: - containerPort: 80 --- apiVersion: v1 kind: Service metadata: name: tea-svc labels: spec: ports: - port: 80 targetPort: 80 protocol: TCP selector: app: tea clusterIP: None
执行以下命令，部署两个Deployment和两个Service。
kubectl apply -f cafe-service.yaml
预期输出：
deployment "coffee" created service "coffee-svc" created deployment "tea" created service "tea-svc" created
查看创建的应用和服务的状态。
执行以下命令，查看应用的状态。
kubect
