## API
[创建](developer-reference/api-sls-2020-12-30-createproject.md)[Project](developer-reference/api-sls-2020-12-30-createproject.md)。
创建 Project 时提示ProjectAlreadyExist，但控制台列表不可见
原因：Project 名称在阿里云地域内全局唯一。若当前账号下看不到该 Project，极可能是被其他阿里云账号占用。
处理建议：由于阿里云资源隔离机制，无法查看或删除其他账号名下的 Project。建议更换一个未被占用的 Project 名称，重新尝试创建。
