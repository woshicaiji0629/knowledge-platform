### 简单工作流
以下示例表示：启动了一个任务Pod，使用alpine镜像，运行Shell命令echo helloworld。
在此工作流基础上，可以在args中指定多个Shell命令并执行，也可以使用自定义镜像运行镜像中的命令。
cat > helloworld.yaml << EOF apiVersion: argoproj.io/v1alpha1 kind: Workflow # new type of k8s spec metadata: generateName: hello-world- # name of the workflow spec spec: entrypoint: main # invoke the main template templates: - name: main # name of the template container: image: mirrors-ssl.aliyuncs.com/alpine:3.18 command: [ "sh", "-c" ] args: [ "echo helloworld" ] EOF argo submit helloworld.yaml
