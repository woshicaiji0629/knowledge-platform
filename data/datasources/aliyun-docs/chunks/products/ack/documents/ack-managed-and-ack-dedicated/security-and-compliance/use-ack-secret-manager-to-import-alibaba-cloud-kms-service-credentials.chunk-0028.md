### JSON格式的凭据解析
JSON中指定的Key解析
如果需要解析一个JSON格式的KMS Secret，并将其中指定的key-value键值对同步到Kubernetes Secret中，可以使用JMESPath字段。以下是一个使用JMESPath字段的样例，例如，如果在KMS凭据管家中有如下JSON格式的Secret。
{"name":"tom","friends":[{"name":"lily"},{"name":"mark"}]}
对应的ExternalSecret样例如下。当使用JMESPath字段时，必须指定以下两个子字段：
path：必选项，基于[JMESPath](https://jmespath.org/specification.html)规范解析JSON中的指定字段。
objectAlias：必选项，用于指定解析出的字段同步到Kubernetes Secret中的Key名称。
apiVersion: alibabacloud.com/v1alpha1 kind: ExternalSecret metadata: name: es-json-demo spec: provider: kms data: - key: <KMS secret name> versionStage: <KMS secret version stage> secretStoreRef: name: <secret store name> namespace: <secret store namespace> jmesPath: # Parse some fields in json string - path: "name" objectAlias: "myname" - path: "friends[0].name" objectAlias: "friendname"
JSON自解析
如果不知道凭据的具体结构，但还需要将JSON凭据解析后再存储在Secret中，可以定义dataProcess.extract字段采用JSON自解析功能，同时还可以定义dataProcess.replaceRule字段，针对解析后的字段键进行规则替换，以防止不规则的Secret data key导致无法创建Secret。
例如，如果在KMS凭据管家中有如下JSON格式的Secret。
{"/name-invalid":"lily","name-invalid/":[{"name":"mark"}]}
对应的ExternalSecret样例如下。
apiVersion: alibabacloud.com/v1alpha1 kind: ExternalSecret metadata: name: extract-secret spec: provider: kms dataProc
