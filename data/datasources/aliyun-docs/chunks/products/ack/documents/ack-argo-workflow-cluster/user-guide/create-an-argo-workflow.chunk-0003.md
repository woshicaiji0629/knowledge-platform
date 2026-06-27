### 步骤二：创建工作流
创建并复制下方示例到helloworld-workflow.yaml文件。
apiVersion: argoproj.io/v1alpha1 kind: Workflow metadata: generateName: helloworld-- # 工作流名称前缀 spec: entrypoint: helloworld # 指定入口工作流模板 templates: - name: helloworld container: image: mirrors-ssl.aliyuncs.com/busybox:latest command: - sh - -c args: - echo "Hello, world!"; sleep 60;
提交工作流。
argo submit helloworld-workflow.yaml
查看工作流状态。
获取工作流列表。
argo list
预期输出：
NAME STATUS AGE DURATION PRIORITY helloworld-lgdpp Succeeded 2m 37s 0
查看工作流状态。
argo get helloworld-lgdpp
预期输出：
Name: hello-world-lgdpp Namespace: default ServiceAccount: unset (will run with the default ServiceAccount) Status: Succeeded Conditions: PodRunning False Completed True .... Duration: 1 minute 46 seconds Progress: 1/1 ResourcesDuration: 17s*(1 cpu),17s*(100Mi memory) STEP TEMPLATE PODNAME DURATION MESSAGE ✔ hello-world-lgdpp helloworld hello-world-lgdpp 1m
