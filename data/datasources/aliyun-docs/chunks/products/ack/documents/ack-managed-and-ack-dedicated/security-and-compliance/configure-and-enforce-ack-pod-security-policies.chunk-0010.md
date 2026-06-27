### 通过ack-policy-external-provider实现跨资源验证
默认情况下，Gatekeeper 策略的决策依据仅限于被审查的资源本身。但在许多复杂的安全场景中，策略需要引用集群中的其他资源状态才能做出正确判断。
托管组件 ack-policy-external-provider 可充当 Gatekeeper 的外部数据源，让策略开发者可以在策略代码（Rego）中查询Kubernetes资源（如内置的CRD保护策略）。
重要
ack-policy-external-provider需配合[gatekeeper](../../product-overview/gatekeeper.md)使用。请确保集群中已部署 gatekeeper。
安装和配置ack-policy-external-provider
在[ACK](https://cs.console.aliyun.com)[集群列表](https://cs.console.aliyun.com)页面，单击目标集群名称，在集群详情页左侧导航栏，单击组件管理。
搜索并定位ack-policy-external-provider，按照页面提示完成配置。
ProviderPodNumber：组件的实例个数。
ProtectedKinds：添加需要保护 CRD 对应的资源类型。
CRD 删除保护需要检查集群中是否存在该资源类型的实例。遵循最小化权限原则，ack-policy-external-provider默认不具备该检查所需的查询权限，需手动配置。
设置ProviderPodNumber（副本数量，默认为1）。在ProtectedKinds区域，输入资源类型名称（如pods、policies、customresources），单击添加可增加多个条目，单击删除可移除条目，完成后单击确认。
接口定义及参数说明
ack-policy-external-provider 实现了一个标准的 Gatekeeper 外部数据 Provider。可在 Rego 策略模板中，通过调用external_data函数并指定provider: ack-policy-external-data-provider，来向该组件发起资源查询请求。
请求参数以 JSON 格式定义，示例如下。
// 示例 1 { "action": "ListK8sResource", "namespaced": false, "group": "", "version": "v1", "resource": "persistentvolumeclaims" "requestID": review.uid, "userInfo": review.userInfo, "requestFrom": "PVCProtector", "labelSel
