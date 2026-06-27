cs:ram::113511544585****:oidc-provider/TestOidcProvider roleArn=acs:ram::113511544585****:role/testoidc # 自定义角色会话名称，用于区分不同的令牌。 roleSessionName= TestOidcAssumedRoleSession region=cn-hangzhou
通过如下命令查询examplebucket中的对象。
ossutil ls oss://examplebucket -c ~/.ossutilconfig
