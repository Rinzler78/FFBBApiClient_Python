from dataclasses import dataclass
from typing import Any, List, Optional

from .converters import from_list, from_none, from_str, from_union, is_type, to_class


@dataclass
class News:
    id: Optional[int] = None
    date: Optional[str] = None
    url: Optional[str] = None
    author: Optional[str] = None
    category: Optional[str] = None
    title: Optional[str] = None
    image: Optional[str] = None
    excerpt: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "News":
        assert isinstance(obj, dict)
        id = from_union([from_none, lambda x: int(from_str(x))], obj.get("id"))
        date = from_union([from_str, from_none], obj.get("date"))
        url = from_union([from_str, from_none], obj.get("url"))
        author = from_union([from_str, from_none], obj.get("author"))
        category = from_union([from_str, from_none], obj.get("category"))
        title = from_union([from_str, from_none], obj.get("title"))
        image = from_union([from_str, from_none], obj.get("image"))
        excerpt = from_union([from_str, from_none], obj.get("excerpt"))
        return News(id, date, url, author, category, title, image, excerpt)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["id"] = from_union(
                [
                    lambda x: from_none((lambda x: is_type(type(None), x))(x)),
                    lambda x: from_str(
                        (lambda x: str((lambda x: is_type(int, x))(x)))(x)
                    ),
                ],
                self.id,
            )
        if self.date is not None:
            result["date"] = from_union([from_str, from_none], self.date)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        if self.author is not None:
            result["author"] = from_union([from_str, from_none], self.author)
        if self.category is not None:
            result["category"] = from_union([from_str, from_none], self.category)
        if self.title is not None:
            result["title"] = from_union([from_str, from_none], self.title)
        if self.image is not None:
            result["image"] = from_union([from_str, from_none], self.image)
        if self.excerpt is not None:
            result["excerpt"] = from_union([from_str, from_none], self.excerpt)
        return result

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, News):
            return False
        return (
            self.id == other.id
            and self.date == other.date
            and self.url == other.url
            and self.author == other.author
            and self.category == other.category
            and self.title == other.title
            and self.image == other.image
            and self.excerpt == other.excerpt
        )

    def __hash__(self) -> int:
        return hash(
            (
                self.id,
                self.date,
                self.url,
                self.author,
                self.category,
                self.title,
                self.image,
                self.excerpt,
            )
        )


def news_from_dict(s: Any) -> List[News]:
    return from_list(News.from_dict, s)


def news_to_dict(x: List[News]) -> Any:
    return from_list(lambda x: to_class(News, x), x)
