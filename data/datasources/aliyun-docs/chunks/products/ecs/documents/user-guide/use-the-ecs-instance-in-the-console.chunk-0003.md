### 步骤三：搭建WordPress
部署 LNMP 环境。
执行以下脚本一键部署 Wordpress 所需的 LNMP 环境（Linux + Nginx + MySQL + PHP）。执行前将MYSQL_PASSWORD替换为自定义的MySQL root密码 ，后续搭建 Wordpress 数据库时需要使用。
密码长度须为8至30个字符，且必须同时包含大小写英文字母、数字和特殊符号，其中特殊符号包含()` ~!@#$%^&*-+=|{}[]:;‘<>,.?/。curl -fsSL https://help-static-aliyun-doc.aliyuncs.com/install-script/deploy-lnmp-acl3_2.sh | MYSQL_ROOT_PASS='MYSQL_PASSWORD' bash脚本仅适用于Alibaba Cloud Linux 3.2104 LTS 64位。
登录 MySQL，创建 WordPress 专用数据库和用户。
MYSQL_PASSWORD：填写为[上一步](use-the-ecs-instance-in-the-console.md)设置的MySQL密码。
WORDPRESS_PASSWORD：自定义WordPress的用户密码。
密码长度须为8至30个字符，且必须同时包含大小写英文字母、数字和特殊符号，其中特殊符号包含()` ~!@#$%^&*-+=|{}[]:;‘<>,.?/。
mysql -u root -p'MYSQL_PASSWORD' <<EOF CREATE DATABASE wordpress; CREATE USER 'wordpress_user'@'localhost' IDENTIFIED BY 'WORDPRESS_PASSWORD'; GRANT ALL PRIVILEGES ON wordpress.* TO 'wordpress_user'@'localhost'; FLUSH PRIVILEGES; EOF
指令将创建一个名为wordpress的数据库和一个具有该数据库全部权限的wordpress_user用户。
下载并解压 WordPress。
cd /usr/share/nginx/html && sudo wget https://cn.wordpress.org/wordpress-6.4.4-zh_CN.zip && sudo yum install unzip -y && sudo unzip wordpress-6.4.4-zh_CN.zip
配置数据库连接。
备份默认配置。
sudo cp /usr/share/nginx/html/wordpress/wp-config-sample.php /usr/share/nginx/html/wordpres
