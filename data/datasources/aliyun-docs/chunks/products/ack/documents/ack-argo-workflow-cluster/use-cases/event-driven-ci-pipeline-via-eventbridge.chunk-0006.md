## 步骤二：使用EventBridge实现Git事件驱动CI Pipeline
[创建自定义事件总线](https://help.aliyun.com/zh/eventbridge/user-guide/manage-custom-event-buses#section-sfl-pcs-6rh)。
事件总线EventBridge与GitHub进行集成对接。具体操作，请参见[GitHub](https://help.aliyun.com/zh/eventbridge/use-cases/integrate-github)[集成](https://help.aliyun.com/zh/eventbridge/use-cases/integrate-github)。
配置事件规则（可选），以下为本示例配置内容。详细配置事件规则的方式，请参见[管理事件规则](https://help.aliyun.com/zh/eventbridge/user-guide/manage-event-rules)。
事件模式：如下设置为只触发来自release-v1分支的变更。
{ "source": [ "github.event" ], "data": { "body": { "ref": [ "refs/heads/release-v1" ] } } }
配置事件目标。
服务类型：选择容器服务Kubernetes。
集群配置文件 KubeConfig：输入工作流集群专有网络访问的KubeConfig。
YAML配置：本示例选择模板。
变量：增加workflowName，配置事件ID。
{ "workflowName": "$.id" }
模板：填入Workflow CI CR。以下示例仅供参考，请根据您的实际信息构建CR。
重要
资源配置的要求是必须明确设置name和namespace，不能使用generateName。如果资源属于默认命名空间default，也必须声明。
apiVersion: argoproj.io/v1alpha1 kind: Workflow metadata: name: ci-go-v1-eb-${workflowName} namespace: default labels: workflows.argoproj.io/workflow-template: ackone-ci spec: arguments: parameters: - name: repo_url value: https://github.com/ivan-cai/echo-server.git - name: repo_name value: echo-server - name: target_branch value: release-v1 - name: contai
