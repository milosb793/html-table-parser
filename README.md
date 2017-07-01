# html-table-parser
This is simple tool for extracting HTML table data from page to structural, manipulative data, written in Python

## How to run 

You may run compiled script from `dist/` folder. Or you can run script directly. For that, you need to install following:
- Python interpreter with `sudo apt-get install python`
- Modules Requests and Beautiful Soap with: `pip install requests` and `pip install beautifulsoup4` 


In `src/` folder, there is file `AllInOneFile.py` where is class code and testing code in once. And, there is separately files. 

## About 

Script can be run from terminal with params. Example:
`python AllInOneFile.py "https://datatables.net/examples/data_sources/dom.html" "id" "example" ` -> this is working just for GET request for now. 

* To make POST request with params, you need to do following:
`url = "http://example.com/table"`
`payload = json.dumps({"username":"user1","pass":"ex@mp1e"})`
`headers` are in TableParser class
`verify` flag is set in TableParser class, if is set as True, it will check certificates if there is https request. Else, if is set to False, it will bypass checking. 

## Other ##

This is an learning project.
Feel free to contribute and join.
Thank you



