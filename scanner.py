import argparse
import requests
from bs4 import BeautifulSoup

def check_security_headers(url):
    try:
        response = requests.get(url)
        headers = response.headers

        print("\n[+] Checking Security Headers...")
        important_headers = [
            "Content-Security-Policy",
            "X-Content-Type-Options",
            "Strict-Transport-Security",
            "X-Frame-Options",
            "X-XSS-Protection"
        ]
        for header in important_headers:
            if header in headers:
                print(f"[OK] {header} found")
            else:
                print(f"[MISSING] {header} is not set")
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Could not connect: {e}")

def main():
    parser = argparse.ArgumentParser(description="OWASP Basic Security Scanner")
    parser.add_argument("-u", "--url", required=True, help="Target URL to scan")
    args = parser.parse_args()

    print(f"[*] Starting scan on {args.url}")
    check_security_headers(args.url)

if __name__ == "__main__":
    main()
