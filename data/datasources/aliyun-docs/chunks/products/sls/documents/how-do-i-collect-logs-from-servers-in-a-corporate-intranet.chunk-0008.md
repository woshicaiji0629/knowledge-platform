## 步骤三：验证网络
登录某台企业内网服务器。
执行如下命令。
下述命令中的${region}为目标Project所在地域，${project_name}为目标Project名称，请根据实际情况替换。
curl http://logtail.${region}.log.aliyuncs.com curl https://logtail.${region}.log.aliyuncs.com curl http://${project_name}.${region}.log.aliyuncs.com curl http://ali-${region}-sls-admin.${region}.log.aliyuncs.com
如果系统返回如下类似信息，表示网络正常。
{"Error":{"Code":"OLSInvalidMethod","Message":"The script name is invalid : /","RequestId":"62591BC7C08B7BD4AA99FCD4"}}
重复执行步骤[1](how-do-i-collect-logs-from-servers-in-a-corporate-intranet.md)和[2](how-do-i-collect-logs-from-servers-in-a-corporate-intranet.md)，验证其他企业内网服务器的网络。
