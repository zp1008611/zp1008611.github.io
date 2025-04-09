# win11使用sphinx编写文档并部署到github page
## Reference
- https://blog.hszofficial.site/recommend/2020/11/27/%E4%BD%BF%E7%94%A8Sphinx%E5%86%99%E9%A1%B9%E7%9B%AE%E6%96%87%E6%A1%A3/
- https://blog.csdn.net/hhy321/article/details/131150447?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522172336378516800175713307%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=172336378516800175713307&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v1~rank_v31_ecpm-1-131150447-null-null.142^v100^pc_search_result_base1&utm_term=readthedocs%20sphinx%20github&spm=1018.2226.3001.4187
- https://blog.csdn.net/gitblog_00003/article/details/136540329
- https://how-to-use-sphinx-write.readthedocs.io/zh-cn/latest/
- https://www.cnblogs.com/jonnyan/p/14207711.html
- `config.py`常用配置可参考：https://www.cnblogs.com/xy-bot/p/16889949.html

## 1 安装
1. 安装python3，这个自己找教程安装即可，记得配置环境变量
2. 打开cmd，输入

	```bash
	pip install sphinx
	```
3. 创建一个文件夹`zpdocs`，在文件夹内打开cmd，初始化一个`sphinx`

	```bash
	sphinx-quickstart
	```
	```bash
	> Separate source and build directories (y/n) [n]: y
	> Project name: zpdocs
	> Author name(s): zp
	> Project release []: 0.1
	> Project language [en]: zh_CN
	```
	执行完毕后，就可以看见创建的工程文件:

	```bash
	|- build 
	|- source
		|- _static 
		|- _templates 
		|- conf.py 
		|- index.rst
	|- Makefile 
	|- make.bat 
	```

	- build：文件夹，当你执行make html的时候，生成的html静态文件都存放在这里
	
	- source/_static：文件夹：图片,js等存放地址
	
	- source/_templates：文件夹:模板文件存放

	- source/index.rst：索引文件,文章目录大纲
	
	- source/conf.py：配置文件
	
	- make.bat：windows平台用于编译文档项目的makefile文件

	
	- Makefile：非windows平台用于编译文档项目的makefile文件
	



## 2 build项目

1. 在文件夹`zpdocs`内打开cmd，运行

	```bash
	./make html
	```
2. 打开`zpdocs/build/html/index.html`，编译成功
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/fec23c56b2c34021a68a55a97579f3b4.png)
3. 编译为http服务，这样可以通过ip地址查看网页
	1. 	安装`sphinx-autobuild`
		```bash
		pip install sphinx-autobuild
		```

	2. 在`zpdoc`中打开cmd重新编译
		```bash
		sphinx-autobuild source build/html
		```
		![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/eb0f2fb92c5b4c068ef9fe7f1e9ad561.png)
## 3 更改样式主题

1. 到[Sphnix官网](https://sphinx-themes.org/#themes)查看自己想要样式
2. 我使用`Book`主题，安装`sphinx-book-theme`
	```bash
	pip install sphinx-book-theme
	```
3. 修改`source/conf.py`文件中的`html_theme`字段

	```python
	html_theme = 'sphinx_book_theme'
	```
4. 在`source/conf.py`文件中的添加以下内容
	```bash
	source_suffix = {
	    '.rst': 'restructuredtext',
	    '.md': 'markdown'
	}
	
	html_title = "My amazing documentation"
	
	html_theme_options = {
	    "show_navbar_depth": 1,
	    "max_navbar_depth": 2,
	    "collapse_navbar": True,
	    "home_page_in_toc": True,
	    "use_download_button": False,
	}
	```
5. 重新编译
	```bash
	sphinx-autobuild source build/html
	```



## 4 支持markdown
1. Sphinx默认只支持reST格式的文件。
如果相要使用markdown格式的文档，还要安装markdown支持工具，命令如下：

	```bash
	pip install recommonmark
	pip install sphinx_markdown_tables
	```
2. 修改`source/conf.py`的`extensions`字段

	```bash
	extensions = ['recommonmark','sphinx_markdown_tables']
	```
3. 重新编译
	```bash
	sphinx-autobuild source build/html
	```
## 5 编辑网页内容
1. 修改source文件夹目录结构如下

	```bash
	|- build 
	|- source
		|- _static 
		|- _templates 
		|- chapter1
			|- section1
				|- README.md
			|- index.rst
		|- chapter2
			|- section1
				|- README.md
			|- index.rst
		|- conf.py 
		|- index.rst
	|- Makefile 
	|- make.bat 
	```
	-  `source/index.rst`
		```bash
		WELCOME!
		=============================
		.. toctree::  
		   :maxdepth: 2  
		   :caption: Contents  
		
		   Chapter1<chapter1/index>  
		   Chapter2<chapter2/index> 
		```
	
	- `source/chapter1/index.rst`
		```bash
		Chapter 1
		=============================

		.. toctree::  
		   :maxdepth: 2  
		   :caption: Chapter 1  Contents
		
		   S1.1<section1/README>  
		```

	- `source/chapter2/index.rst`
		```bash
		Chapter 2
		=============================

		.. toctree::  
		   :maxdepth: 2  
		   :caption: Chapter 2  Contents
		
		   S2.1<section1/README>  
		```
	- `source/chapter1/section1/README.md`
		```bash
		# S1.1
		```

	- `source/chapter2/section1/README.md`
		```bash
		# S2.1
		```

## 6 部署到github page
1. 在远程仓库创建一个仓库
2. 在`zpdocs`文件夹打开cmd，输入`./make clean`清除build缓存
3. 修改`conf.py`，添加
	```bash
	extensions = [...,'sphinx.ext.githubpages',...]
	```
	这个插件会为生成后的文档添加 .nojekyll 文件， 也会为 GitHub Pages 自定义域名添加 CNAME 文件。 如果没有 .nojekyll， GitHub Pages 会认为 _ 开头的文件夹是 jekyll 内部文件夹， 然后将它过滤掉。

	> 注意: Sphinx 文档的文件名不能使用大写字母。 因为 Sphinx 在 windows 上输出时会把的文件名转成小写, 而
	> GitHub Pages 的路由是大小写敏感的。 无法正确链接到使用了大写字母作为文件名的文件。

4. 重新编译
	```bash
	sphinx-autobuild source build/html
	```
5. 将`build/html`的文件推送到仓库的main分支，仓库中`setting`->`page`设置如下：
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/96d008a9254544aea08e765dafe0ebed.png)
## 7 注意事项