# Access Key Id $ export ALICLOUD_ACCESS_KEY="<你的 Access Key ID>" # Access Key Secret $ export ALICLOUD_SECRET_KEY="<你的 Access Key Secret>" # 如果是 STS 的访问凭证，此处需要配置 security_token $ export ALICLOUD_SECURITY_TOKEN="<你的访问 Token>"
设置了环境变量之后，provider块可以不在配置模板中显式声明或者只声明地域信息：
provider "alicloud" { region = "cn-hangzhou" }
当然，region也是支持通过环境变量ALICLOUD_REGION进行配置的。如果 region 没有显式声明也没有配置环境变量，cn-beijing将是其默认配置值。
