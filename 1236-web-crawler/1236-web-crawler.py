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

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        from urllib.parse import urlparse

        output = set()
        start_host = urlparse(startUrl).hostname

        stack = [startUrl]
        while stack:
            url = stack.pop()
            if url in output:
                continue
            output.add(url)
            for next_urls in htmlParser.getUrls(url):
                if urlparse(next_urls).hostname == start_host:
                    if next_urls not in stack:
                        stack.append(next_urls)
        
        return list(output)