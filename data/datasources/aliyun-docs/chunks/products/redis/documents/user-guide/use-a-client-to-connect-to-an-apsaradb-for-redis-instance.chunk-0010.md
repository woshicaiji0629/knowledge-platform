### redis-py
下载并安装[redis-py](https://github.com/andymccurdy/redis-py)客户端。
在Python编辑器中输入下述代码，然后根据注释提示修改代码。
本示例的Python版本为3.9、redis-py版本为4.4.1。
#!/usr/bin/env python #-*- coding: utf-8 -*- import redis # 分别将host和port的值替换为实例的连接地址、端口号。 host = 'r-bp10noxlhcoim2****.redis.rds.aliyuncs.com' port = 6379 # 将pwd的值替换为实例的密码。 # 默认账号password可直接填写密码；新建账号password填写格式 账号:密码，例如新建账号testaccount，密码Rp829dlwa，password填写testaccount:Rp829dlwa。 pwd = 'testaccount:Rp829dlwa' r = redis.Redis(host=host, port=port, password=pwd) # 连接建立后即可执行数据库操作，下述代码为您提供SET与GET的使用示例。 r.set('foo', 'bar') print(r.get('foo'))
执行上述代码。
