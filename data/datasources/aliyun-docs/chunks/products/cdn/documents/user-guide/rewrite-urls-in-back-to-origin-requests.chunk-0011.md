### 示例六：匹配多条规则时，执行空规则。
在回源URL重写配置中添加两条规则：第一条将待重写Path^/image_01.png$重写为目标Path/image_02.png，执行规则为空；第二条将待重写Path^(.*)$重写为目标Path/image$1，执行规则为空。两条规则状态均为已生效。
结果说明：
原始请求：http://example.com/image_01.png
重写后的回源请求：http://example.com/image/image_02.png
说明
先匹配第一条规则，重写为http://example.com/image_02.png，继续匹配第二条规则，最终重写为http://example.com/image/image_02.png。
