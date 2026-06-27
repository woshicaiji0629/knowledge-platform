### ACKExternalIPs
规则说明：限制在集群指定范围内的Service实例使用白名单范围之外的externalIPs。
重要等级：high。
参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| allowedIPs | array | externalIPs 白名单列表。 |

示例：
Constraint：
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKExternalIPs metadata: name: external-ips spec: match: kinds: - apiGroups: [""] kinds: ["Service"] namespaces: - "test-gatekeeper" parameters: allowedIPs: - "192.168.0.5"
Allowed：
apiVersion: v1 kind: Service metadata: name: my-service-3 namespace: test-gatekeeper spec: selector: app: MyApp ports: - name: http protocol: TCP port: 80 targetPort: 9376
Disallowed：
apiVersion: v1 kind: Service metadata: name: my-service namespace: test-gatekeeper spec: selector: app: MyApp ports: - name: http protocol: TCP port: 80 targetPort: 9376 externalIPs: - 80.11.XX.XX
