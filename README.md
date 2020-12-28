# midscan

## 安装方法

```
# 安装依赖
pip install -r requirements.txt

# 安装lxml
pip install lxml-4.4.3-cp27-cp27m-win_amd64.whl

```

## 使用方法

```
# 整理nmap扫描结果
python midscan.py [-f|--file] [<NMAP扫描结果路径,可全路径,也可相对路径>]

# 存活扫描整理结果
python midscan.py [-s|--scan] [扫描结果文件名|或为空采用默认]  
```

> 

## 示例

> 当前目录文件
```
│  midscan.py --> 程序主入口
│  SCAN_IP_PORT_RESULT.txt --> 扫描结果
│  SORT_IP_RESULT.txt --> namp整理结果
│  nmap_result.xml--> nmap扫描结果导出xml
```

```
# 整理nmap扫描结果 -> nmap_result.xml
python midscan.py -f nmap_result.xml

# 结果被保存到 SORT_IP_RESULT.txt

# 存活扫描整理结果
python midscan.py -s

# 结果被保存到 SCAN_IP_PORT_RESULT.txt

```