# PCCS server address PCCS_URL=https://sgx-dcap-server.[Region-ID].aliyuncs.com/sgx/certification/v4/ # To accept insecure HTTPS cert, set this option to FALSE USE_SECURE_CERT=TRUE
如果vSGX实例只有VPC内网IP，/etc/sgx_default_qcnl.conf文件的内容修改如下。其中，[Region-ID]需替换为vSGX实例所在地域的ID。
