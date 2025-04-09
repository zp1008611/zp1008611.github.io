# Linux下COPT安装与配置

本文使用的系统为`Ubuntu 22.04.5 LTS (GNU/Linux 5.15.0-127-generic x86_64)`

## 1 官网申请

1. 进入官网https://www.shanshu.ai/copt申请试用版

## 2 安装

1. 将安装包移动到用户目录下，并解压

    ```bash
    cd ~/
    tar -zxvf CardinalOptimizer-7.2.4-lnx64.tar.gz
    ```

2. 查看是否存在 `.bashrc` 隐藏文件：

    ```bash
    ls -a
    ```
    若不存在该文件，则在终端上执行下述命令创建空的 `.bashrc` 文件：
    ```bash
    touch ~/.bashrc
    ```
    若已存在该文件，打开 `.bashrc` 文件
    ```bash
    vim .bashrc
    ```    
    按下`i`进入插入模式，并添加如下内容：
    ```bash
    export COPT_HOME=~/copt72
    export COPT_LICENSE_DIR=~/copt72
    export PATH=$COPT_HOME/bin:$PATH
    export LD_LIBRARY_PATH=$COPT_HOME/lib:$LD_LIBRARY_PATH
    ```
    按下`Esc`键回到命令模式，再执行`:wq`命令保存文件并退出.

3. 在终端输入下述命令使得上述环境变量修改生效.
    ```bash
    source ~/.bashrc
    ```

## 3 配置许可文件

1. 在系统的用户目录下新建文件夹`copt`，并移动已验证的授权文档 `license.dat` 和`license.key`至新建文件夹`copt`中.

2. 执行下述命令将授权文档`license.dat`和`license.key`移动到 `COPT_LICENSE_DIR`指向的路径下：
    ```bash
    cd ~/copt/
    mv license.* $COPT_LICENSE_DIR/
    ```
3. 输入`copt_cmd`，如果出现命令行工具，则说明安装配置成功

## 4 python调用copt

1. 安装python3.9

    1. 备份源文件：打开终端，执行cd /etc/apt/进入目录，再执行sudo cp sources.list sources.list.bak备份原文件。
    2. 编辑源文件：使用文本编辑器打开源文件，如sudo nano /etc/apt/sources.list或sudo gedit /etc/apt/sources.list或sudo vim /etc/apt/sources.list。
    3. 替换内容：访问清华大学开源软件镜像站 Ubuntu 页面，选择对应的 Ubuntu 版本，将页面中提供的镜像源内容复制，粘贴到打开的sources.list文件中，替换原有内容，然后保存文件。
    4. 更新源：在终端执行sudo apt-get update使新的源配置生效。
    5. 安装依赖包：执行sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev命令
    6. 下载 Python 3.9 的源代码：到官网https://www.python.org/downloads/release/python-390/下载Gzipped source tarball文件
    解压并进入目录：解压下载的源代码包tar -zxvf Python-3.9.0.tgz，然后进入解压后的目录cd Python-3.9.0。
    7. 配置并编译安装：执行./configure --enable-optimizations和
        ```bash
        make -j $(nproc)
        sudo make altinstall
        ```
    使用make altinstall可避免覆盖系统默认的 Python 版本。
    8. 验证：执行python3.9或python3.9 --version检查是否安装成功

2. 安装`coptpy`

    ```bash
    pip install coptpy
    ```
    或
    ```bash
    cd ~/copt72/lib/python
    python3 setup.py install
    ```

3. 新建python文件`lp_ex1.py`

    ```bash
    cd ~/copt/
    mkdir lp_ex1
    cd lp_ex1
    touch lp_ex1.py
    ```

    ```python
    #
    # This file is part of the Cardinal Optimizer, all rights reserved.
    #

    """
    The problem to solve:

    Maximize:
    1.2 x + 1.8 y + 2.1 z

    Subject to:
    1.5 x + 1.2 y + 1.8 z <= 2.6
    0.8 x + 0.6 y + 0.9 z >= 1.2

    where:
    0.1 <= x <= 0.6
    0.2 <= y <= 1.5
    0.3 <= z <= 2.8
    """

    import coptpy as cp
    from coptpy import COPT

    # Create COPT environment
    env = cp.Envr()

    # Create COPT model
    model = env.createModel("lp_ex1")

    # Add variables: x, y, z
    x = model.addVar(lb=0.1, ub=0.6, name="x")
    y = model.addVar(lb=0.2, ub=1.5, name="y")
    z = model.addVar(lb=0.3, ub=2.8, name="z")

    # Add constraints
    model.addConstr(1.5*x + 1.2*y + 1.8*z <= 2.6)
    model.addConstr(0.8*x + 0.6*y + 0.9*z >= 1.2)

    # Set objective function
    model.setObjective(1.2*x + 1.8*y + 2.1*z, sense=COPT.MAXIMIZE)

    # Set parameter
    model.setParam(COPT.Param.TimeLimit, 10.0)

    # Solve the model
    del.solve()

    # Analyze solution
    if model.status == COPT.OPTIMAL:
    print("Objective value: {}".format(model.objval))
    allvars = model.getVars()

    print("Variable solution:")
    for var in allvars:
    print(" x[{0}]: {1}".format(var.index, var.x))

    print("Variable basis status:")
    for var in allvars:
    print(" x[{0}]: {1}".format(var.index, var.basis))

    # Write model, solution and modified parameters to file
    model.write("lp_ex1.mps")
    model.write("lp_ex1.bas")
    model.write("lp_ex1.sol")
    model.write("lp_ex1.par")
    ```

4. 运行py文件

    ```bash
    python3 lp_ex1.py
    ```


## python下pyomo调用copt

