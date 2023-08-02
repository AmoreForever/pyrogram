#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from typing import List, Optional

from pyrogram import raw
from pyrogram import types
from ..object import Object


class AllStories(Object):
    """All readed stories

    Parameters:
        count (``int`` ``32-bit``):
            Count of stories

        state (``str``):
            State of stories

        user_stories (List of :obj:`UserStories <pyrogram.raw.base.UserStories>`):
            List of user stories

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            List of users

        has_more (``bool``, *optional*):
            Has more stories
    """

    def __init__(
        self, *,
        count: int,
        state: str,
        user_stories: List["raw.base.UserStories"],
        users: List["types.User"],
        has_more: Optional[bool] = None
    ):
        super().__init__()

        self.count = count
        self.state = state
        self.user_stories = user_stories
        self.users = users
        self.has_more = has_more

    @staticmethod
    def _parse(all_stories: "raw.types.AllStories") -> "AllStories":
        return AllStories(
            count=all_stories.count,
            state=all_stories.state,
            user_stories=all_stories.user_stories,
            users=all_stories.users,
            has_more=all_stories.has_more
        )
