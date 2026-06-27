### 示例七：匹配多条规则时，执行break规则。
在回源URL重写配置中添加两条重写规则：第一条待重写Path为^/image_01.png$，目标Path为/image_02.png，执行规则为break，状态为已生效；第二条待重写Path为^(.*)$，目标Path为/image$1，执行规则为空，状态为已生效。当请求URI匹配到第一条规则且执行规则为break时，将不再继续匹配后续规则。
结果说明：
原始请求：http://example.com/image_01.png
重写后的回源请求：http://example.com/image_02.png
说明
先匹配第一条规则，重写为http://example.com/image_02.png，由于第一条规则设置为break，所以不再匹配后续规则。
该文章对您有帮助吗？
反馈
