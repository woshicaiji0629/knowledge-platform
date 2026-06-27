## 资源组授权的工作原理
您可以使用资源组（Resource Group）对阿里云账号内的资源进行分组管理。例如，为不同的项目创建对应的资源组，并将资源转移到对应的组中，以便集中管理各项目的资源。更多信息，请参见[什么是资源组](https://help.aliyun.com/zh/resource-management/resource-group/product-overview/resource-group-overview)。
在完成资源分组后，您可以为不同的RAM授权主体（RAM用户、RAM用户组或RAM角色）授予指定资源组范围的权限，从而限定这个授权主体只能管理该资源组内的资源。更多信息，请参见[资源分组和授权](https://help.aliyun.com/zh/resource-management/resource-group/use-cases/use-ram-to-create-and-authorize-resource-groups#DAS)。
这种授权方式的优点有：
权限精细化：确保每个身份能获得最准确的资源访问权限，避免账号下的多个项目的资源混合管理。
良好的扩展性：后续新增资源时，只需将其加入该资源组，RAM身份便会自动获得新资源的相应权限，无需再次授权。
