### 手动修改应用模板使用RRSA功能
您可以通过手动修改应用模板挂载应用所需的OIDC Token文件以及配置相关环境变量，在不安装ack-pod-identity-webhook组件的情况下使用RRSA功能。
应用模板示例代码如下。
展开查看应用模板示例代码
apiVersion: v1 kind: Pod metadata: name: demo namespace: rrsa-demo spec: containers: - args: - rrsa - demo env: - name: ALIBABA_CLOUD_ROLE_ARN value: <role_arn> - name: ALIBABA_CLOUD_OIDC_PROVIDER_ARN value: <oid_provider_arn> - name: ALIBABA_CLOUD_OIDC_TOKEN_FILE value: /var/run/secrets/ack.alibabacloud.com/rrsa-tokens/token image: registry.cn-hangzhou.aliyuncs.com/acs/ack-ram-tool:1.3.0 imagePullPolicy: Always name: demo volumeMounts: - mountPath: /var/run/secrets/ack.alibabacloud.com/rrsa-tokens name: rrsa-oidc-token readOnly: true restartPolicy: OnFailure serviceAccount: demo-sa serviceAccountName: demo-sa volumes: - name: rrsa-oidc-token projected: defaultMode: 420 sources: - serviceAccountToken: audience: sts.aliyuncs.com expirationSeconds: 3600 path: token
重要
请替换应用模板示例代码中的如下字段。
<oid_provider_arn>：替换为当前集群的OIDC提供商ARN。该ARN获取请参见[获取集群中](use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[OIDC](use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[提供商的](use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[URL](u
