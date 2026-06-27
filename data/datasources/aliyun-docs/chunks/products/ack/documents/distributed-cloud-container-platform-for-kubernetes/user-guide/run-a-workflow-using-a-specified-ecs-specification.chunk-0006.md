### AMD示例
apiVersion: argoproj.io/v1alpha1 kind: Workflow metadata: generateName: hello-world- spec: entrypoint: whalesay templates: - name: whalesay metadata: annotations: k8s.aliyun.com/eci-use-specs: "ecs.c6a.xlarge" # 指定支持的ECS AMD规格。 container: image: docker/whalesay command: [ cowsay ] args: [ "hello world" ]
该文章对您有帮助吗？
反馈
