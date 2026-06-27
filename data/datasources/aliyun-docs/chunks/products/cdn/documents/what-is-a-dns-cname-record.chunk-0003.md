### 快速实现服务器IP的更新
当服务器的IP地址发生了变化（从10.10.10.10变为10.10.10.1），只需要把A记录对应的记录值修改成新的IP（10.10.10.1），与A记录的域名存在映射关系的三个CNAME记录无需任何改动，就能实现三个域名最终指向新的服务器IP的效果。
示例（示例数据仅供理解，不具有真实性）：
服务器IP修改前：
记录类型 域名 记录值 CNAME cname1.example.com www.example.com CNAME cname2.example.com www.example.com CNAME cname3.example.com www.example.com A www.example.com 10.10.10.10
服务器IP修改后：
记录类型 域名 记录值 CNAME cname1.example.com www.example.com CNAME cname2.example.com www.example.com CNAME cname3.example.com www.example.com A www.example.com 10.10.10.1
