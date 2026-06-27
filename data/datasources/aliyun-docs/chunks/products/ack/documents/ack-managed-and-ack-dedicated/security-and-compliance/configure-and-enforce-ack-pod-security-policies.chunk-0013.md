场景示例：防止CRD被删除
本示例展示利用 ack-policy-external-provider 实现一个常见的高级策略：当 CRD 仍然存在关联的 CR 实例时，禁止删除该 CRD。
此策略已作为内置规则集成到策略库中，无需手动部署。仅作为原理说明。
策略逻辑
触发：Gatekeeper 监听到DELETECRD 操作。
查询：Rego 策略通过external_data调用 ack-policy-external-provider。
判断：ack-policy-external-provider 根据请求参数查询集群中是否存在对应的 CR 实例。
决策：如果查询结果返回了至少一个 CR 实例，ack-policy-external-provider 会将结果返回给 Rego 策略，策略最终会deny(拒绝) 本次删除操作。
策略模板（ConstraintTemplate）
定义策略的逻辑。
apiVersion: templates.gatekeeper.sh/v1beta1 kind: ConstraintTemplate metadata: name: blockcrddeletion annotations: meta.helm.sh/release-name: gatekeeper meta.helm.sh/release-namespace: kube-system metadata.gatekeeper.sh/version: 1.0.0 labels: app.kubernetes.io/managed-by: Helm spec: crd: spec: names: kind: BlockCrdDeletion validation: legacySchema: true targets: - target: admission.k8s.gatekeeper.sh rego: | package block_crd_deletion violation[{"msg": msg}] { before(input.review.operation) response := handle(input.review) msg := after(response) } before(operation) { operation == "DELETE" } handle(review) = response { customrequest := { "action": "ListK8sResource", "namespaced": false, "group": review.object.spec.group, "version": "", "resource": review.object.spec.names.plural, "reque
