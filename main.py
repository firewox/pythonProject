# This is a sample Python script.

# Press Alt+Shift+X to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+Shift+B to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


import aiohttp
import asyncio


async def get_data(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    urls = ["https://www.baidu.com","https://www.bilibili.com","https://www.taobao.com"]
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.create_task(get_data(session, url))
            tasks.append(task)
        htmls = await asyncio.gather(*tasks)
        for html in htmls:
            print(f"html: {html[:10]}")

asyncio.run(main())




