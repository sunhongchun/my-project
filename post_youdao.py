import requests



url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
form_data={
    'i': '我和你都是中国人',
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '15892034528866',
    'sign': '1224004e05a6408886446af5fb5ac69a',
    'ts': '1589203452886',
    'bv': 'dc1dbc42604a22f25b4e2b2e26c074bb',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_CLICKBUTTION'
}
requests.post(url,form_data)