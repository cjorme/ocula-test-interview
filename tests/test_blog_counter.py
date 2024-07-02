import pytest
import asyncio
from resources.blog_count import count_blog_posts

@pytest.mark.asyncio
async def test_count_blog_posts():
    url = 'https://ocula.tech/resources'
    total_posts = await count_blog_posts(url)
    assert total_posts == 25, f"Expected 25 blog posts, but found {total_posts}"

# removed as only running via pytest, rather than standalone script
# if __name__ == "__main__":
#     asyncio.run(test_count_blog_posts())