## 强制使用按量计费ECI运行工作流
在成本优先模式下，如需运行关键任务，不希望使用抢占式ECI实例。您可以设置工作流使用按量计费ECI实例运行工作流。
配置Container的requests和limits字段，示例代码如下。
apiVersion: argoproj.io/v1alpha1 kind: Workflow # new type of k8s spec. metadata: generateName: hello-world- # name of the workflow spec. spec: entrypoint: whalesay # invoke the whalesay template. templates: - name: whalesay # name of the template. container: image: docker/whalesay command: [ cowsay ] args: [ "hello world" ] resources: requests: cpu: 0.5 memory: 1Gi limits: cpu: 0.5 memory: 1Gi
该文章对您有帮助吗？
反馈
