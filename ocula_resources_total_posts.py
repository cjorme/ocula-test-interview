import asyncio
from playwright.async_api import async_playwright

async def count_posts():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://ocula.tech/resources")

        total_posts = 0
        while True:
            posts = await page.query_selector_all(".post-item")  # Adjust the selector based on the actual class/element
            total_posts += len(posts)
            
            next_button = await page.query_selector("a.next")
            if next_button:
                await next_button.click()
                await page.wait_for_load_state('networkidle')
            else:
                break

        await browser.close()
        return total_posts

if __name__ == "__main__":
    total_posts = asyncio.run(count_posts())
    print(f"Total number of posts: {total_posts}")
