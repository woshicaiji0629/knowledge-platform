### ACKBlockLoadBalancer
规则说明：限制在指定集群范围内部署LoadBalancer类型的Service。
重要等级：high。
参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| restrictedNamespaces | array | 禁止资源部署在该参数声明的列表中。 |

示例：
Constraint：
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKBlockLoadBalancer metadata: name: block-load-balancer spec: match: kinds: - apiGroups: [""] kinds: ["Service"] namespaces: - "test-gatekeeper"
Allowed：
apiVersion: v1 kind: Service metadata: name: my-service-1 namespace: test-gatekeeper spec: selector: app: MyApp ports: - name: http protocol: TCP port: 80 targetPort: 9376
Disallowed：
apiVersion: v1 kind: Service metadata: name: my-service namespace: test-gatekeeper spec: type: LoadBalancer selector: app: MyApp ports: - name: http protocol: TCP port: 80 targetPort: 9376
