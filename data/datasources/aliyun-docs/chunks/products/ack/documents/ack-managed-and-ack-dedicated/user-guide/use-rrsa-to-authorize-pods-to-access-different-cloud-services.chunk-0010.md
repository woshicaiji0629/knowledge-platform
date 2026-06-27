ook组件配置的更多说明，请参见[ack-pod-identity-webhook](../../product-overview/ack-pod-identity-webhook.md)。
展开查看示例代码
--- apiVersion: v1 kind: Namespace metadata: name: rrsa-demo labels: pod-identity.alibabacloud.com/injection: 'on' --- apiVersion: v1 kind: ServiceAccount metadata: name: demo-sa namespace: rrsa-demo annotations: pod-identity.alibabacloud.com/role-name: demo-role-for-rrsa --- apiVersion: v1 kind: Pod metadata: name: demo namespace: rrsa-demo spec: serviceAccountName: demo-sa containers: - image: registry.cn-hangzhou.aliyuncs.com/acs/ack-ram-tool:1.3.0 args: - rrsa - demo name: demo restartPolicy: OnFailure
执行以下命令，部署测试应用。
kubectl apply -f demo.yaml
执行以下命令，查看测试应用Pod，确认ack-pod-identity-webhook组件已为Pod自动注入所需的配置。
kubectl -n rrsa-demo get pod demo -o yaml
展开查看预期输出
apiVersion: v1 kind: Pod metadata: name: demo namespace: rrsa-demo spec: containers: - args: - rrsa - demo env: - name: ALIBABA_CLOUD_ROLE_ARN value: acs:ram::1***:role/demo-role-for-rrsa - name: ALIBABA_CLOUD_OIDC_PROVIDER_ARN value: acs:ram::1***:oidc-provider/ack-rrsa-c*** - name: ALIBABA_CLOUD_OIDC_TOKEN_FILE value: /var/run/secrets/ack.alibabacloud.com/rrsa-tokens/token - name: ALIBABA_CLOUD_STS_ENDPOINT value: sts-vpc.c
