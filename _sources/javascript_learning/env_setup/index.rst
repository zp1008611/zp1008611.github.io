JavaScript 运行环境搭建
=======================

Reference
---------

-  https://www.bilibili.com/video/BV15L4y1a7or/?vd_source=3d4b12fb4a4bfbc98942d43612ae2fb9

JavaScript是什么
----------------

JavaScript是一种高级编程语言，主要用于网页开发。它是一种解释型语言，通常用于为网页添加交互性和动态效果。JavaScript可以在浏览器中运行，也可以在服务器端（例如使用Node.js）。

JavaScript的运行环境搭建（Windows下）
-------------------------------------

1. 安装 Node.js 和 npm

   vtk.js supports the following development environments:

   -  Node 14+
   -  NPM 7+

   .. code:: bash

      curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
      sudo apt install -y nodejs
      sudo apt install npm

   您可以使用以下命令检查安装是否成功：

   .. code:: bash

      node -v
      npm -v

2. 创建项目目录

   创建一个新的项目目录并进入该目录：

   .. code:: bash

      cd /mnt/d/Users/16587/OneDrive/zp/postgraduate_code/MRI_code/
      mkdir vtkjs-project
      cd vtkjs-project

3. 初始化 npm 项目

   在项目目录中初始化一个新的 npm 项目：

   .. code:: bash

      npm init -y

4. 进入网址https://github.com/Kitware/vtk-js，下载 ``code zip``

5. 安装 vtk.js

   .. code:: bash

      npm install @kitware/vtk.js
      npm install -D webpack-cli webpack webpack-dev-server

6. 创建 HTML 文件

   .. code:: bash

      mkdir dist/ src/
      cd dist/
      touch index.html

   ``./dist/index.html``\ 内容如下：

   .. code:: bash

      <!doctype html>
      <html>
        <head>
          <meta charset="utf-8" />
        </head>
        <body>
          <script src="./main.js"></script>
        </body>
      </html>

7. 启动本地服务器

   为了访问 HTML 文件，您可以使用 ``http-server``
   启动一个简单的本地服务器。首先安装 ``http-server``\ ：

   .. code:: bash

      npm install -g http-server

   然后在项目目录中运行：

   .. code:: bash

      http-server

8. 访问项目

   打开浏览器，访问
   ``http://localhost:8080``\ （或其他显示的端口），您应该能够看到您的
   VTK.js 示例。

   通过以上步骤，您应该能够在 Ubuntu 上成功安装并使用 ``vtk.js``\ 。
