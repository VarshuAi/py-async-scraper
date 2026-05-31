import urllib.request
import re
import sys

def scrape_links(url):
    print(f"[*] Starting scraper parsing links on target: {url}")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            links = re.findall(r'href=["\'](https?://[^"\']+)["\']', html)
            print(f"[+] Found {len(links)} unique links in body markup.")
            for link in list(set(links))[:20]:
                print(f"  --> {link}")
    except Exception as e:
        print(f"[-] Scraper aborted: {e}")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "https://github.com"
    scrape_links(target)