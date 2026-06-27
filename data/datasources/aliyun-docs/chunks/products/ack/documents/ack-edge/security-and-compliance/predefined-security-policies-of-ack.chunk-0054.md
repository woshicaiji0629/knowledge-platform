### ACKPSPForbiddenSysctls
规则说明：限制在集群指定范围内部署的Pod禁止的Sysctl范围。
重要等级：high。
参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| forbiddenSysctls | array | Pod 中禁止的 sysctl 列表。 |

示例：
Constraint：
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKPSPForbiddenSysctls metadata: name: psp-forbidden-sysctls spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: - "test-gatekeeper" parameters: forbiddenSysctls: # - "*" # * may be used to forbid all sysctls - "kernel.*"
Allowed：
apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: good-2 namespace: test-gatekeeper spec: securityContext: sysctls: - name: 'net.ipv4.tcp_syncookies' value: "65536" containers: - image: test name: test
Disallowed：
apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: bad-1 namespace: test-gatekeeper spec: securityContext: sysctls: - name: 'kernel.shm_rmid_forced' value: '1024' containers: - image: test name: test
