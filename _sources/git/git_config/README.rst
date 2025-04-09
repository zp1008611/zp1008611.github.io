Git常用场景
===========

Ubuntu配置Git
-------------

在 Ubuntu 系统下使用 Git 可以按照以下步骤进行：安装 Git、配置
Git、基本操作、分支管理、远程仓库操作等，以下为你详细介绍：

安装 Git
~~~~~~~~

在 Ubuntu 中，你可以使用 ``apt`` 包管理器来安装
Git。打开终端，执行以下命令：

.. code:: bash

   sudo apt update
   sudo apt install git

安装完成后，你可以通过以下命令来验证 Git 是否安装成功：

.. code:: bash

   git --version

如果安装成功，会显示当前安装的 Git 版本号。

配置 Git
~~~~~~~~

安装完成后，你需要配置你的用户名和邮箱，这些信息会与你提交的代码关联起来。在终端中执行以下命令进行配置：

.. code:: bash

   git config --global user.name "Your Name"
   git config --global user.email "your_email@example.com"

你可以使用 ``git config --list`` 命令查看当前的配置信息。

本地配置SSH
~~~~~~~~~~~

大文件传输通过SSH稳定。

1. 生成SSH秘钥
   ``bash     ssh-keygen -t rsa -C "your_email@example.com"``
   提示的地方直接按\ ``Enter``

2. 查看生成秘钥 ``bash     cat  ~/.ssh/id_rsa.pub`` 或者
   ``bash     gedit ~/.ssh/id_rsa.pub``

gitee配置SSH公钥
~~~~~~~~~~~~~~~~

1. 登录git官网

2. 登陆后点击\ ``设置``\ ，选择\ ``SSH公钥``\ ，将\ ``id_rsa.pub``\ 中的内容复制到上面添加新的公钥.

将本地已存在的代码上传到 Gitee 仓库的 ``develop`` 分支
------------------------------------------------------

步骤 1：初始化本地仓库
~~~~~~~~~~~~~~~~~~~~~~

如果你还没有将本地代码初始化为 Git
仓库，需要在本地代码所在的目录下打开终端（Windows 可以使用 Git
Bash），执行以下命令来初始化仓库：

.. code:: bash

   git init

步骤 2：关联本地仓库和 Gitee 远程仓库
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

在 Gitee
上创建仓库后，会得到该仓库的远程地址。在终端中执行以下命令，将本地仓库与
Gitee 远程仓库关联起来：

.. code:: bash

   git remote add origin <Gitee 仓库的远程地址>

例如：

.. code:: bash

   git remote add origin https://gitee.com/your_username/your_repository.git

步骤 3：创建并切换到 ``develop`` 分支
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

在本地仓库中创建 ``develop`` 分支，并切换到该分支：

.. code:: bash

   git checkout -b develop

步骤 4：拉取gitee仓库中本来存在的代码
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

   git pull --no-rebase --allow-unrelated-histories origin develop

步骤 5：添加文件到暂存区
~~~~~~~~~~~~~~~~~~~~~~~~

将本地代码的所有文件添加到 Git 的暂存区，使用以下命令：

.. code:: bash

   git add .

这里的 ``.`` 表示当前目录下的所有文件。如果你只想添加特定的文件，可以将
``.`` 替换为具体的文件名。

步骤 3：提交暂存区的文件到本地仓库
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

执行以下命令将暂存区的文件提交到本地仓库，并添加一条提交信息：

.. code:: bash

   git commit -m "zp"

你可以将 ``"Initial commit"`` 替换为更具描述性的提交信息。

步骤7：推送本地 ``develop`` 分支到 Gitee 远程仓库
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

执行以下命令将本地 ``develop`` 分支的代码推送到 Gitee 远程仓库的
``develop`` 分支：

.. code:: bash

   git push -u origin develop

``-u`` 参数会将本地的 ``develop`` 分支和远程的 ``develop``
分支关联起来，以后再推送该分支时，就可以直接使用 ``git push`` 命令。

按照以上步骤操作，你就可以将本地已存在的代码上传到 Gitee 仓库的
``develop`` 分支上。
