# async_queue.py

import argparse
import asyncio
import sys
from collections import Counter
from typing import NamedTuple
from urlib.parse import urljoin

import aiohttp
from bs4 import BeautifulSoup


class Job(NamedTuple):