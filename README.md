# DPayOcr

[![PyPI version](https://badge.fury.io/py/dpayocr.svg)](https://badge.fury.io/py/dpayocr)

## 介绍

`dpayocr` 可以识别支付宝微信收款码信息。例如支付类型，支付金额，支付链接。

## 安装

```bash
$ pip install dpayocr
```

## 使用

### 命令行使用

```
dpayocr 66.JPG
```

输出

```
PayQrCode(pay_type=1, price=66.0, url='https://qr.alipay.com/xxx')
```

### 接口

```python
>>> from dpayocr import parse_pay_qr_code
>>> fp = '66.JPG' # 可以传入文件名或者二进制IO
>>> parse_pay_qr_code(fp)
PayQrCode(pay_type=1, price=66.0, url='https://qr.alipay.com/xxx')
```

## 问题

### 在虚拟环境找不到 Tesseract 命令

```
# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
```

## 参考链接

- [tesseract](https://github.com/tesseract-ocr/tesseract)
- [pytesseract](https://pypi.org/project/pytesseract/)
- [pyzbar](https://pypi.org/project/pyzbar/)
- [A comprehensive guide to OCR with Tesseract, OpenCV and Python](https://nanonets.com/blog/ocr-with-tesseract/)
