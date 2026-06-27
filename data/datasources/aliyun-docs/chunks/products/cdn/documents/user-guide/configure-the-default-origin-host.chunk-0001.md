### 虚拟站点技术
虚拟站点技术是一种在单个 Web 服务器上提供多个网站服务的技术。服务器使用不同的域名或主机名区分和隔离不同的网站。当用户请求访问某个特定的域名或主机名时，服务器会根据请求中的域名或主机名，将请求定向到相应的虚拟站点，从而提供对应的网站内容。
Nginx 相关实现
Nginx 支持通过server区块配置多个虚拟站点，示例如下：
server { listen 80; server_name example.org www.example.org; ... } server { listen 80; server_name example.net www.example.net; ... } server { listen 80; server_name example.com www.example.com; ... }
上述配置了 3 个虚拟站点，分别为example.org、example.net、example.com。Nginx 使用server_name匹配 HTTP 请求头中的Host字段选择虚拟站点；如果未匹配到任何一个虚拟站点，Nginx 会使用默认的虚拟站点提供服务（若未配置，默认为第一个server配置的默认站点）。
