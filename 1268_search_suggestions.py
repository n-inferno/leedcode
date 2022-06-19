# https://leetcode.com/problems/search-suggestions-system/
from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        results = []
        for i in range(len(searchWord)):
            prefix = searchWord[:i + 1]
            take = []
            found = False
            for product in products:
                if len(take) >= 3:
                    break
                if product.startswith(prefix):
                    found = True
                    take.append(product)
                elif found:
                    break
            results.append(take)

        return results


if __name__ == '__main__':
    assert Solution().suggestedProducts(products=["mobile", "mouse", "moneypot", "monitor", "mousepad"], searchWord="mouse") == [
        ["mobile", "moneypot", "monitor"], ["mobile", "moneypot", "monitor"], ["mouse", "mousepad"], ["mouse", "mousepad"],
        ["mouse", "mousepad"]
    ]
    assert Solution().suggestedProducts(products=["havana"], searchWord="havana") == [["havana"], ["havana"], ["havana"],
                                                                                      ["havana"], ["havana"], ["havana"]]
    assert Solution().suggestedProducts(products=["bags", "baggage", "banner", "box", "cloths"], searchWord="bags") == [
        ["baggage", "bags", "banner"], ["baggage", "bags", "banner"], ["baggage", "bags"], ["bags"]]
