# Win下配置WSL


## wsl下ubuntu配置python3.8.10虚拟环境

地图数据处理使用

1. 更新包仓库

    ```bash
    sudo apt update && sudo apt upgrade
    ```

2. 安装依赖

    ```bash
    sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget make gcc
    ```
	
3. 下载 [python3.10.0源代码](https://www.python.org/downloads/release/python-3100/) 的 `Gzipped source tarball` 

4. 在压缩包所在目录打开终端

    ```bash
    tar -zvxf Python-3.10.0.tgz
    ```

5. 测试系统并优化python

    ```bash
    cd Python-3.10.0
    ./configure --enable-optimizations
    ```

6. 编译代码（这里等待的时间比较长）

    ```bash
    mkdir build
    make -s
    ```

7. 安装python

    ```bash
    sudo make altinstall
    ```

8. 测试

    ```bash
    python3 -V
    ```

9. 配置虚拟环境

    ```bash
    cd ~/workspace/uav_competition
    python3.8 -m ensurepip
    sudo apt-get install python3.8-venv
    sudo apt-get install python3.8-distutils

    python3.8 -m venv .venv
    source .venv/bin/activate
    ```

## 使用vscode开发

1. win下安装vscode，安装wsl插件

2. 权限修改

    ```bash
    cd ~/workspace/uav_competition
    sudo chown -R zp for_py
    ```

    zp为你的用户名，for_py为你想要修改的文件夹权限的路径

3. 用vscode打开wsl的文件夹

    ```bash
    cd ~/workspace/uav_competition/for_py
    code .
    ```