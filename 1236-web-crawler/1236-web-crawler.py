# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

from urllib.parse import urlparse
from collections import deque

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        output = set()
        start_host = urlparse(startUrl).hostname
        queue = deque([startUrl])

        output.add(startUrl)
        while queue:
            url = queue.popleft()
            for next_url in htmlParser.getUrls(url):
                if urlparse(next_url).hostname == start_host and next_url not in output:
                    output.add(next_url)
                    queue.append(next_url)
        return list(output)
