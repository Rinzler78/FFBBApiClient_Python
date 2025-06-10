from dataclasses import dataclass
from typing import Any, Optional

from ..utils.converters import from_int, from_none, from_union


@dataclass
class PageInfo:
    """
    Data class representing pagination information for API responses.
    """

    total_results: Optional[int] = None
    results_per_page: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> "PageInfo":
        """
        Create a PageInfo instance from a dictionary.
        """
        assert isinstance(obj, dict)
        total_results = from_union([from_int, from_none], obj.get("totalResults"))
        results_per_page = from_union([from_int, from_none], obj.get("resultsPerPage"))
        return PageInfo(total_results, results_per_page)

    def to_dict(self) -> dict:
        """
        Convert the PageInfo instance to a dictionary.
        """
        result: dict = {}
        if self.total_results is not None:
            result["totalResults"] = from_union(
                [from_int, from_none], self.total_results
            )
        if self.results_per_page is not None:
            result["resultsPerPage"] = from_union(
                [from_int, from_none], self.results_per_page
            )
        return result

    def __eq__(self, other: Any) -> bool:
        """
        Check equality with another PageInfo instance.
        """
        if not isinstance(other, PageInfo):
            return False
        return (
            self.total_results == other.total_results
            and self.results_per_page == other.results_per_page
        )

    def __hash__(self) -> int:
        """
        Compute the hash of the PageInfo instance.
        """
        return hash((self.total_results, self.results_per_page))
