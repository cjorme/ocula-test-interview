import asyncio
from playwright.async_api import async_playwright

async def count_blog_posts(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(url)

        # Count the number of blog posts on the first page
        blog_posts_first_page = await page.query_selector_all('.blog-title')
        count_first_page = len(blog_posts_first_page)

        # Navigate to the second page
        await page.click('text="Older Posts"')
        await page.wait_for_selector('.blog-title')

        # Count the number of blog posts on the second page
        blog_posts_second_page = await page.query_selector_all('.blog-title')
        count_second_page = len(blog_posts_second_page)

        await browser.close()
        return count_first_page + count_second_page

async def main():
    url = 'https://ocula.tech/resources'
    total_posts = await count_blog_posts(url)
    print(f"Total blog posts: {total_posts}")


# keep in this file, to allow running manually for debug purposes
if __name__ == "__main__":
    asyncio.run(main())