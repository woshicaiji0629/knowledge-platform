## 自定义报表
示例1：查看最近30天内，响应状态码为499的域名排行榜。
日志分析语句：return_code = 499| select domain , count(*) as c group by domain order by c desc limit 10
示例2：查看最近30天内，响应状态码为502的域名排行榜。
日志分析语句：return_code = 502| select domain , count(*) as c group by domain order by c desc limit 10
示例3：查看最近30天内，访问URI为/cpu的日志数据。
可以直接单击左侧原始日志栏的URI字段，然后单击/cpu即可过滤出需要的日志。
过滤后，左侧快速分析面板的uri字段显示/cpu占比 53%，为最主要的请求 URI。查询栏过滤条件为* and uri : "/cpu"，时间范围选择30天（相对），日志总条数为 1,556,698。
该文章对您有帮助吗？
反馈
