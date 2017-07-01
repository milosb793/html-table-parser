#!/usr/bin/python

from bs4 import BeautifulSoup
from sys import argv
import json
import requests


class TableParser():
    """
    This is simple tool for extracting HTML table from page to structural, manipulative data
    """

    def __init__(self, url, data_post=None, selector=None, value=None):
        """
            @url is required argument, it's presents a page whom table is.
            @data_post is data for POST request.
            @selector argument is for type of selector: id, class, name.
            If selector is None, it means that table is selected by tag name
            @value is value of selector, or if Selector is None, it represents a
            index of a table in document, if there is many tables at page.
            Leave as None if there is just one table
        """
        self.url = url
        self.selector = selector
        self.value = value
        request_response = None

        if data_post is not None:
            self.data_post = data_post
            headers = {'content-type': 'application/json'}
            request_response = requests.post(
                url,
                data=data_post,
                headers=headers,
                verify=False
            ).text
        else:
            request_response = requests.get(url).text

        # selecting valid table
        if selector is not None:
            self.table_soap = BeautifulSoup(request_response).find("table", {selector: value})
        elif value is not None:
            self.table_soap = BeautifulSoup(request_response).find_all("table")[value]
        else:
            self.table_soap = BeautifulSoup(request_response).find("table")

        self.header = self.headerAsList()
        self.body = self.bodyAsList()
        self.number_of_cells_per_row = self.numberOfCellsPerRow()
        self.number_of_rows = len(self.body)
        self.full_table = self.header + self.body
        self.max_length_of_cell = self.maxLengthOfCell()

    def headerAsList(self):
        list_ = []
        # this should be first row, no matter it has th or td in itself
        header_raw = self.table_soap.find("tr")
        for item in header_raw:
            if not isEmpty(item):
                list_.append(item.text)
        return list_


    def numberOfCellsPerRow(self):
        rows = self.table_soap.find("tr")
        counter = 0
        for td in rows:
            if not isEmpty(td):
                counter += 1
        return counter


    def bodyAsList(self):
        counter = 0
        body_raw = self.table_soap.find_all("tr")
        list_ = []

        for item in body_raw:
            counter += 1
            if counter == 1:
                continue
            elif not isEmpty(item):
                list_.append(filterList(item.text.split("\n")))
        return list_


    def printTable(self):
        print("\n", "-" * self.max_length_of_cell * self.number_of_cells_per_row)
        print("|", end='')
        for th in self.header:
            print(("{:^" + str(self.maxLengthOfCell()) + "}").format(th), end="")
            print("|", end='')
        print("\n", "-" * self.max_length_of_cell * self.number_of_cells_per_row)

        for tr in self.body:
            print("|", end='')
            for td in tr:
                print(("{:^" + str(self.maxLengthOfCell()) + "}").format(td), end="")
                print("|", end='')
            print()
        print("\n", "-" * self.max_length_of_cell * self.number_of_cells_per_row)


    def getAllCellsOfTable(self):
        list_ = []
        for row in self.full_table:
            for td in row:
                list_.append(td)
        return list_


    def maxLengthOfCell(self):
        max_cell_len = list(map((lambda x: len(x)), self.getAllCellsOfTable()))
        return max(max_cell_len)


def isEmpty(x):
    if x is None or x == "" or x == " " or x == "\n" or x == "\t":
        return True
    return False


def filterList(list_):
    return list(filter((lambda x: isEmpty(x) != True), list_))


if __name__ == "__main__":

    ### via argvs, just for GET req.  ###
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
        
           ### POST example ###
        # url = "http://example.com/table"
        # data = json.dumps({"username":"user1","pass":"ex@mp1e"})
        # selector = "id"
        # value = "table-example"
        # dummy_obj = TableParser(url=url, data_post=data, selector=selector, value=value)


    print(dummy_obj.printTable())
