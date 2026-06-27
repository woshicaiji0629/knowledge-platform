### ACKBlockNodePort
规则说明：限制在集群指定范围内使用NodePort类型的Service。
重要等级：low。
参数说明：无。
示例：
Constraint：
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKBlockNodePort metadata: name: block-node-port spec: match: kinds: - apiGroups: [""] kinds: ["Service"] namespaces: - "test-gatekeeper"
Allowed：
apiVersion: v1 kind: Service metadata: name: my-service-1 namespace: test-gatekeeper spec: selector: app: MyApp ports: - name: http protocol: TCP port: 80 targetPort: 9376
Disallowed：
apiVersion: v1 kind: Service metadata: name: my-service namespace: test-gatekeeper spec: type: NodePort selector: app: MyApp ports: - name: http protocol: TCP port: 80 targetPort: 9376
