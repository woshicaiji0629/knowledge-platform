将自定义域名修改至RAM中OAuth应用的回调地址中。
使用RAM管理员登录[RAM](https://ram.console.aliyun.com/)[控制台](https://ram.console.aliyun.com/)。
在左侧导航栏，选择集成管理>OAuth应用（公测）。
在企业应用页签，单击目标应用ackone-argo-${cluster_id}@app.${uid}.onaliyun.com，其中，${cluster_id}为集群ID，${uid}为阿里云账号ID。
在基本信息区域，单击编辑基本信息，将回调地址修改为https://${domain}:2746/oauth2/callback，其中，${domain}为自定义的域名。
在浏览器中输入https://${domain}:2746，并使用云SSO账号登录，快速访问工作流集群控制台。
