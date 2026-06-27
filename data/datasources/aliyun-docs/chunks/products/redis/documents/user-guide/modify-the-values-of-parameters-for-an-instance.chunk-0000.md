## 注意事项
若在设置实例参数时报错Parameter is not supported for current version，表示当前实例的小版本过低。您需要将实例升级至最新的小版本，具体操作请参见[升级小版本与代理版本](update-the-minor-version.md)。
云数据库 Tair（兼容 Redis）不支持直接调用命令设置参数，例如执行CONFIG SET TIMEOUT 60，返回OK是为了满足某些集成框架的需求，但实际不会生效，请您通过控制台或[ModifyInstanceConfig](../developer-reference/api-r-kvstore-2015-01-01-modifyinstanceconfig-redis.md)API接口设置参数。
