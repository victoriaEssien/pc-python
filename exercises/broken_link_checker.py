import argparse
import requests
from bs4 import BeautifulSoup


def check_links(url):
    try:
        # Fetch the webpage
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [a['href'] for a in soup.find_all('a', href=True)]

        print(f"\nFound {len(links)} links on the page.\n")

        broken_links = []
        for link in links:
            # Handle relative URLs
            if link.startswith('/'):
                link = requests.compat.urljoin(url, link)

            try:
                res = requests.head(link, timeout=5)
                if res.status_code >= 400:
                    broken_links.append((link, res.status_code))
            except Exception as e:
                broken_links.append((link, "Error"))

        # Display results
        print(f"\nBroken Links ({len(broken_links)}):")
        for link, status in broken_links:
            print(f"- {link} (Status: {status})")

        if not broken_links:
            print("No broken links found! 🎉")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")


if __name__ == "__main__":
    # Define command-line arguments
    parser = argparse.ArgumentParser(description="Check a website for broken links.")
    parser.add_argument("url", help="The URL of the website to check.")

    args = parser.parse_args()
    check_links(args.url)
