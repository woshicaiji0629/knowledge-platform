kms-service-credentials.md)[1](use-csi-secrets-store-provider-alibabacloud-to-import-alibaba-cloud-kms-service-credentials.md)已创建的RAM角色的ARN（需要Base64编码）。
{ak}：替换为RAM用户的AK（需要Base64编码）。
{sk}：替换为RAM用户的SK（需要Base64编码）。
apiVersion: v1 data: id: {ak} secret: {sk} rolearn: {rolearn} kind: Secret metadata: name: alibaba-credentials namespace: kube-system type: Opaque
执行以下命令，部署Secret。
kubectl apply -f alibaba-credentials.yaml
