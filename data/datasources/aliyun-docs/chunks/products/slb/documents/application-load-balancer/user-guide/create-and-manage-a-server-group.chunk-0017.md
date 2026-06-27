## 控制台
在创建或编辑服务器组时，开启会话保持，选择Cookie处理方式：
Cookie处理方式：
植入Cookie：ALB自动生成Cookie（SERVERID）并植入响应，后续携带该Cookie的请求将转发至同一后端服务器。会话保持超时时间取值范围1~86400秒。
重写Cookie：ALB重写用户自定义的Cookie值。需输入Cookie名称。
