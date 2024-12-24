from playwright.sync_api import sync_playwright
from rich import print
import urllib.parse

def scrape_cointopper_news():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=False)  # Set headless=True for production
        page = browser.new_page()
 
        # Navigate to the target URL
        url = "https://cointopper.com/news"
        page.goto(url)

        # Wait for the news cards to load
        page.wait_for_selector('div[class*="shadow hover:shadow-xl"]')

        # Select news cards
        news_cards = page.query_selector_all('div[class*="shadow hover:shadow-xl"]')
        print(f"[blue]Found {len(news_cards)} news cards[/blue]")  # Debugging print

        news_data = []
        for card in news_cards:
            try: 
                title = card.query_selector('h2').inner_text() 
                date = card.query_selector('span.text-pgray-400').inner_text() 
                link = card.query_selector('a').get_attribute('href') 
                tags = [tag.inner_text() for tag in card.query_selector_all('span[class*="bg-slate-50"]')] 
                image_url = card.query_selector('img').get_attribute('src')

                # Append the extracted data
                news_data.append({
                    "title": title,
                    "date": date,
                    "link": f"https://cointopper.com{link}",
                    "tags": tags,
                    "image_url": urllib.parse.unquote(image_url.split('&')[0]).replace('/_next/image?url=', ''),
                })
            except Exception as e:
                print(f"[red]Error scraping card: {e}[/red]")

        # Print the scraped data
        print("[bold green]Scraped News Data:[/bold green]")
        for news in news_data:
            print(news)

        # Close the browser
        browser.close()

# Call the scraper function
if __name__ == "__main__":
    scrape_cointopper_news()
