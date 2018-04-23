import aiohttp
import asyncio
import async_timeout
import re


URL = 'https://www.python.org/'


async def fetch(session, url):
    with async_timeout.timeout(10):
        async with session.get(url.lower()) as response:
            return await response.text()


async def main(url):
    body = None
    domain = url.split('//')[-1].split('/')[0]
    proto = ("%r" % (url.split(':')[0] + '://'))[1:-1]
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, URL)
        # print(body)
    if html:
        pattern = 'href="([^"]*)"[^>]*>([\s\S]*?)</a>'
        regex = re.compile(r'^((http|https):)?//')
        hrefs = []
        for href in re.findall(pattern, html):
            if regex.search(href[0]) and not re.search(domain, href[0]):
                # hrefs.append(re.sub(r'^//', r'https://', href[0]))
                hrefs.append(re.sub(r'^//', proto, href[0]))
        return hrefs


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    external_urls = loop.run_until_complete(main(URL))
    for xurl in external_urls:
        print(xurl)
