Win下配置WSL
============



wsl下ubuntu配置python3.8.10虚拟环境

-----------------------------------



1. 更新包仓库



   .. code:: bash



      sudo apt update && sudo apt upgrade



2. 安装依赖



   .. code:: bash



      sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget make gcc



3. 下载

   `python3.10.0源代码 <https://www.python.org/downloads/release/python-3100/>`__

   的 ``Gzipped source tarball``



4. 在压缩包所在目录打开终端



   .. code:: bash



      tar -zvxf Python-3.10.0.tgz



5. 测试系统并优化python



   .. code:: bash



      cd Python-3.10.0

      ./configure --enable-optimizations



6. 编译代码（这里等待的时间比较长）



   .. code:: bash



      mkdir build

      make -s



7. 安装python



   .. code:: bash



      sudo make altinstall



8. 测试



   .. code:: bash



      python3 -V



9. 配置虚拟环境



   .. code:: bash



      cd ~/workspace/uav_competition

      python3.8 -m ensurepip

      sudo apt-get install python3.8-venv

      sudo apt-get install python3.8-distutils



      python3.8 -m venv .venv

      source .venv/bin/activate



使用vscode开发

--------------



1. win下安装vscode，安装wsl插件



2. 权限修改



   .. code:: bash



      cd ~/workspace/uav_competition

      sudo chown -R zp for_py



   zp为你的用户名，for_py为你想要修改的文件夹权限的路径



3. 用vscode打开wsl的文件夹



   .. code:: bash



      cd ~/workspace/uav_competition/for_py

      code .



wsl配置代理

-----------



-  https://blog.csdn.net/iftodayhappy/article/details/137236279



1. 把之前在.bashrc启动文件中配置http_proxy和https_proxy的逻辑删去，并且关闭

   WSL



   .. code:: bash



      wsl --shutdown



2. 在我的window主机编辑~.wslconfig

   “去‘C::raw-latex:`\Users`:raw-latex:`\你的名字`’下面新建一个‘.wslconfig’，然后用记事本打开往里面放这些内容”



   如”C::raw-latex:`\Users`:raw-latex:`\fangy`\\.wslconfig”

   ``bash  [wsl2]  memory=8GB  processors=8  [experimental]  autoMemoryReclaim=gradual  networkingMode=mirrored  dnsTunneling=true  firewall=true  autoProxy=true  sparseVhd=true``



3. 重启 WSL 确实自动设置了代理，代理正常工作，

   很好，不必再手动设置http_proxy和https_proxy了。

