# 创建 CRD apiVersion: apiextensions.k8s.io/v1 kind: CustomResourceDefinition metadata: name: simplestthings.example.com spec: group: example.com scope: Namespaced names: plural: simplestthings singular: simplestthing kind: SimplestThing versions: - name: v1 served: true storage: true schema: openAPIV3Schema: type: object properties: spec: type: object properties: message: type: string --- # 创建 CR 实例 apiVersion: example.com/v1 kind: SimplestThing metadata: name: my-simple-thing namespace: default labels: protected: "false" spec: message: "Hello"
尝试删除该 CRD。
kubectl delete crd simplestthings.example.com
查看删除操作是否被策略拦截，并返回明确的错误信息。
预期输出：
Error from server (Forbidden): admission webhook "delete.validation.gatekeeper.sh" denied the request: [block-crd-deletion-rule] The CRD simplestthings.example.com is not allowed to be deleted. Reason: It is not allowed to delete a CRD object when it contains a collection of custom resources. Current existing custom resources: my-simple-thing, etc.
