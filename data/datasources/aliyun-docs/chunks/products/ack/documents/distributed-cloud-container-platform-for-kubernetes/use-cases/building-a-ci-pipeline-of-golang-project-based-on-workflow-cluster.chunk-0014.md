## 通过Argo CLI提交工作流
使用以下内容创建workflow.yaml文件，按照[模板参数说明](building-a-ci-pipeline-of-golang-project-based-on-workflow-cluster.md)将参数值修改为您实际使用的参数值。
apiVersion: argoproj.io/v1alpha1 kind: Workflow metadata: generateName: ci-go-v1- labels: workflows.argoproj.io/workflow-template: ackone-ci spec: arguments: parameters: - name: repo_url value: https://github.com/ivan-cai/echo-server.git - name: repo_name value: echo-server - name: target_branch value: main - name: container_image value: "test-registry.cn-hongkong.cr.aliyuncs.com/acs/echo-server" - name: container_tag value: "v1.0.0" - name: dockerfile value: ./Dockerfile - name: enable_suffix_commitid value: "true" - name: enable_test value: "true" workflowTemplateRef: name: ci-go-v1 clusterScope: true
执行以下命令提交工作流。
argo submit workflow.yaml
