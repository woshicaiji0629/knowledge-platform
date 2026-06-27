## 步骤一：配置代理服务器
使用Nginx将一台具有公网访问权限的企业内网服务器配置为正向代理服务器。
登录待配置为正向代理服务器的机器。
下载Nginx及HTTPS补丁。
下载HTTPS补丁。
git clone https://github.com/chobits/ngx_http_proxy_connect_module.git
下载并解压Nginx。
其中，${version}表示Nginx版本，请根据实际情况替换。最新版本，请参见[nginx: download](https://nginx.org/en/download.html)。
wget http://nginx.org/download/nginx-${version}.tar.gz tar -xzvf nginx-${version}.tar.gz cd nginx-${version}/
添加HTTPS补丁到Nginx。
其中，${patchfile}为文件路径，请根据Nginx版本选择对应的文件。更多信息，请参见[Select patch](https://github.com/chobits/ngx_http_proxy_connect_module/#select-patch)。
patch -p1 < ../ngx_http_proxy_connect_module/patch/${patchfile}.patch
安装Nginx。
./configure --add-module=../ngx_http_proxy_connect_module make && make install
在nginx.conf文件中添加如下配置。
其中，${代理服务器监听端口}和${DNS服务器地址}，请根据实际情况替换。
server { listen ${代理服务器监听端口}; resolver ${DNS服务器地址}; # 用于指定非HTTP请求的代理。 proxy_connect; proxy_connect_allow 443; proxy_connect_connect_timeout 10s; proxy_connect_data_timeout 10s; # 用于指定HTTP请求的代理。 location / { proxy_pass http://$host; proxy_set_header Host $host; } }
启动Nginx服务器。
