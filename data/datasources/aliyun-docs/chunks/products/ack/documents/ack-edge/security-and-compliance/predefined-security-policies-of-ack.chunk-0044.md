### ACKCheckNginxPath
限制在Ingress实例spec.rules[].http.paths[].path字段中使用危险配置，Ingress-nginx 1.2.1以下版本建议开启该策略。
重要等级：high。
参数说明：无。
示例：
Constraint：
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKCheckNginxPath metadata: name: block-nginx-path spec: enforcementAction: deny match: kinds: - apiGroups: ["extensions", "networking.k8s.io"] kinds: ["Ingress"] namespaces: - "test-gatekeeper"
Allowed：
apiVersion: networking.k8s.io/v1 kind: Ingress metadata: name: good-paths namespace: test-gatekeeper spec: rules: - host: cafe.example.com http: paths: - path: /tea pathType: Prefix backend: service: name: tea-svc port: number: 80 - path: /coffee pathType: Prefix backend: service: name: coffee-svc port: number: 80
Disallowed：
apiVersion: networking.k8s.io/v1 kind: Ingress metadata: name: bad-path-secrets namespace: test-gatekeeper spec: rules: - host: cafe.example.com http: paths: - path: /var/run/secrets pathType: Prefix backend: service: name: tea-svc port: number: 80
