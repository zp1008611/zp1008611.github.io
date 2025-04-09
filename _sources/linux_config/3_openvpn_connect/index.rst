OpenVPN客户端连接OpenVPN服务器
==============================



Reference

---------



-  https://luanlengli.github.io/2019/11/25/OpenVPN%E5%AE%A2%E6%88%B7%E7%AB%AF-Windows-Linux-MacOS-%E8%BF%9E%E6%8E%A5OpenVPN%E6%9C%8D%E5%8A%A1%E5%99%A8.html

-  https://openvpn.net/connect-docs/installation-guide-windows.html



windows

-------



1. 进入https://openvpn.net/client/下载下载文件



Linux

-----



1. 安装软件（或者进⼊上述⽹站⼿动下载安装）： sudo apt install openvpn

2. 上传客⼾端配置 client.ovpn ⽂件⾄ /etc/openvpn ⽬录

3. 启动服务： sudo openvpn client.ovpn ，后台任务⽅式启动： sudo openvpn

   – daemon —config client.ovpn

