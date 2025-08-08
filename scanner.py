from vulnerabilities import sqli, xss

def main(url):
    sqli.test_sqli(url)
    xss.test_xss(url)

if __name__ == "__main__":
    main("http://example.com")
