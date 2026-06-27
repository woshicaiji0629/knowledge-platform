1 kind: Ingress metadata: name: tomcat-https spec: tls: - hosts: - foo.bar.com secretName: secret-https rules: - host: foo.bar.com http: paths: - path: / pathType: Prefix backend: service: name: tomcat-svc port: number: 8080
返回路由列表，查看创建的路由（Ingress），本例中域名为foo.bar.com，并查看端点和域名，您也可进入路由详情页进行查看。
说明
本例中以foo.bar.com作为测试域名，您需要在hosts文件中创建一条记录。
47.110.119.203 foo.bar.com #其中IP地址即是路由的端点。
在路由（Ingress）列表中，可以看到已创建的tomcat-https路由条目，其端点列显示的 IP 地址即为路由端点。
在浏览器中访问https://foo.bar.com。
说明
由于创建了TLS证书访问，所以要用HTTPS来进行域名访问，针对该应用，本例以foo.bar.com为示例，在本地进行解析。在具体使用场景中，请使用备案过的域名。
在浏览器中访问https://foo.bar.com，页面成功显示 Apache Tomcat/8.5.34 默认欢迎页面，表明 Tomcat 服务已正常部署且通过 Ingress 路由可达。
该文章对您有帮助吗？
反馈
