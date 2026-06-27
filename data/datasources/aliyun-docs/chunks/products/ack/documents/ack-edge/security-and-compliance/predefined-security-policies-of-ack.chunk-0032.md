### ASMSidecarInjectionEnforced
规则说明：限制Pod必须注入ASM Sidecar。
重要等级：high
参数说明：无。
示例：
Constraint：
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ASMSidecarInjectionEnforced metadata: name: asm-sidecar-injectionen-forced spec: enforcementAction: deny match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: ["test-gatekeeper"]
Allowed：
apiVersion: v1 kind: Pod metadata: name: sidecar-injection namespace: test-gatekeeper spec: containers: - name: test image: test - name: istio-proxy image: xxx/proxyv2:xxx
Disallowed：
apiVersion: v1 kind: Pod metadata: name: sidecar-injection namespace: test-gatekeeper spec: containers: - name: test image: test
