## 步骤三：配置数据同步信息
认证信息配置完成后，需要通过自定义资源ExternalSecret来配置待访问的KMS凭据信息，从而将KMS凭据导入到Kubernetes Secret。
说明
KMS凭据导入的Kubernetes Secret的命名空间、名称均与ExternalSecret的命名空间、名称一致。
创建自定义资源ExternalSecret并部署。
使用以下内容，替换相关字段后，创建external.yaml文件。
