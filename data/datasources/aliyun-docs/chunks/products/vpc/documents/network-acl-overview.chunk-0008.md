| 端口 | 服务 | 说明 |
| --- | --- | --- |
| 21 | FTP | FTP 服务所开放的端口，用于上传、下载文件。 |
| 22 | SSH | SSH 端口，用于通过命令行模式或远程连接软件（例如 PuTTY、Xshell、SecureCRT 等）连接 Linux 实例。 |
| 23 | Telnet | Telnet 端口，用于 Telnet 远程登录 ECS 实例。 |
| 25 | SMTP | SMTP 服务所开放的端口，用于发送邮件。 |
| 53 | DNS | 用于域名解析服务器（Domain Name Server，简称 DNS）协议。 |
| 80 | HTTP | 用于 HTTP 服务提供访问功能，例如，IIS、Apache、Nginx 等服务。 |
| 110 | POP3 | 用于 POP3 协议，POP3 是电子邮件接收的协议。 |
| 143 | IMAP | 用于 IMAP（Internet Message Access Protocol）协议，IMAP 是用于接收电子邮件的协议。 |
| 443 | HTTPS | 用于 HTTPS 服务提供访问功能。HTTPS 是一种能提供加密和通过安全端口传输的协议。 |
| 1433 | SQL Server | SQL Server 的 TCP 端口，用于供 SQL Server 对外提供服务。 |
| 1434 | SQL Server | SQL Server 的 UDP 端口，用于获取 SQL Server 使用的 TCP/IP 端口号和 IP 地址等信息。 |
| 1521 | Oracle | Oracle 通信端口，ECS 实例上部署了 Oracle SQL 需要放行的端口。 |
| 3306 | MySQL | MySQL 数据库对外提供服务的端口。 |
| 3389 | Windows Server Remote Desktop Services | Windows Server Remote Desktop Services（远程桌面服务）端口，可以通过这个端口使用软件连接 Windows 实例。 |
| 8080 | 代理端口 | 与 80 端口类似，8080 端口通常用于提供 WWW 代理服务，用于实现网页浏览。如果您使用了 8080 端口，当访问网站或使用代理服务器时，需要在 IP 地址后面加上冒号和 8080（例如： IP 地址:8080 ）。在安装 Apache Tomcat 服务后，默认的服务端口为 8080。 |
| 137、138、139 | NetBIOS 协议 | NetBIOS 协议常被用于 Windows 文件、打印机共享和 Samba。 UDP 端口 137 和 138 通常用于网上邻居传输文件时的通信。
