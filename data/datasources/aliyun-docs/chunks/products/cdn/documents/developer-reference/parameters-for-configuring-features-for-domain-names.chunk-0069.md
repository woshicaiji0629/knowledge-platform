配置示例：
鉴权方式A
{ "Functions": [{ "functionArgs": [{ "argName": "auth_type", "argValue": "type_a" }, { "argName": "auth_key1", "argValue": "1234567890123456789" }, { "argName": "auth_key2", "argValue": "1234567890123456789" }, { "argName": "ali_auth_delta", "argValue": 1800 }, { "argName": "req_auth_ip_white", "argValue": "192.168.0.1" }, { "argName": "req_auth_ip_acl_xfwd", "argValue": "all" }], "functionName": "aliauth" }], "domainNames": "example.com" }
鉴权方式F
{ "Functions": [{ "functionArgs": [{ "argName": "auth_type", "argValue": "type_f" },{ "argName": "auth_key1", "argValue": "1234567890123456789" },{ "argName": "auth_key2", "argValue": "1234567890123456789" },{ "argName": "ali_auth_delta", "argValue": 1800 },{ "argName": "sign_param", "argValue": "sign" },{ "argName": "time_param", "argValue": "time", },{ "argName": "time_format", "argValue": "hec" },{ "argName": "path_encoding", "argValue": "on" }], "functionName": "aliauth" }], "domainNames": "example.com" }
cdn_remote_auth
功能说明：配置远程鉴权，该功能详细介绍请参见控制台配置说明[配置远程鉴权](../user-guide/configure-remote-authentication.md)。
功能ID（FunctionID/FuncId）：258。
参数说明：
