# hello-world
This my usually tools edit with python.
get address from ip use python3.8


pdf_sqplite usage:
requirement:           PyPDF2

pip -y install PyPDF2

使用方法
1、使用配置文件进行分割

	eg:
	
	python pdf_splite.py  pdf_name.pdf -f conf_name.txt
2、使用固定页数进行分割

	eg：
	python pdf_splite.py pdf_name.pdf -i conf_name.txt
3、使用指定分割点进行分割

	eg：
	
	python pdf_splite.py pdf_name.pdf -s 1,5,10,15,30
注意：

1、配置文件内容需使用指定格式，如下：
1-5
10-15
20-30

2、使用指定分割点分割，必须以1开头，以总页数量结尾
