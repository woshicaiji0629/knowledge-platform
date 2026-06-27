## 功能优势
安全便捷：无需在ECS上的代码或配置文件中保存AccessKey，通过实例元数据服务（Instance Metadata Service, IMDS）即可自动获取STS临时凭证调用API，从而降低AccessKey泄露的风险。
无缝切换：如需更换应用程序的RAM身份，只需在控制台调整授予ECS的RAM角色，无需修改代码或重启服务。
权限精细化：可以为不同的ECS实例分配不同的RAM角色，实现最小权限原则。
