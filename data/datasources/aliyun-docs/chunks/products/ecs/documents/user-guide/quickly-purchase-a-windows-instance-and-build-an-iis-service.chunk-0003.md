### 步骤三：部署 IIS 服务并验证访问
在实例上安装 IIS 服务，部署一个测试页面，从公网验证访问。
在开始菜单中搜索并打开Windows Powershell。
安装IIS服务。
Install-WindowsFeature -name Web-Server -IncludeAllSubFeature -IncludeManagementTools
待安装进度到达100%，返回Success为True表示安装成功。
创建测试页面。将自定义内容写入IIS默认站点目录。
Set-Content -Path "C:\inetpub\wwwroot\index.html" -Value "<html><body><h1>Hello from Alibaba Cloud ECS</h1></body></html>"
在本地电脑的浏览器中访问http://<ECS公网IP地址>/index.html。
<ECS公网IP地址>可在实例列表的IP地址列获取。
页面显示"Hello from Alibaba Cloud ECS"，表示Web部署成功。
