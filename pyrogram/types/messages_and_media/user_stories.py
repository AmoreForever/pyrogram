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

from pyrogram import raw
from pyrogram import types
from ..object import Object
from typing import List


class UserStories(Object):
    """User stories

    Parameters:
        stories (:obj:`stories.UserStories <pyrogram.raw.base.stories.UserStories>`):
            List of stories

        users (List of :obj:`User <pyrogram.types.User>`):
            List of users
    """

    def __init__(
        self, *,
        stories: "raw.base.stories.UserStories",
        users: List["types.User"]
    ):
        super().__init__()

        self.stories = stories
        self.users = users

    @staticmethod
    def _parse(user_stories: "raw.base.stories.UserStories") -> "UserStories":
        return UserStories(
            stories=user_stories.stories,
            users=user_stories.users
        )
