### ACKBlockInternetLoadBalancer
规则说明：限制创建公网类型的LoadBalancer Service。
重要等级：high。
参数说明：无。
示例：
Constraint：
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKBlockInternetLoadBalancer metadata: name: block-internet-load-balancer spec: match: kinds: - apiGroups: [""] kinds: ["Service"] namespaces: ["test-gatekeeper"]
Allowed：
apiVersion: v1 kind: Service metadata: name: my-service namespace: non-test-gatekeeper annotations: 'service.beta.kubernetes.io/alibaba-cloud-loadbalancer-address-type': 'intranet' spec: selector: app: MyApp ports: - name: http protocol: TCP port: 80 targetPort: 9376 type: LoadBalancer
Disallowed：
apiVersion: v1 kind: Service metadata: name: bad-service-2 namespace: test-gatekeeper annotations: 'service.beta.kubernetes.io/alibaba-cloud-loadbalancer-address-type': 'internet' spec: type: LoadBalancer selector: app: MyApp ports: - name: http protocol: TCP port: 80 targetPort: 9376
