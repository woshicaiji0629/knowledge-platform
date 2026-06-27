ll unzip -y && sudo unzip wordpress-6.4.4-zh_CN.zip
配置数据库连接。
备份默认配置。
sudo cp /usr/share/nginx/html/wordpress/wp-config-sample.php /usr/share/nginx/html/wordpress/wp-config.php
编辑wp-config.php，将WORDPRESS_PASSWORD替换为设置的[WordPress 用户密码](use-the-ecs-instance-in-the-console.md)。
sudo sed -i "s/database_name_here/wordpress/" /usr/share/nginx/html/wordpress/wp-config.php && \sudo sed -i "s/username_here/wordpress_user/" /usr/share/nginx/html/wordpress/wp-config.php && \sudo sed -i "s/password_here/WORDPRESS_PASSWORD/" /usr/share/nginx/html/wordpress/wp-config.php
更新 Nginx 站点根目录并重启。
sudo sed -i 's|root /usr/share/nginx/html;|root /usr/share/nginx/html/wordpress;|' /etc/nginx/conf.d/default.conf && sudo nginx -t && sudo systemctl restart nginx
