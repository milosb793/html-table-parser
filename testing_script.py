#!/usr/bin/python

import requests
import json
from sys import argv
from posao.TableParser import TableParser



### via args, just for GET req. EXPERIMENTAL ###

if len(argv) == 2:
    url = argv[0]
    selector = argv[1]
    value = argv[2]
    dummy_obj = TableParser(url=url, selector=selector, value=value)
else:
    url = "https://datatables.net/examples/data_sources/dom.html"
    dummy_obj = TableParser(url=url, selector="id", value="example")

    # url = "https://www.w3schools.com/html/html_tables.asp"
    # dummy_obj = TableParser(url=url, selector="id", value="customers")


print(dummy_obj.printTable())
