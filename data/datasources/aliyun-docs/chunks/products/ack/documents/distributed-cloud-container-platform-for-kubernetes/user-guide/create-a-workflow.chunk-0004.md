### 使用阿里云Argo CLI操作工作流
使用以下内容，创建helloworld-workflow.yaml文件。
apiVersion: argoproj.io/v1alpha1 kind: Workflow # new type of k8s spec. metadata: generateName: hello-world- # name of the workflow spec. spec: entrypoint: whalesay # invoke the whalesay template. templates: - name: whalesay # name of the template. container: image: docker/whalesay command: [ cowsay ] args: [ "hello world" ]
执行以下命令，提交工作流。
argo submit helloworld-workflow.yaml
查看工作流状态。
执行以下命令，获取工作流列表。
argo list
预期输出：
NAME STATUS AGE DURATION PRIORITY hello-world-lgdpp Succeeded 2m 37s 0
执行以下命令，查看工作流状态。
argo get hello-world-lgdpp
预期输出：
Name: hello-world-lgdpp Namespace: default ServiceAccount: unset (will run with the default ServiceAccount) Status: Succeeded Conditions: PodRunning False Completed True .... Duration: 37 seconds Progress: 1/1 ResourcesDuration: 17s*(1 cpu),17s*(100Mi memory) STEP TEMPLATE PODNAME DURATION MESSAGE ✔ hello-world-lgdpp whalesay hello-world-lgdpp 27s
