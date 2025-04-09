# SCIP安装与配置

在 Linux 系统上安装 SCIP（Solving Constraint Integer Programs）求解器，可按照以下步骤进行操作。这里以 Ubuntu 系统为例，其他 Linux 发行版的步骤类似，仅包管理命令有所不同。

## 1. 安装必要的依赖
SCIP 的编译和运行依赖一些工具和库，需要先进行安装。打开终端，执行以下命令：
```bash
sudo apt update
sudo apt install build-essential g++ python3-dev libgmp-dev libbz2-dev libz-dev libboost-all-dev coinor-libipopt-dev
```
- `build-essential`：包含了编译 C 和 C++ 程序所需的基本工具，如 `gcc`、`g++`、`make` 等。
- `python3-dev`：如果需要使用 Python 接口与 SCIP 交互，此包提供了 Python 开发所需的头文件和库。
- `libgmp-dev`：GNU 多精度算术库的开发包，SCIP 在某些计算中会用到。
- `libbz2-dev` 和 `libz-dev`：分别是 bzip2 和 zlib 压缩库的开发包，用于处理压缩文件。

## 2. 下载 SCIP 求解器
可以从 SCIP 的官方网站（https://scipopt.org/）下载最新版本的 SCIP 求解器。通常下载的是源代码压缩包，也可以使用 `wget` 命令直接从终端下载，例如下载 SCIPOptSuite 8.0.3 版本：
```bash
wget https://scipopt.org/download/release/scipoptsuite-8.0.3.tgz
```

## 3. 解压源代码
使用 `tar` 命令解压下载的压缩包：
```bash
tar -xf scipoptsuite-8.0.3.tgz
```
解压后会生成一个名为 `scipoptsuite-8.0.3` 的目录，进入该目录：
```bash
cd scipoptsuite-8.0.3
```

## 4. 配置和编译
```bash
mkdir build                                                       # create a new directory
cd build                                                          # change directories
cmake .. -DCMAKE_INSTALL_PREFIX=/home/zhongpei/jzlog/scipoptsuite-8.0.3/ -DAUTOBUILD=ON
make                                                               # start compiling SCIP
make check                                               # (recommended) check build
sudo make install               # (optional) install SCIP executable, library, and headers
```

## 6. 验证安装
安装完成后，可以通过运行以下命令来验证 SCIP 是否安装成功：
```bash
scip
```
如果成功启动 SCIP 求解器，显示 SCIP 的欢迎信息和命令行提示符，则说明安装成功。

## 7. 设置环境变量
为了方便使用 SCIP 的 Python 接口，建议设置 `SCIPOPTDIR` 环境变量。打开终端，执行以下命令：
```bash
export SCIPOPTDIR=/home/zhongpei/jzlog/scipoptsuite-8.0.3/
```
将 `/path/to/scipoptsuite-8.0.3` 替换为你实际解压 SCIPOptSuite 的目录路径。为了让这个环境变量在每次启动终端时都生效，可以将上述命令添加到 `~/.bashrc` 或 `~/.bash_profile` 文件中：
```bash
echo 'export SCIPOPTDIR=/home/zhongpei/jzlog/scipoptsuite-8.0.3/' >> ~/.bashrc
source ~/.bashrc
```

通过以上步骤，你就可以在 Linux 系统上成功安装 SCIP 求解器。 