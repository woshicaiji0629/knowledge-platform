sion.md)。
重定向：当源站需要重定向用户到另一个URL时，回源响应头可以设置正确的重定向响应头。关于重定向具体请参见[配置回源](configure-301-or-302-redirection.md)[301/302](configure-301-or-302-redirection.md)[跟随](configure-301-or-302-redirection.md)。
示例：Location: https://www.example.com/new-page.html：通知CDN及用户浏览器新的资源位置，用于301或302重定向。
自定义回源行为：在某些情况下，源站可能需要提供一些自定义的头部信息给客户端，以实现特定的功能或跟踪目的，您可以通过配置回源响应头来添加这些自定义头部。
