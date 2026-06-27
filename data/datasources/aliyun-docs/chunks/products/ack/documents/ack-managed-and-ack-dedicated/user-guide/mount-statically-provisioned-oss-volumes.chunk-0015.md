配置为 rrsa ，使用 RRSA 方式鉴权。 |
| roleName | 配置为此前创建或修改的 RAM 角色。 如需为不同 PV 配置不同权限，可创建不同的 RAM 角色，并在 PV 中配置不同的 roleName 。 |
| sigVersion | 请求 OSS 服务端的请求签名版本。 "v1" （默认）：使用 OSS [签名版本](../../../../oss/documents/developer-reference/ddd-signatures-to-urls.md) [1](../../../../oss/documents/developer-reference/ddd-signatures-to-urls.md) 。 "v4" ：使用 OSS [签名版本](../../../../oss/documents/developer-reference/add-signatures-to-urls.md) [4（推荐）](../../../../oss/documents/developer-reference/add-signatures-to-urls.md) 。 |
