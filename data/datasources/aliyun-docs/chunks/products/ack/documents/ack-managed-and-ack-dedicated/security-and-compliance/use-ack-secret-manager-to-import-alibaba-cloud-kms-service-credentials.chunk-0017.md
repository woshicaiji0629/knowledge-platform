.md)。
{ "Statement": [ { "Action": "sts:AssumeRole", "Effect": "Allow", "Resource": "acs:ram:*:<ACCOUNT_ID>:role/<ROLE_NAME>" } ], "Version": "1" }
上述自定义策略中的Resource为角色ARN，其中，<ACCOUNT_ID>为阿里云账号ID，<ROLE_NAME>为RAM角色名称。关于如何查看角色ARN，请参见[如何查看](../../../../ram/documents/support/faq-about-ram-roles-and-sts-tokens.md)[RAM](../../../../ram/documents/support/faq-about-ram-roles-and-sts-tokens.md)[角色的](../../../../ram/documents/support/faq-about-ram-roles-and-sts-tokens.md)[ARN？](../../../../ram/documents/support/faq-about-ram-roles-and-sts-tokens.md)。
将上述自定义策略授权给RAM用户，便可以指定具体可以扮演的RAM角色。关于如何为RAM用户授权，请参见[为](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户授权](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)。
创建Secret用于存放指定RAM用户的访问凭证信息。
使用以下内容，替换您的AccessKey ID和AccessKey Secret的Base64编码信息后，创建ramuser.yaml文件。
apiVersion: v1 data: accessKey: <AccessKey ID的Base64编码> accessKeySecret: <AccessKey Secret的Base64编码> kind: Secret metadata: name: ramuser namespace: kube-system type: Opaque
执行以下命令，创建名为ramuser的Secret。
kubectl apply -f ramuser.yaml
创建自定义资源SecretStore关联对应的认证方式并部署。
