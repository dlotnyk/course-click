# Installation
Install `Selenium`
```
pip install -r requirements.txt
```
or
```
pip install selenium
```
Here the Chrome Webdriver is used. Required version download from off website:

https://sites.google.com/a/chromium.org/chromedriver/downloads

and extract the last into the `PATH` path or add to the `PATH`.

# Usage

Change `urls`, `user_name`, `password`, `xpath` variables to yours. Enjoy

# Logger

Log message has such `regex` pattern (Useful for PyCharm log plugin):

```
^([0-9]\w+-[0-9]\w-[0-9]\w\s[0-9]\w:[0-9]\w:[0-9]\w,[0-9]\w+)\s-\s([A-Z]\w+)\s-\s(.[a-z]\w+.)\s-\s(line:\s[0-9]\w+)\s-\s([\s\S]*)$
```

with a start pattern `^2`
