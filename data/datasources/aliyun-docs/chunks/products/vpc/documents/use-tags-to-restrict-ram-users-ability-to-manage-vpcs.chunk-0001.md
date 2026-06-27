### 鉴权流程
标签鉴权的核心流程如下图所示：当RAM用户发起API请求时，RAM会根据主账号授予的权限策略中的Condition条件，同时检查请求中携带的标签（acs:RequestTag）和目标资源上已绑定的标签（acs:ResourceTag），只有所有条件均满足时，操作才会被允许。
