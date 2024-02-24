from dataclasses import dataclass
from datetime import datetime
from typing import Any, Optional

from .converters import (
    from_datetime,
    from_int,
    from_none,
    from_str,
    from_union,
    to_class,
)
from .resource_id import ResourceID
from .thumbnails import Thumbnails


@dataclass
class Snippet:
    published_at: Optional[datetime] = None
    channel_id: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    thumbnails: Optional[Thumbnails] = None
    channel_title: Optional[str] = None
    playlist_id: Optional[str] = None
    position: Optional[int] = None
    resource_id: Optional[ResourceID] = None
    video_owner_channel_title: Optional[str] = None
    video_owner_channel_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "Snippet":
        assert isinstance(obj, dict)
        published_at = from_union([from_datetime, from_none], obj.get("publishedAt"))
        channel_id = from_union([from_str, from_none], obj.get("channelId"))
        title = from_union([from_str, from_none], obj.get("title"))
        description = from_union([from_str, from_none], obj.get("description"))
        thumbnails = from_union(
            [Thumbnails.from_dict, from_none], obj.get("thumbnails")
        )
        channel_title = from_union([from_str, from_none], obj.get("channelTitle"))
        playlist_id = from_union([from_str, from_none], obj.get("playlistId"))
        position = from_union([from_int, from_none], obj.get("position"))
        resource_id = from_union(
            [ResourceID.from_dict, from_none], obj.get("resourceId")
        )
        video_owner_channel_title = from_union(
            [from_str, from_none], obj.get("videoOwnerChannelTitle")
        )
        video_owner_channel_id = from_union(
            [from_str, from_none], obj.get("videoOwnerChannelId")
        )
        return Snippet(
            published_at,
            channel_id,
            title,
            description,
            thumbnails,
            channel_title,
            playlist_id,
            position,
            resource_id,
            video_owner_channel_title,
            video_owner_channel_id,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        if self.published_at is not None:
            result["publishedAt"] = from_union(
                [lambda x: x.isoformat(), from_none], self.published_at
            )
        if self.channel_id is not None:
            result["channelId"] = from_union([from_str, from_none], self.channel_id)
        if self.title is not None:
            result["title"] = from_union([from_str, from_none], self.title)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.thumbnails is not None:
            result["thumbnails"] = from_union(
                [lambda x: to_class(Thumbnails, x), from_none], self.thumbnails
            )
        if self.channel_title is not None:
            result["channelTitle"] = from_union(
                [from_str, from_none], self.channel_title
            )
        if self.playlist_id is not None:
            result["playlistId"] = from_union([from_str, from_none], self.playlist_id)
        if self.position is not None:
            result["position"] = from_union([from_int, from_none], self.position)
        if self.resource_id is not None:
            result["resourceId"] = from_union(
                [lambda x: to_class(ResourceID, x), from_none], self.resource_id
            )
        if self.video_owner_channel_title is not None:
            result["videoOwnerChannelTitle"] = from_union(
                [from_str, from_none], self.video_owner_channel_title
            )
        if self.video_owner_channel_id is not None:
            result["videoOwnerChannelId"] = from_union(
                [from_str, from_none], self.video_owner_channel_id
            )
        return result

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Snippet):
            return False
        return (
            self.published_at == other.published_at
            and self.channel_id == other.channel_id
            and self.title == other.title
            and self.description == other.description
            and self.thumbnails == other.thumbnails
            and self.channel_title == other.channel_title
            and self.playlist_id == other.playlist_id
            and self.position == other.position
            and self.resource_id == other.resource_id
            and self.video_owner_channel_title == other.video_owner_channel_title
            and self.video_owner_channel_id == other.video_owner_channel_id
        )

    def __hash__(self) -> int:
        return hash(
            (
                self.published_at,
                self.channel_id,
                self.title,
                self.description,
                self.thumbnails,
                self.channel_title,
                self.playlist_id,
                self.position,
                self.resource_id,
                self.video_owner_channel_title,
                self.video_owner_channel_id,
            )
        )
