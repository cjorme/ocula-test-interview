import pytest
import asyncio
from playwright.async_api import async_playwright

@pytest.mark.asyncio
async def test_count_blog_posts():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://ocula.tech/resources")

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
    total_posts = await test_count_blog_posts()
    assert total_posts == 25, f"Expected 25 blog posts, but found {total_posts}"

asyncio.run(main())
