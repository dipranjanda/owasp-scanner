# xss.py
def test_xss(url):
    payload = "<script>alert('XSS')</script>"
    # scanning logic here

# sqli.py
def test_sqli(url):
    payload = "' OR '1'='1"
    # scanning logic here

