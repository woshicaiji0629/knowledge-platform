### ACKRequiredLabels
规则说明：校验 Pod 是否包含特定的标签（Labels），并确保标签值符合预定义格式。支持为每个标签键（Key）指定一个正则表达式，用于验证其值（Value）。还可通过optional来控制标签校验的强制性。
重要等级：low。
参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| allowedRegex | string | Label 白名单的正则表达式。 |
| key | string | 待校验的标签 Key。 |
| optional | bool | 是否允许 Pod 缺少此标签。 true ：允许缺少，仅在标签存在时校验。包含时，其值必须通过正则校验。 false ：不允许缺少，标签必须存在且通过校验。 |

示例：
Constraint：
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKRequiredLabels metadata: name: must-have-label-test spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: - "test-gatekeeper" parameters: labels: - key: test allowedRegex: "^test.*$" - key: env allowedRegex: "^(dev|prod)$" optional: true
Allowed：
apiVersion: v1 kind: Pod metadata: creationTimestamp: null name: test namespace: test-gatekeeper labels: 'test': 'test_233' spec: containers: - name: mycontainer image: redis
Disallowed：
apiVersion: v1 kind: Pod metadata: creationTimestamp: null name: bad2 namespace: test-gatekeeper labels: 'test': '233' 'env': 'invalid' spec: containers: - name: mycontainer image: redis
