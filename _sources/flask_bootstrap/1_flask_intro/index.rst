Flask 入门教程
==============

Reference
---------

-  `项目搭建参考 <https://flask.palletsprojects.com/en/3.0.x/tutorial/>`__
-  `测试参考 <https://testdriven.io/blog/flask-pytest/>`__

本文参考官网教程来做一个可以实现注册，登录，创建、修改、删除博客的博客网站，使用的宿主机为ubuntu22.04，源码可从\ `该网址 <https://github.com/pallets/flask/tree/2.3.3/examples/tutorial>`__\ 获得。

1 项目架构
----------

项目文件架构如下：

.. code:: bash

   /home/user/Projects/flask-tutorial
   ├── flaskr/
   │   ├── __init__.py
   │   ├── db.py
   │   ├── schema.sql
   │   ├── auth.py
   │   ├── blog.py
   |   ├── Dockerfile
   |   ├── .dockerignore
   |   ├── requirements.txt
   │   ├── templates/
   │   │   ├── base.html
   │   │   ├── auth/
   │   │   │   ├── login.html
   │   │   │   └── register.html
   │   │   └── blog/
   │   │       ├── create.html
   │   │       ├── index.html
   │   │       └── update.html
   │   └── static/
   │       └── style.css
   ├── tests/
   │   ├── conftest.py
   │   ├── data.sql
   │   ├── test_factory.py
   │   ├── test_db.py
   │   ├── test_auth.py
   │   └── test_blog.py
   └──  .venv/

这个项目结构是一个 Flask
应用程序的典型布局。下面是各个文件和文件夹的作用介绍：

1. ``flaskr/``

   这是 Flask 应用的主要包，包含应用的核心代码。

   -  **``__init__.py``**: 这个文件用于初始化 Flask 应用。通常在这里创建
      Flask 实例，并注册蓝图（Blueprints）、数据库等。

   -  **``db.py``**:
      该文件通常用于数据库的配置和操作，比如创建数据库连接、定义模型等。

   -  **``schema.sql``**:
      这个文件包含数据库的创建和初始化语句，通常用于设置数据库表结构。

   -  **``auth.py``**:
      处理与用户身份验证相关的路由和逻辑，比如登录、注册和登出功能。

   -  **``blog.py``**:
      处理与博客相关的路由和逻辑，比如创建、更新和显示博客文章。

   -  **``templates/``**: 存放 HTML 模板文件的目录，Flask
      会从这里加载模板。

   -  **``Dockerfile``, ``.dockerignore``,
      ``requirements.txt``**\ ：Docker部署项目时需要用到的文件

   -  **``base.html``**:
      基本模板，其他模板通常会继承这个模板，包含公共的 HTML
      结构（如头部、底部）。

      -  **``auth/``**: 存放与身份验证相关的模板。

         -  **``login.html``**: 用户登录页面的模板。

         -  **``register.html``**: 用户注册页面的模板。

      -  **``blog/``**: 存放与博客相关的模板。

         -  **``create.html``**: 创建新博客文章的页面模板。

         -  **``index.html``**: 显示所有博客文章的页面模板。

         -  **``update.html``**: 更新现有博客文章的页面模板。

   -  **``static/``**: 存放静态文件的目录，如 CSS、JavaScript 和图片等。

      -  **``style.css``**: 应用的样式表文件，用于定义网页的外观。

2. ``tests/`` 这个目录包含了项目的测试代码，确保应用的各个部分正常工作。

   -  **``conftest.py``**: 用于配置 pytest
      的测试设置，通常包括测试夹具（fixtures）。

   -  **``data.sql``**: 测试用的数据库初始化数据，可以在测试时加载。

   -  **``test_factory.py``**:
      测试应用工厂函数的文件，确保应用可以正确创建。

   -  **``test_db.py``**: 测试数据库相关功能的文件，确保数据库操作正常。

   -  **``test_auth.py``**:
      测试身份验证相关功能的文件，确保登录、注册等功能正常。

   -  **``test_blog.py``**:
      测试博客相关功能的文件，确保博客文章的创建、更新等功能正常。

3. ``.venv/`` 这是 Python
   虚拟环境的目录，包含项目所需的所有依赖包。虚拟环境可以隔离项目的依赖，避免与其他项目冲突。

2 虚拟环境配置
--------------

.. code:: bash

   mkdir flask-tutorial
   cd flask-tutorial
   sudo ln -fs /usr/local/bin/python3.11 /usr/bin/python3
   python3.11 -m venv .venv
   sudo ln -fs /usr/bin/python3.10 /usr/bin/python3
   source .venv/bin/activate

   # 如果使用代理运行，取消以下命令注释，并运行
   # unset all_proxy && unset ALL_PROXY # 取消所有 socks 代理
   # pip install pysocks

   pip install --upgrade pip
   pip install flask uwsgi

3 实列初始化
------------

1. 应用工厂模式介绍 Flask 应用程序是 Flask
   类的一个实例。与应用程序相关的所有内容，例如配置和
   URL，都将注册在这个类中。

   创建 Flask 应用程序的传统方式 最直接的创建 Flask
   应用程序的方法是在代码顶部直接创建一个全局的 Flask 实例，例如：
   
   .. code:: bash 

      from flask import Flask

      app = Flask(**name**)

      @app.route(“/”) 
      def hello_world(): 
         return "Hello, World!"

   虽然这种方法简单且在某些情况下有用，但随着项目的增长，可能会导致一些棘手的问题。

   在应用工厂模式中，您不再在全局范围内创建 Flask
   实例，而是将其放在一个函数内部。这个函数被称为”应用工厂”。所有的配置、注册和其他应用程序所需的设置都将在这个函数内部进行，最后返回应用程序实例。

   具体步骤:

   i. 创建应用工厂函数：定义一个函数来创建和配置 Flask 应用实例。
   ii. 配置应用：在函数内部加载配置，例如从文件或环境变量。
   iii. 注册蓝图和扩展：在应用上下文中注册蓝图和其他扩展。
   iv. 返回应用实例：函数最后返回配置好的应用实例。

2. 创建主代码文件夹和\ ``__init__.py``.

   ``__init__.py`` 文件的存在告诉 Python
   解释器该目录应被视为一个包。这使得您可以在该目录中组织模块，并通过导入语句访问它们。在
   Flask 应用程序中，\ ``__init__.py``
   通常用于定义应用工厂函数。这个函数负责创建和配置 Flask
   应用实例，并可以在不同的环境中创建多个实例。

   .. code:: bash

      mkdir flaskr
      cd flaskr
      touch __init__.py

   ``__init__.py``\ 内容如下：

   .. code:: bash

      import os

      from flask import Flask


      def create_app(test_config=None):
          # create and configure the app
          app = Flask(__name__, instance_relative_config=True)
          app.config.from_mapping(
              SECRET_KEY='dev',
              DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
          )

          if test_config is None:
              # load the instance config, if it exists, when not testing
              app.config.from_pyfile('config.py', silent=True)
          else:
              # load the test config if passed in
              app.config.from_mapping(test_config)

          # ensure the instance folder exists
          try:
              os.makedirs(app.instance_path)
          except OSError:
              pass

          # a simple page that says hello
          @app.route('/hello')
          def hello():
              return 'Hello, World!'

          return app

   ``create_app`` 是应用工厂函数，负责创建和配置 Flask
   实例。接下来，我们将详细介绍该函数的各个部分及其作用。

   i. 创建 Flask 实例

      .. code:: python

         app = Flask(__name__, instance_relative_config=True)

      -  ``__name__``\ ：当前 Python 模块的名称。Flask
         需要知道它的位置，以便设置一些路径。
      -  ``instance_relative_config=True``\ ：指示应用程序配置文件相对于实例文件夹。实例文件夹位于
         ``flaskr``
         包之外，可以存放不应提交到版本控制的本地数据，如配置秘密和数据库文件。

   ii. 设置默认配置

       .. code:: python

         app.config.from_mapping(
             SECRET_KEY='dev',
             DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
         )

       -  **``SECRET_KEY``**\ ：
          用于 Flask和扩展来保护数据。在开发阶段设置为``'dev'``\ ，但在部署时应用随机值。
       
       -  **``DATABASE``**\ ：
          SQLite 数据库文件的保存路径，位于``app.instance_path`` 下，
          这是 Flask 为实例文件夹选择的路径。

   iii. 从配置文件加载配置

        .. code:: python

         app.config.from_pyfile('config.py', silent=True)

        -  该方法会覆盖默认配置，使用实例文件夹中的 ``config.py``
           文件中的值（如果存在）。例如，在部署时，可以使用此方法设置真实的``SECRET_KEY``\ 。

   iv. 测试配置

       -  ``test_config``
          可以传递给工厂函数，并将用于替代实例配置。这使得您在后续编写的测试可以独立于任何开发值进行配置。

   v. 确保实例路径存在

      .. code:: python

         os.makedirs(app.instance_path, exist_ok=True)

      -  ``os.makedirs()`` 确保 ``app.instance_path`` 存在。Flask
         不会自动创建实例文件夹，但需要创建，因为您的项目将在此处创建
         SQLite 数据库文件。

   vi. 创建简单路由

       .. code:: python

         @app.route('/hello')
         def hello():
             return 'Hello, World!'

       -  ``@app.route()``
          创建一个简单的路由，使您可以在继续教程之前查看应用程序的工作情况。它将
          URL ``/hello`` 与返回字符串 ``'Hello, World!'``
          的函数连接起来。

4 定义并访问数据库
------------------

该应用程序将使用SQLite数据库来存储用户和帖子。Python内置了对SQLite的支持，通过sqlite3模块实现。

SQLite的便利之处在于它不需要单独设置数据库服务器，并且与Python紧密集成。然而，如果多个请求同时尝试写入数据库，写入操作将会顺序进行，从而导致性能下降。对于小型应用程序而言，这种影响可能不明显，但一旦应用规模扩大，可能需要考虑切换到其他数据库，如mysql.

1. 连接数据库

   在处理SQLite数据库（以及大多数其他Python数据库库）时，首先要做的就是创建一个与数据库的连接。所有的查询和操作都是通过这个连接来执行的，而在完成工作后会关闭该连接。

   在Web应用程序中，这个连接通常与请求相绑定。在处理请求的某个时刻创建连接，并在发送响应之前关闭连接。

   .. code:: bash

      cd flaskr
      touch db.py

   ``db.py``\ 内容如下：

   .. code:: bash

      import sqlite3

      import click
      from flask import current_app, g


      def get_db():
          if 'db' not in g:
              g.db = sqlite3.connect(
                  current_app.config['DATABASE'],
                  detect_types=sqlite3.PARSE_DECLTYPES
              )
              g.db.row_factory = sqlite3.Row

          return g.db


      def close_db(e=None):
          db = g.pop('db', None)

          if db is not None:
              db.close()

   这段代码是一个用Flask框架和SQLite3数据库进行数据库连接管理的示例。以下是对各部分代码的逐行解释：

   -  导入库

      .. code:: python

         import sqlite3      
         import click      
         from flask import current_app, g

      -  ``sqlite3``\ ：用于与SQLite数据库交互的模块。
      -  ``click``\ ：Flask用来处理命令行界面的模块。
      -  ``current_app``\ ：Flask的上下文对象，指向当前处理请求的应用程序。
      -  ``g``\ ：Flask提供的一个特殊对象，用于存储在一个请求中使用的临时数据。

   -  获取数据库连接的函数 

      .. code:: python

         def get_db(): if 'db' not in g:
            g.db = sqlite3.connect( current_app.config['DATABASE'],
                     detect_types=sqlite3.PARSE_DECLTYPES ) 
            g.db.row_factory = sqlite3.Row

            return g.db

      -  ``get_db()``\ ：这个函数用于获取数据库连接。
      -  ``if 'db' not in g:``\ ：检查\ ``g``\ 对象中是否已经存在数据库连接。如果不存在，则创建新的连接。
      -  ``sqlite3.connect(...)``\ ：使用\ ``DATABASE``\ 配置键所指向的文件名建立数据库连接。\ ``detect_types=sqlite3.PARSE_DECLTYPES``\ 允许SQLite自动将某些类型（如日期）解析为Python对象。
      -  ``g.db.row_factory = sqlite3.Row``\ ：设置行工厂，使返回的行可以像字典一样通过列名访问。
      -  ``return g.db``\ ：返回数据库连接，供其他函数使用。

   -  关闭数据库连接的函数 
      
      .. code:: python 

         def close_db(e=None): 
            db = g.pop('db', None)
            if db is not None:
               db.close()

      -  ``close_db(e=None)``\ ：这个函数用于关闭之前打开的数据库连接。
      -  ``db = g.pop('db', None)``\ ：从\ ``g``\ 中弹出\ ``db``\ ，如果没有连接则返回\ ``None``\ 。
      -  ``if db is not None:``\ ：检查是否有打开的数据库连接。
      -  ``db.close()``\ ：如果连接存在，则关闭该连接，以释放资源。

   -  ``get_db``\ 和\ ``close_db``\ 函数实现了数据库连接的获取和关闭。\ ``get_db``\ 在请求周期内维护一个连接，而\ ``close_db``\ 在请求结束时关闭连接，从而避免每次请求都创建新的连接，提高效率并减少资源占用。通常在Flask应用中，会在请求生命周期的适当位置（如\ ``after_request``\ ）调用\ ``close_db``\ ，以确保每次请求后连接被正确关闭。

2. 创建数据表

   在SQLite中，数据存储在表和列中。这些表和列需要在存储和检索数据之前创建。Flaskr将会把用户存储在用户表中，把帖子存储在帖子表中。创建一个包含创建空表所需的SQL命令的文件:

   .. code:: bash

      cd flaskr
      touch schema.sql

   ``schema.sql``\ 内容如下：

   .. code:: sql

      DROP TABLE IF EXISTS user;
      DROP TABLE IF EXISTS post;

      CREATE TABLE user (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          username TEXT UNIQUE NOT NULL,
          password TEXT NOT NULL
      );

      CREATE TABLE post (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          author_id INTEGER NOT NULL,
          created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
          title TEXT NOT NULL,
          body TEXT NOT NULL,
          FOREIGN KEY (author_id) REFERENCES user (id)
      );

   将运行SQL命令的Python函数添加到 ``db.py`` 文件中: 
   
   .. code:: python 
      
      # flaskr/db.py
      def init_db(): db = get_db()
         with current_app.open_resource('schema.sql') as f:
            db.executescript(f.read().decode('utf8'))

      @click.command('init-db') 
      def init_db_command(): 
      # Clear the existing data and create new tables.
      init_db()
      click.echo('Initialized the database.')
      

   -  ``open_resource()`` 功能： current_app.open_resource(‘schema.sql’)
      允许你以包相对路径打开文件。在部署应用时，文件的绝对路径可能无法预知，因此使用相对路径确保文件能够正确访问。这种方式特别符合
      Flask 应用的结构，使得资源管理更为高效和灵活。
   -  ``get_db()``
      功能：该函数返回数据库连接，允许你执行数据库操作，例如执行 SQL
      语句（如从 schema.sql
      中读取的命令）。这样，你可以在独立的函数中管理数据库连接的创建和访问，保持代码的模块化和清晰性。
   -  ``click.command()`` 功能：这是 Click
      库提供的装饰器，用于定义新的命令行指令。在这个例子中，它创建了一个名为
      init-db 的命令，当用户在命令行中输入 ``flask init-db``
      时，这个命令会被触发，调用 init_db_command()
      函数。执行函数后，会调用 init_db()
      来初始化数据库，然后显示成功消息。

3. 注册函数

   由于我们使用了应用工厂函数创建app时，所以应用工厂函数外的
   ``close_db`` 和 ``init_db_command``
   函数并不可用，因此需要编写一个函数来让app接受这些函数

   -  ``flaskr/db.py``

      .. code:: bash

         def init_app(app):
             app.teardown_appcontext(close_db)
             app.cli.add_command(init_db_command)

      这个函数的主要作用是将数据库相关的功能注册到 Flask 应用实例中

   -  ``flaskr/__init__.py``

      .. code:: bash

         def create_app():
             app = ...
             # existing code omitted

             from . import db
             db.init_app(app)

             return app

      在 Flask 的工厂函数中，我们需要调用 ``init_app(app)``
      来确保我们的数据库功能被正确注册

4. 初始化数据库文件

   ::

      cd flask-tutorial
      source .venv/bin/activate

      flask --app flaskr init-db

5 Templates（模板）
-------------------

1. Templates 介绍 在 Flask 中，templates 目录用于存放 HTML
   模板文件。Flask 利用 Jinja2 模板引擎来渲染这些模板。

   主要概念：

   -  模板：模板是包含静态和动态内容的 HTML 文件。通过
      Jinja2，你可以在模板中动态插入变量、控制结构（如循环、条件语句）等。

   -  渲染模板：Flask 提供了 render_template
      函数来渲染模板。当你调用这个函数时，Flask
      会将指定的模板文件加载并渲染成最终的 HTML 页面。

   -  模板语法：

      -  变量：使用 ``{{ variable_name }}`` 语法来插入变量。

      -  控制结构：使用 ``{%…%}`` ; 语法来实现逻辑，比如 ``for`` 循环和
         ``if`` 语句。例如：

         .. code:: html

            {% for item in items %}  
            <p>{{ item }}</p>  
            {% endfor %} 

         Flask 的 templates 目录和 Jinja2 模板引擎使得将动态内容与静态
         HTML 结合变得非常简单和高效。这对于构建现代 Web
         应用程序是一个非常重要的部分。

2. 基础布局模板

   在 Flask 中，你可以使用 Jinja2
   模板引擎的继承功能来创建一个基本的布局模板（称为基模板）。这个基模板包含应用的公共结构，比如头部、导航栏和底部，而每个具体的页面模板则可以继承这个基模板，并只需要定义特定的内容部分。通过模板继承，Flask
   使得重用 HTML
   结构变得简单而高效。你只需在基模板中定义一次公共结构，然后在各个页面模板中覆盖特定区域，这样可以减少重复代码，使维护变得更容易。

   .. code:: bash

      cd flask-tutorial/flaskr
      mkdir templates
      touch base.html

   ``base.html``\ 内容如下：

   .. code:: html

      <!doctype html>
      <title>{% block title %}{% endblock %} - Flaskr</title>
      <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
      <nav>
      <h1>Flaskr</h1>
      <ul>
          {% if g.user %}
          <li><span>{{ g.user['username'] }}</span>
          <li><a href="{{ url_for('auth.logout') }}">Log Out</a>
          {% else %}
          <li><a href="{{ url_for('auth.register') }}">Register</a>
          <li><a href="{{ url_for('auth.login') }}">Log In</a>
          {% endif %}
      </ul>
      </nav>
      <section class="content">
      <header>
          {% block header %}{% endblock %}
      </header>
      {% for message in get_flashed_messages() %}
          <div class="flash">{{ message }}</div>
      {% endfor %}
      {% block content %}{% endblock %}
      </section>

   在 Flask 的模板中，g
   是一个自动可用的对象，常用于存储与当前请求相关的数据。例如，通过
   load_logged_in_user 函数设置的 g.user
   可以用来判断用户是否已登录。如果 g.user
   被设置，模板会显示用户名和退出链接；如果未设置，则会显示注册和登录的链接。

   此外，url_for() 函数也是自动可用的，它用于生成指向视图的
   URL，而不是手动编写这些地址，这样能够提高代码的可读性和维护性。

   在页面标题之后，内容之前，模板会循环遍历 get_flashed_messages()
   返回的每条消息。你在视图中使用 flash()
   函数显示错误信息，这段代码则负责显示这些信息。

   模板中定义了三个块，它们可以在其他模板中被重写：

   {% block title %}：用于更改浏览器标签和窗口标题中显示的内容。 {%
   block header %}：类似于标题，但用于改变页面上显示的标题。 {% block
   content %}：用于包含每个页面的主要内容，例如登录表单或博客文章等。
   基模板直接放在 templates
   目录下，而针对每个蓝图（blueprint）的具体模板则会放在与蓝图同名的子目录中，以便保持组织性和清晰性。这样做可以让项目结构更清晰，便于管理和维护。

6 Static Files（静态文件）
--------------------------

1. Static Files介绍

   在Flask中，静态文件是指那些不需要经过服务器端处理的文件，例如图像、CSS文件、JavaScript文件等。Flask框架会自动为这些静态文件提供支持，使得开发者能够轻松地在Web应用中使用它们。

   -  静态文件的目录
      Flask默认将静态文件存放在名为static的文件夹中。项目目录结构通常像这样：
      
      .. code:: bash
         
         your_flask_app/        
         │        
         ├── app.py        
         └── static/            
         ├── css/            
         │   └── style.css            
         ├── js/            
         │   └── script.js            
         └── images/                
         └── logo.png

      在上面的示例中，static文件夹包含了CSS、JavaScript和图像文件。

   -  放置静态文件的方法
      在HTML模板中，你可以使用url_for函数来生成静态文件的URL，确保在更改文件位置或名称后，链接仍然有效。例如：
      
      .. code:: html

         <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/style.css') }}">        <img src="{{ url_for('static', filename='images/logo.png') }}" alt="Logo">``

   -  自定义静态文件路径
      你还可以通过自定义Flask应用的配置来更改静态文件的路径。例如：
      
      .. code:: python

         from flask import Flask        
         app = Flask(__name__, static_url_path='/assets', static_folder='my_static')

      在这个例子中，css静态文件可以通过/assets/css/style.css这样的路径访问。

   Flask中的静态文件为开发者提供了方便的方式来管理和访问不需要服务器处理的文件。通过使用默认的static目录，或者自定义配置，Flask能够有效地加载和提供这些文件。在开发Web应用时合理利用静态文件是非常重要的，可以改善用户体验和应用性能。

2. 添加静态文件

   这里简单设置一下css样式

   ::

      cd flask-tutorial/flaskr
      mkdir static
      touch style.css

   ``style.css``\ 内容如下：

   .. code:: css

      html {
      font-family: sans-serif;
      background: #eee;
      padding: 1rem;
      }

      body {
      max-width: 960px;
      margin: 0 auto;
      background: white;
      }

      h1, h2, h3, h4, h5, h6 {
      font-family: serif;
      color: #377ba8;
      margin: 1rem 0;
      }

      a {
      color: #377ba8;
      }

      hr {
      border: none;
      border-top: 1px solid lightgray;
      }

      nav {
      background: lightgray;
      display: flex;
      align-items: center;
      padding: 0 0.5rem;
      }

      nav h1 {
      flex: auto;
      margin: 0;
      }

      nav h1 a {
      text-decoration: none;
      padding: 0.25rem 0.5rem;
      }

      nav ul  {
      display: flex;
      list-style: none;
      margin: 0;
      padding: 0;
      }

      nav ul li a, nav ul li span, header .action {
      display: block;
      padding: 0.5rem;
      }

      .content {
      padding: 0 1rem 1rem;
      }

      .content > header {
      border-bottom: 1px solid lightgray;
      display: flex;
      align-items: flex-end;
      }

      .content > header h1 {
      flex: auto;
      margin: 1rem 0 0.25rem 0;
      }

      .flash {
      margin: 1em 0;
      padding: 1em;
      background: #cae6f6;
      border: 1px solid #377ba8;
      }

      .post > header {
      display: flex;
      align-items: flex-end;
      font-size: 0.85em;
      }

      .post > header > div:first-of-type {
      flex: auto;
      }

      .post > header h1 {
      font-size: 1.5em;
      margin-bottom: 0;
      }

      .post .about {
      color: slategray;
      font-style: italic;
      }

      .post .body {
      white-space: pre-line;
      }

      .content:last-child {
      margin-bottom: 0;
      }

      .content form {
      margin: 1em 0;
      display: flex;
      flex-direction: column;
      }

      .content label {
      font-weight: bold;
      margin-bottom: 0.5em;
      }

      .content input, .content textarea {
      margin-bottom: 1em;
      }

      .content textarea {
      min-height: 12em;
      resize: vertical;
      }

      input.danger {
      color: #cc2f2e;
      }

      input[type=submit] {
      align-self: start;
      min-width: 10em;
      }

7 Blueprints and Views（蓝图与视图）
------------------------------------

1. 蓝图和视图介绍

   Flask的蓝图（Blueprint）和视图（View）是构建Flask应用的重要概念。下面是对这两个概念的解释及示例代码。

   -  视图（View）

      视图是处理特定请求的函数。当Flask收到一个请求时，它会根据请求的URL匹配相应的视图函数，并返回视图函数的返回值作为响应。下列代码中的\ ``home``\ 和\ ``about``\ 都是视图函数

      .. code:: python

         from flask import Flask

         app = Flask(__name__)

         @app.route('/')
         def home():
             return "欢迎来到主页！"

         @app.route('/about')
         def about():
             return "这是关于页面。"

         if __name__ == '__main__':
             app.run(debug=True)

   -  蓝图（Blueprint）

      蓝图是Flask应用的一个模块化组件，允许你将应用分成多个部分，以便于管理和维护。每个蓝图可以定义自己的视图、静态文件和模板。

      .. code:: python

         from flask import Flask, Blueprint

         # 创建蓝图
         main = Blueprint('main', __name__)

         @main.route('/')
         def home():
             return "欢迎来到主页！"

         @main.route('/about')
         def about():
             return "这是关于页面。"

         # 创建Flask应用
         app = Flask(__name__)

         # 注册蓝图
         app.register_blueprint(main)

         if __name__ == '__main__':
             app.run(debug=True)

   -  总结

      -  视图：处理请求的函数，返回响应。
      -  蓝图：模块化应用的方式，允许将视图和其他功能分组，便于管理。

      通过使用蓝图，可以使大型应用更加结构化和可维护。

   下面我们将利用蓝图和视图构建身份验证和博客发布两大功能。

2. 身份验证蓝图

   身份验证蓝图将具有注册新用户、登录和注销三个视图。

   1. 创建并注册蓝图

      .. code:: bash

         cd flask-tutorial/flaskr
         touch auth.py

      ``auth.py``\ 内容如下：

      .. code:: python

         import functools

         from flask import (
             Blueprint, flash, g, redirect, render_template, request, session, url_for
         )
         from werkzeug.security import check_password_hash, generate_password_hash

         from flaskr.db import get_db

         bp = Blueprint('auth', __name__, url_prefix='/auth')

      这段代码创建了一个名为 ``auth``
      的蓝图。与应用对象类似，蓝图需要知道它是在哪里定义的，所以将
      ``__name__`` 作为第二个参数传入。\ ``url_prefix``
      会被添加到所有与该蓝图相关的URL前缀。

      要使用这个蓝图，需要从工厂函数中导入并注册它，使用
      ``app.register_blueprint()``\ 。将这段新代码放在工厂函数的末尾，在返回应用实例之前进行注册。修改\ ``flaskr/__init__.py``:

      .. code:: bash

         def create_app():
             app = ...
             # existing code omitted

             from . import auth
             app.register_blueprint(auth.bp)

             return app

   2. 用户注册视图

      ``flaskr/auth.py`` 添加内容：

      .. code:: bash

         @bp.route('/register', methods=('GET', 'POST'))
         def register():
             if request.method == 'POST':
                 username = request.form['username']
                 password = request.form['password']
                 db = get_db()
                 error = None

                 if not username:
                     error = 'Username is required.'
                 elif not password:
                     error = 'Password is required.'

                 if error is None:
                     try:
                         db.execute(
                             "INSERT INTO user (username, password) VALUES (?, ?)",
                             (username, generate_password_hash(password)),
                         )
                         db.commit()
                     except db.IntegrityError:
                         error = f"User {username} is already registered."
                     else:
                         return redirect(url_for("auth.login"))

                 flash(error)

             return render_template('auth/register.html')

      这段代码是一个用于处理用户注册的视图函数。当用户访问/auth/register
      URL时，如果是GET请求，会展示一个注册表单让用户填写；如果是POST请求，表示用户已经提交了注册表单，将对用户输入进行验证并处理注册逻辑。

      1. 当请求方法是POST时，获取用户提交的用户名和密码，并准备进行数据验证。
      2. 验证用户名和密码是否为空，如果为空，则设定相应的错误信息
      3. 如果输入验证通过，将用户提供的用户名和哈希过的密码插入到数据库中。
      4. 为了安全起见，密码不应该直接存储在数据库中，使用generate_password_hash()函数对密码进行加密处理，然后将哈希后的密码存储。
      5. 如果数据库中已存在相同用户名的用户，将捕获到IntegrityError，并显示相应的错误信息。
      6. 注册成功后，用户将被重定向到登录页面。redirect()函数生成一个重定向到登录视图的响应。
      7. 如果验证失败，错误信息将被显示给用户。flash()函数用于存储消息，以便在渲染模板时检索。
      8. 最后，如果用户是初次访问auth/register页面，或者存在验证错误，将展示一个包含注册表单的HTML页面。render_template()函数将渲染内容包含在HTML中，这部分内容将在本教程的下一步中编写。

      ``flaskr/templates/auth/register.html`` 内容如下：

      .. code:: html

         {% extends 'base.html' %}

         {% block header %}
         <h1>{% block title %}Register{% endblock %}</h1>
         {% endblock %}

         {% block content %}
         <form method="post">
             <label for="username">Username</label>
             <input name="username" id="username" required>
             <label for="password">Password</label>
             <input type="password" name="password" id="password" required>
             <input type="submit" value="Register">
         </form>
         {% endblock %}

   3. 用户登录视图

      ``flaskr/auth.py`` 添加内容：

      .. code:: bash

          @bp.route('/login', methods=('GET', 'POST'))
          def login():
              if request.method == 'POST':
                  username = request.form['username']
                  password = request.form['password']
                  db = get_db()
                  error = None
                  user = db.execute(
                      'SELECT * FROM user WHERE username = ?', (username,)
                  ).fetchone()

                  if user is None:
                      error = 'Incorrect username.'
                  elif not check_password_hash(user['password'], password):
                      error = 'Incorrect password.'

                  if error is None:
                      session.clear()
                      session['user_id'] = user['id']
                      return redirect(url_for('index'))

                  flash(error)

              return render_template('auth/login.html')

          @bp.before_app_request
          def load_logged_in_user():
              user_id = session.get('user_id')

              if user_id is None:
                  g.user = None
              else:
                  g.user = get_db().execute(
                      'SELECT * FROM user WHERE id = ?', (user_id,)
                  ).fetchone()

      这段代码是用于处理用户登录逻辑的视图函数。用户访问/auth/login
      URL时，如果是GET请求，将展示一个登录表单；如果是POST请求，表示用户已经提交了登录表单，将对用户的用户名和密码进行验证并处理登录逻辑。

      1. 当请求方法是POST时，获取用户提交的用户名和密码，并准备进行数据验证。
      2. 根据用户输入的用户名，从数据库中查询对应的用户数据。
      3. 如果查询结果为空，则设定错误信息提示”用户名不正确”；如果密码不匹配，则设定错误信息提示”密码不正确”。
      4. 如果验证通过，将用户的ID存储在会话中。会话是一个字典，用于在请求之间存储数据。Flask会将数据以cookie的形式发送到浏览器，并在后续的请求中将其发送回来。Flask会对数据进行安全签名，以确保数据不会被篡改。
      5. 登录成功后，用户将被重定向到主页。redirect()函数会生成一个重定向到主页视图的响应。
      6. 如果验证失败，错误信息将被显示给用户。flash()函数用于存储消息，以便在渲染模板时检索。

      除了处理登录请求的视图函数外，还有一个名为load_logged_in_user的函数注册到了\ ``bp.before_app_request``\ 中，它会在每次请求之前运行。这个函数用于检查会话中是否存储了用户ID，并将相应的用户数据从数据库中取出并存储在g.user中。g.user是一个特殊的对象，它的作用域仅限于当前请求。如果没有找到用户ID，或者ID不存在，g.user将被设置为None。

      这段代码结合了Flask的会话管理和视图处理，用于处理用户登录请求和会话管理。

      ``flaskr/templates/auth/login.html``\ 内容如下：

      .. code:: html

         {% extends 'base.html' %}

         {% block header %}
         <h1>{% block title %}Log In{% endblock %}</h1>
         {% endblock %}

         {% block content %}
         <form method="post">
             <label for="username">Username</label>
             <input name="username" id="username" required>
             <label for="password">Password</label>
             <input type="password" name="password" id="password" required>
             <input type="submit" value="Log In">
         </form>
         {% endblock %}

   4. 用户注销视图

      ``flaskr/auth.py`` 添加内容：

      .. code:: bash

         @bp.route('/logout')
         def logout():
             session.clear()
             return redirect(url_for('index'))

   5. 在其他视图中要求身份验证

      ``flaskr/auth.py`` 添加内容：

      .. code:: bash

         def login_required(view):
             @functools.wraps(view)
             def wrapped_view(**kwargs):
                 if g.user is None:
                     return redirect(url_for('auth.login'))

                 return view(**kwargs)

             return wrapped_view

      这段代码定义了一个装饰器函数login_required，该装饰器函数用于检查用户是否已经登录，如果用户尚未登录，则重定向到登录页面。

      装饰器函数接受一个视图函数作为参数，并返回一个新的视图函数，这个新的函数用于包装原始的视图函数。在包装的函数中，首先检查g.user是否为None（即用户是否已经登录），若用户未登录，则重定向到登录页面；如果用户已经登录，就调用原始的视图函数，并继续执行原始的视图逻辑。

      在使用该装饰器时，可以将其应用于需要用户登录才能进行操作的视图上，这样可以确保用户在执行相关操作之前已经完成了登录，提高了应用的安全性和稳定性。例如，在编写博客视图时，可以使用该装饰器来要求用户必须先登录才能创建、编辑或删除博客文章。

3. 博客发布蓝图

   博客发布蓝图包括帖子展示、发布帖子、编辑帖子和删除帖子四个视图

   1. 创建并注册蓝图

      .. code:: bash

         cd flask-tutorial/flaskr
         touch blog.py

      ``blog.py``\ 内容如下：

      .. code:: bash

         from flask import (
             Blueprint, flash, g, redirect, render_template, request, url_for
         )
         from werkzeug.exceptions import abort

         from flaskr.auth import login_required
         from flaskr.db import get_db

         bp = Blueprint('blog', __name__)

      注册蓝图，\ ``flaskr/__init__.py``\ 修改如下：

      .. code:: bash

         def create_app():
             app = ...
             # existing code omitted

             from . import blog
             app.register_blueprint(blog.bp)
             app.add_url_rule('/', endpoint='index')

             return app

      与身份验证蓝图不同，博客发布蓝图没有url_前缀。索引视图是/，创建视图是/create，等等。博客是flask的主要功能，所以博客索引将成为主要索引是有道理的。

   2. 博客展示视图

      ``flaskr/blog.py``\ 修改如下：

      .. code:: python

         @bp.route('/')
         def index():
             db = get_db()
             posts = db.execute(
                 'SELECT p.id, title, body, created, author_id, username'
                 ' FROM post p JOIN user u ON p.author_id = u.id'
                 ' ORDER BY created DESC'
             ).fetchall()
             return render_template('blog/index.html', posts=posts)

      ``flaskr/templates/blog/index.html``\ 内容如下：

      .. code:: html

         {% extends 'base.html' %}

         {% block header %}
         <h1>{% block title %}Posts{% endblock %}</h1>
         {% if g.user %}
             <a class="action" href="{{ url_for('blog.create') }}">New</a>
         {% endif %}
         {% endblock %}

         {% block content %}
         {% for post in posts %}
             <article class="post">
             <header>
                 <div>
                 <h1>{{ post['title'] }}</h1>
                 <div class="about">by {{ post['username'] }} on {{ post['created'].strftime('%Y-%m-%d') }}</div>
                 </div>
                 {% if g.user['id'] == post['author_id'] %}
                 <a class="action" href="{{ url_for('blog.update', id=post['id']) }}">Edit</a>
                 {% endif %}
             </header>
             <p class="body">{{ post['body'] }}</p>
             </article>
             {% if not loop.last %}
             <hr>
             {% endif %}
         {% endfor %}
         {% endblock %}

   3. 博客创建视图

      ``flaskr/blog.py``\ 修改如下：

      .. code:: python

         @bp.route('/create', methods=('GET', 'POST'))
         @login_required
         def create():
             if request.method == 'POST':
                 title = request.form['title']
                 body = request.form['body']
                 error = None

                 if not title:
                     error = 'Title is required.'

                 if error is not None:
                     flash(error)
                 else:
                     db = get_db()
                     db.execute(
                         'INSERT INTO post (title, body, author_id)'
                         ' VALUES (?, ?, ?)',
                         (title, body, g.user['id'])
                     )
                     db.commit()
                     return redirect(url_for('blog.index'))

             return render_template('blog/create.html')

      ``flaskr/templates/blog/create.html``\ 内容如下：

      .. code:: html

         {% extends 'base.html' %}

         {% block header %}
         <h1>{% block title %}New Post{% endblock %}</h1>
         {% endblock %}

         {% block content %}
         <form method="post">
             <label for="title">Title</label>
             <input name="title" id="title" value="{{ request.form['title'] }}" required>
             <label for="body">Body</label>
             <textarea name="body" id="body">{{ request.form['body'] }}</textarea>
             <input type="submit" value="Save">
         </form>
         {% endblock %}

   4. 博客编辑视图

      ``flaskr/blog.py``\ 修改如下：

      .. code:: python

         def get_post(id, check_author=True):
             post = get_db().execute(
                 'SELECT p.id, title, body, created, author_id, username'
                 ' FROM post p JOIN user u ON p.author_id = u.id'
                 ' WHERE p.id = ?',
                 (id,)
             ).fetchone()

             if post is None:
                 abort(404, f"Post id {id} doesn't exist.")

             if check_author and post['author_id'] != g.user['id']:
                 abort(403)

             return post

         @bp.route('/<int:id>/update', methods=('GET', 'POST'))
         @login_required
         def update(id):
             post = get_post(id)

             if request.method == 'POST':
                 title = request.form['title']
                 body = request.form['body']
                 error = None

                 if not title:
                     error = 'Title is required.'

                 if error is not None:
                     flash(error)
                 else:
                     db = get_db()
                     db.execute(
                         'UPDATE post SET title = ?, body = ?'
                         ' WHERE id = ?',
                         (title, body, id)
                     )
                     db.commit()
                     return redirect(url_for('blog.index'))

             return render_template('blog/update.html', post=post)

      ``flaskr/templates/blog/update.html``\ 内容如下：

      .. code:: bash

         {% extends 'base.html' %}

         {% block header %}
         <h1>{% block title %}Edit "{{ post['title'] }}"{% endblock %}</h1>
         {% endblock %}

         {% block content %}
         <form method="post">
             <label for="title">Title</label>
             <input name="title" id="title"
             value="{{ request.form['title'] or post['title'] }}" required>
             <label for="body">Body</label>
             <textarea name="body" id="body">{{ request.form['body'] or post['body'] }}</textarea>
             <input type="submit" value="Save">
         </form>
         <hr>
         <form action="{{ url_for('blog.delete', id=post['id']) }}" method="post">
             <input class="danger" type="submit" value="Delete" onclick="return confirm('Are you sure?');">
         </form>
         {% endblock %}

   5. 博客删除视图

      ``flaskr/blog.py``\ 修改如下：

      .. code:: python

         @bp.route('/<int:id>/delete', methods=('POST',))
         @login_required
         def delete(id):
             get_post(id)
             db = get_db()
             db.execute('DELETE FROM post WHERE id = ?', (id,))
             db.commit()
             return redirect(url_for('blog.index'))

8 重点解读\ ``auth.py``
-----------------------

.. code:: python

   import functools

   from flask import Blueprint
   from flask import flash
   from flask import g
   from flask import redirect
   from flask import render_template
   from flask import request
   from flask import session
   from flask import url_for
   from werkzeug.security import check_password_hash
   from werkzeug.security import generate_password_hash

   from flaskr.db import get_db

   bp = Blueprint("auth", __name__, url_prefix="/auth")


   def login_required(view):
       """View decorator that redirects anonymous users to the login page."""

       @functools.wraps(view)
       def wrapped_view(**kwargs):
           if g.user is None:
               return redirect(url_for("auth.login"))

           return view(**kwargs)

       return wrapped_view


   @bp.before_app_request
   def load_logged_in_user():
       """If a user id is stored in the session, load the user object from
       the database into ``g.user``."""
       user_id = session.get("user_id")

       if user_id is None:
           g.user = None
       else:
           g.user = (
               get_db().execute("SELECT * FROM user WHERE id = ?", (user_id,)).fetchone()
           )


   @bp.route("/register", methods=("GET", "POST"))
   def register():
       """Register a new user.

       Validates that the username is not already taken. Hashes the
       password for security.
       """
       if request.method == "POST":
           username = request.form["username"]
           password = request.form["password"]
           db = get_db()
           error = None

           if not username:
               error = "Username is required."
           elif not password:
               error = "Password is required."

           if error is None:
               try:
                   db.execute(
                       "INSERT INTO user (username, password) VALUES (?, ?)",
                       (username, generate_password_hash(password)),
                   )
                   db.commit()
               except db.IntegrityError:
                   # The username was already taken, which caused the
                   # commit to fail. Show a validation error.
                   error = f"User {username} is already registered."
               else:
                   # Success, go to the login page.
                   return redirect(url_for("auth.login"))

           flash(error)

       return render_template("auth/register.html")


   @bp.route("/login", methods=("GET", "POST"))
   def login():
       """Log in a registered user by adding the user id to the session."""
       if request.method == "POST":
           username = request.form["username"]
           password = request.form["password"]
           db = get_db()
           error = None
           user = db.execute(
               "SELECT * FROM user WHERE username = ?", (username,)
           ).fetchone()

           if user is None:
               error = "Incorrect username."
           elif not check_password_hash(user["password"], password):
               error = "Incorrect password."

           if error is None:
               # store the user id in a new session and return to the index
               session.clear()
               session["user_id"] = user["id"]
               return redirect(url_for("index"))

           flash(error)

       return render_template("auth/login.html")


   @bp.route("/logout")
   def logout():
       """Clear the current session, including the stored user id."""
       session.clear()
       return redirect(url_for("index"))

1. ``load_logged_in_user`` 和 ``login_required`` 两个函数在 Flask
   身份验证系统中是互相配合的，确保用户的登录状态得到有效管理。以下是它们如何互相影响的详细解释：

   1. ``load_logged_in_user`` 函数

      -  **目的**\ ：在每个请求之前检查用户是否已登录，并将用户信息加载到
         ``g.user`` 中。
      -  **工作流程**\ ：

         1. 每次请求到达时，\ ``load_logged_in_user`` 会被调用。
         2. 它从会话中获取用户 ID (``session.get("user_id")``)。
         3. 如果用户 ID 存在，则从数据库中查询用户信息，并将其存储在
            ``g.user`` 中；如果不存在，则将 ``g.user`` 设置为
            ``None``\ 。

   2. ``login_required`` 装饰器

      -  **目的**\ ：保护特定视图，确保只有已登录用户才能访问。
      -  **工作流程**\ ：

         1. 当被装饰的视图函数被调用时，\ ``login_required``
            装饰器会首先检查 ``g.user`` 的值。
         2. 如果 ``g.user`` 为
            ``None``\ （表示用户未登录），则重定向到登录页面。
         3. 如果 ``g.user`` 不为
            ``None``\ ，则表示用户已登录，视图函数继续执行。

   3. 互相影响的方式

      1. **用户状态的检查**\ ：

         -  ``load_logged_in_user`` 在每个请求之前设置 ``g.user`` 的值。
         -  ``login_required`` 装饰器依赖于 ``g.user``
            的值来判断用户是否已登录。

      2. **请求的处理**\ ：

         -  当用户请求一个受保护的视图时，首先执行
            ``load_logged_in_user``\ ，确保 ``g.user`` 已被正确设置。
         -  接着，\ ``login_required`` 装饰器会检查 ``g.user``
            的值，以决定是否允许访问该视图。

      3. **重定向与访问控制**\ ：

         -  如果用户未登录（\ ``g.user`` 为
            ``None``\ ），\ ``load_logged_in_user``
            会将其状态设置为未登录，而 ``login_required``
            会捕捉到这一点并重定向用户到登录页面。

   4. 总结

      -  **协作关系**\ ：\ ``load_logged_in_user``
         函数负责在每个请求中更新用户的登录状态，而 ``login_required``
         装饰器则根据这个状态来决定是否允许访问特定的视图。这种协作关系确保了用户在访问应用时的安全性和一致性。
      -  **用户体验**\ ：通过这种设计，用户在未登录时尝试访问受保护的页面时，会被自动重定向到登录页面，从而提供了良好的用户体验。

2. 用户注册流程（register）

   1. **请求处理**\ ：

      -  用户访问 ``/auth/register`` 路由，发送一个 GET 请求。
      -  Flask 调用 ``register`` 视图函数，返回注册页面的模板。

   2. **表单提交**\ ：

      -  用户填写用户名和密码并提交表单，发送一个 POST 请求。
      -  Flask 再次调用 ``register`` 视图函数。

   3. **数据验证**\ ：

      -  检查用户名和密码是否为空。
      -  如果有错误，使用 ``flash``
         函数显示错误信息，并重新渲染注册页面。

   4. **数据库操作**\ ：

      -  如果没有错误，尝试将用户信息（用户名和加密后的密码）插入到数据库中。
      -  如果用户名已存在，捕获 ``IntegrityError``
         异常，显示相应的错误信息。

   5. **成功注册**\ ：

      -  如果插入成功，重定向到登录页面 (``/auth/login``)。

3. 用户登录流程（login）

   1. **请求处理**\ ：

      -  用户访问 ``/auth/login`` 路由，发送一个 GET 请求。
      -  Flask 调用 ``login`` 视图函数，返回登录页面的模板。

   2. **表单提交**\ ：

      -  用户输入用户名和密码并提交表单，发送一个 POST 请求。
      -  Flask 再次调用 ``login`` 视图函数。

   3. **数据验证**\ ：

      -  从数据库中查询用户信息，检查用户名是否存在。
      -  如果用户名不存在，返回错误信息。
      -  如果用户名存在，再检查密码是否正确。

   4. **成功登录**\ ：

      -  如果用户名和密码都正确，清空当前会话，并将用户 ID
         存储到会话中。
      -  重定向到首页 (``/index``)。

4. 用户注销流程

   1. **请求处理**\ ：

      -  用户访问 ``/auth/logout`` 路由，发送一个 GET 请求。
      -  Flask 调用 ``logout`` 视图函数。

   2. **清空会话**\ ：

      -  调用 ``session.clear()`` 清空当前会话，包括存储的用户 ID。

   3. **重定向**\ ：

      -  重定向到首页 (``/index``)。

5. 总结

   -  注册：用户填写信息，验证后将其存入数据库。
   -  登录：用户输入凭证，验证后将其 ID 存入会话。
   -  注销：清空会话信息，用户退出。
   -  用户状态管理：load_logged_in_user
      函数在每个请求中检查用户的登录状态，并将用户信息存储在 g
      对象中，方便后续使用。
   -  安全性：login_required
      装饰器保护敏感视图，确保只有已登录用户才能访问。

9 重点解读\ ``blog.py``
-----------------------

.. code:: python

   from flask import Blueprint
   from flask import flash
   from flask import g
   from flask import redirect
   from flask import render_template
   from flask import request
   from flask import url_for
   from werkzeug.exceptions import abort

   from flaskr.auth import login_required
   from flaskr.db import get_db

   bp = Blueprint("blog", __name__)


   @bp.route("/")
   def index():
       """Show all the posts, most recent first."""
       db = get_db()
       posts = db.execute(
           "SELECT p.id, title, body, created, author_id, username"
           " FROM post p JOIN user u ON p.author_id = u.id"
           " ORDER BY created DESC"
       ).fetchall()
       return render_template("blog/index.html", posts=posts)


   def get_post(id, check_author=True):
       """Get a post and its author by id.

       Checks that the id exists and optionally that the current user is
       the author.

       :param id: id of post to get
       :param check_author: require the current user to be the author
       :return: the post with author information
       :raise 404: if a post with the given id doesn't exist
       :raise 403: if the current user isn't the author
       """
       post = (
           get_db()
           .execute(
               "SELECT p.id, title, body, created, author_id, username"
               " FROM post p JOIN user u ON p.author_id = u.id"
               " WHERE p.id = ?",
               (id,),
           )
           .fetchone()
       )

       if post is None:
           abort(404, f"Post id {id} doesn't exist.")

       if check_author and post["author_id"] != g.user["id"]:
           abort(403)

       return post


   @bp.route("/create", methods=("GET", "POST"))
   @login_required
   def create():
       """Create a new post for the current user."""
       if request.method == "POST":
           title = request.form["title"]
           body = request.form["body"]
           error = None

           if not title:
               error = "Title is required."

           if error is not None:
               flash(error)
           else:
               db = get_db()
               db.execute(
                   "INSERT INTO post (title, body, author_id) VALUES (?, ?, ?)",
                   (title, body, g.user["id"]),
               )
               db.commit()
               return redirect(url_for("blog.index"))

       return render_template("blog/create.html")


   @bp.route("/<int:id>/update", methods=("GET", "POST"))
   @login_required
   def update(id):
       """Update a post if the current user is the author."""
       post = get_post(id)

       if request.method == "POST":
           title = request.form["title"]
           body = request.form["body"]
           error = None

           if not title:
               error = "Title is required."

           if error is not None:
               flash(error)
           else:
               db = get_db()
               db.execute(
                   "UPDATE post SET title = ?, body = ? WHERE id = ?", (title, body, id)
               )
               db.commit()
               return redirect(url_for("blog.index"))

       return render_template("blog/update.html", post=post)


   @bp.route("/<int:id>/delete", methods=("POST",))
   @login_required
   def delete(id):
       """Delete a post.

       Ensures that the post exists and that the logged in user is the
       author of the post.
       """
       get_post(id)
       db = get_db()
       db.execute("DELETE FROM post WHERE id = ?", (id,))
       db.commit()
       return redirect(url_for("blog.index"))

1. 博客展示 (``index`` 函数)

   流程：

   1. **路由匹配**\ ：当用户访问 ``/`` 路径时，Flask 会调用 ``index``
      函数。

   2. **数据库查询**\ ：

      -  使用 ``get_db()`` 获取数据库连接。
      -  执行 SQL 查询，获取

         -  id：文章的唯一标识符（主键）。
         -  title：文章的标题。
         -  body：文章的内容（正文）。
         -  created：文章的创建时间（通常是一个时间戳）。
         -  author_id：作者的唯一标识符（指向用户表中的用户 ID）。
         -  username：作者的用户名（从用户表中获取。

   3. **渲染模板**\ ：

      -  将SQL查询结果（即所有文章）传递给 ``render_template``
         函数，渲染 ``blog/index.html`` 模板。

   4. **返回响应**\ ：将渲染后的 HTML 页面返回给用户。

2. 博客创建 (``create`` 函数)

   流程：

   1. **路由匹配**\ ：当用户访问 ``/create`` 路径时，Flask 会调用
      ``create`` 函数。
   2. **登录检查**\ ：由于使用了 ``@login_required``
      装饰器，首先会检查用户是否已登录。如果未登录，则会重定向到登录页面。
   3. **处理 POST 请求**\ ：

      -  如果请求方法为 ``POST``\ ，则获取表单中的 ``title`` 和
         ``body``\ 。
      -  检查标题是否为空：
      -  如果为空，使用 ``flash`` 函数存储错误消息。
      -  如果不为空，执行插入操作。

   4. **数据库插入**\ ：

      -  使用 ``get_db()`` 获取数据库连接，并执行插入 SQL
         语句，将新博客文章添加到数据库中。
      -  提交更改。

   5. **重定向**\ ：插入成功后，重定向到博客文章列表页（\ ``blog.index``\ ）。
   6. **渲染模板**\ ：如果请求方法为 ``GET``\ ，则渲染
      ``blog/create.html`` 模板，显示创建文章的表单。

3. 博客编辑 (``update`` 函数)

   流程：

   1. **路由匹配**\ ：当用户访问 ``/\<int:id>/update`` 路径时，Flask
      会调用 ``update`` 函数，\ ``id`` 是要编辑的文章的 ID。
   2. **登录检查**\ ：同样，由于使用了 ``@login_required``
      装饰器，首先会检查用户是否已登录。
   3. **获取文章**\ ：

      -  调用 ``get_post(id)`` 函数，获取指定 ID
         的文章。如果文章不存在或用户不是作者，则会抛出 ``404`` 或
         ``403`` 错误。

   4. **处理 POST 请求**\ ：

      -  如果请求方法为 ``POST``\ ，获取表单中的 ``title`` 和
         ``body``\ 。
      -  检查标题是否为空：
      -  如果为空，使用 ``flash`` 存储错误消息。
      -  如果不为空，执行更新操作。

   5. **数据库更新**\ ：

      -  使用 ``get_db()`` 获取数据库连接，并执行更新 SQL
         语句，更新指定文章的标题和内容。
      -  提交更改。

   6. **重定向**\ ：更新成功后，重定向到博客文章列表页（\ ``blog.index``\ ）。
   7. **渲染模板**\ ：如果请求方法为 ``GET``\ ，则渲染
      ``blog/update.html`` 模板，并传递要编辑的文章信息。

4. 博客删除 (``delete`` 函数)

   流程：

   1. **路由匹配**\ ：当用户访问 ``/\<int:id>/delete`` 路径时，Flask
      会调用 ``delete`` 函数。
   2. **登录检查**\ ：同样，由于使用了 ``@login_required``
      装饰器，首先会检查用户是否已登录。
   3. **获取文章**\ ：

      -  调用 ``get_post(id)``
         函数，确保要删除的文章存在，并且用户是作者。如果不满足条件，则抛出相应的错误。

   4. **数据库删除**\ ：

      -  使用 ``get_db()`` 获取数据库连接，并执行删除 SQL 语句，删除指定
         ID 的文章。
      -  提交更改。

   5. **重定向**\ ：删除成功后，重定向到博客文章列表页（\ ``blog.index``\ ）。

5. 总结

   -  **展示**\ ：用户访问 ``/``\ ，获取并显示所有文章。
   -  **创建**\ ：用户访问 ``/create``\ ，提交表单创建新文章。
   -  **编辑**\ ：用户访问 ``/\<int:id>/update``\ ，修改指定文章。
   -  **删除**\ ：用户访问 ``/\<int:id>/delete``\ ，删除指定文章。

9 测试
------



10 docker部署
-------------
