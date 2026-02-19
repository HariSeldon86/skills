'''
# description: A simple script to crawl a webpage and return its content as markdown. Optionally saves the output to a file.
# requires: crawl4ai
# note: After installing, it needs to run crawl4ai-setup once to download the browser binaries - this is a one-time setup step, not per-run.

# If you need to install crawl4ai, use virtual environment
python -m venv .venv
.venv/Scripts/activate
pip install crawl4ai

# Print to stdout
python web_crawl.py https://example.com

# Save to file
python web_crawl.py https://example.com -o out.md

# Built-in help
python web_crawl.py --help
'''

#!/usr/bin/env python3
# web_crawl.py
import sys
import argparse
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, BrowserConfig


async def crawl(url: str, output_file: str | None = None) -> str:
    browser_config = BrowserConfig(headless=True)
    run_config = CrawlerRunConfig(
        magic=True,
        remove_overlay_elements=True
    )

    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(url=url, config=run_config)
        markdown = result.markdown  # type: ignore

        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(markdown)
            return f"Saved to {output_file}"
        else:
            return markdown


def parse_args():
    parser = argparse.ArgumentParser(
        description="Crawl a webpage and return its content as markdown."
    )
    parser.add_argument(
        "url",
        help="URL to crawl"
    )
    parser.add_argument(
        "-o", "--output-file",
        dest="output_file",
        default=None,
        help="Optional file path to save the markdown output"
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    try:
        result = asyncio.run(crawl(args.url, args.output_file))
        print(result)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)