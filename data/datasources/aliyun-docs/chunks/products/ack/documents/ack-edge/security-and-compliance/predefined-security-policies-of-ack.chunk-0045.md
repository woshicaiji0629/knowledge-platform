### ACKCheckNginxAnnotation
限制在Ingress实例metadata.annotations字段中使用危险配置，Ingress-nginx 1.2.1以下版本建议开启该策略。
重要等级：high。
参数说明：无。
示例：
Constraint：
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKCheckNginxAnnotation metadata: name: block-nginx-annotation spec: match: kinds: - apiGroups: ["extensions", "networking.k8s.io"] kinds: ["Ingress"] namespaces: - "test-gatekeeper"
Allowed：
apiVersion: networking.k8s.io/v1 kind: Ingress metadata: name: good-annotations namespace: test-gatekeeper annotations: nginx.org/good: "value" spec: rules: - host: cafe.example.com http: paths: - path: /tea pathType: Prefix backend: service: name: tea-svc port: number: 80 - path: /coffee pathType: Prefix backend: service: name: coffee-svc port: number: 80
Disallowed：
apiVersion: networking.k8s.io/v1 kind: Ingress metadata: name: var-run-secrets namespace: test-gatekeeper annotations: nginx.org/bad: "/var/run/secrets" spec: rules: - host: cafe.example.com http: paths: - path: /tea pathType: Prefix backend: service: name: tea-svc port: number: 80 - path: /coffee pathType: Prefix backend: service: name: coffee-svc port: number: 80
