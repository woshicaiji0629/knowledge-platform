无法处理请求时仍旧有请求发送，继而导致业务异常的风险。 | 修改 Pod spec，增加 readinessProbe 字段。 示例： |
| livenessProbeMissing | 配置容器存活探针 | 通过检查 Workload 的 Pod spec 中是否未配置 livenessProbe ，检查是否未配置检测容器内应用是否出现异常需要重启容器的探针。如果未配置，存在容器内应用异常需要重启容器才能恢复时未及时重启导致业务异常的风险。 | 修改 Pod spec，增加 livenessProbe 字段。 示例： |
| tagNotSpecified | 容器使用明确的镜像版本 | 通过检查 Workload 的 Pod spec 中的 image 字段的值是否未包含镜像 Tag 或者使用了 latest 作为镜像 Tag，检查是否未配置运行容器时使用指定 Tag 的容器镜像。如果未配置，存在运行容器时运行了非预期的容器镜像版本导致业务异常的风险。 | 修改 Pod spec，修改 image 字段，使用指定的镜像 Tag，并且不要使用 latest 作为镜像 Tag。 示例： |
| anonymousUserRBACBinding | 禁止匿名用户访问集群 | 通过检查集群内的 RBAC（Role-based access control）绑定找出配置了匿名用户访问权限的配置项。如果配置了允许匿名用户访问集群资源的配置项，则存在被恶意匿名用户窃取集群敏感信息、攻击和入侵集群的风险。 | 修改扫描出来的 RBAC 绑定，根据实际情况删除允许匿名用户访问集群资源的权限配置项。 示例： |
