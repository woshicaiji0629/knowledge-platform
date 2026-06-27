### GPU示例
apiVersion: argoproj.io/v1alpha1 kind: Workflow metadata: generateName: hello-world- spec: entrypoint: whalesay templates: - name: whalesay metadata: annotations: k8s.aliyun.com/eci-use-specs: ecs.gn5i-c4g1.xlarge # 指定支持的ECS GPU规格。 container: image: docker/whalesay command: [ cowsay ] args: [ "hello world" ]
