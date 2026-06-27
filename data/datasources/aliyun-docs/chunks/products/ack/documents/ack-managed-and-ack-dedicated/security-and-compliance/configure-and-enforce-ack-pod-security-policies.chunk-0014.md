est := { "action": "ListK8sResource", "namespaced": false, "group": review.object.spec.group, "version": "", "resource": review.object.spec.names.plural, "requestID": review.uid, "userInfo": review.userInfo, "requestFrom": "BlockCrdDeletion", "labelSelector": "protected", "limit": 1 } request_keys := [json.marshal(customrequest)] response := external_data({ "provider": "ack-policy-external-data-provider", "keys": request_keys }) } after(response) = msg { count(response.responses[0]) > 0 msg := sprintf( "The CRD %v is not allowed to be deleted. Reason: It is not allowed to delete a CRD object when it contains a collection of custom resources. Current existing custom resources: %v, etc.", [input.review.name, response.responses[0][0]] ) }
策略实例（Constraint）
将模板应用到具体资源。本示例应用到所有CRD。
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: BlockCrdDeletion metadata: name: block-crd-deletion-rule spec: enforcementAction: deny match: kinds: - apiGroups: - '*' kinds: - CustomResourceDefinition
效果验证
创建一个测试 CRD 和对应的 CR 实例：
