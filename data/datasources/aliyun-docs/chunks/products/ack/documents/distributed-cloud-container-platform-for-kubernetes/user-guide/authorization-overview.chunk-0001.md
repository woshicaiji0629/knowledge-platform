## 权限类型

| 权限类型 | 是否必须授权 | 权限说明 |
| --- | --- | --- |
| [服务角色](authorization-overview.md) | 首次使用 ACK One 服务时需要授权，使用阿里云账号（主账号）或者 [RAM](../../../../ram/documents/create-admin-user.md) [管理员账号](../../../../ram/documents/create-admin-user.md) （子账号）授权一次即可。 | 授权后，ACK One 服务才能访问其他关联云服务资源。 |
| [RAM](authorization-overview.md) [系统权限策略](authorization-overview.md) | RAM 用户或 RAM 角色必须授权，阿里云账号默认拥有权限，无需额外授权。 | 授权后，RAM 用户或 RAM 角色才能使用 ACK One 的功能。 |
| [RBAC](authorization-overview.md) [权限](authorization-overview.md) | RAM 用户或 RAM 角色必须授权，阿里云账号默认拥有权限，无需额外授权。 | 授权后，RAM 用户或 RAM 角色才能对 ACK One 集群内的 K8s 资源进行操作。 |
