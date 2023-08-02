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
from ..object import Object


class AllReadedStories(Object):
    """All readed stories

    Parameters:
        user_id (``int`` ``64-bit``):
            User identifier

        max_id (``int`` ``32-bit``):
            Max id of stories
    """

    def __init__(
        self, *,
        user_id: int,
        max_id: int
    ):
        super().__init__()

        self.user_id = user_id
        self.max_id = max_id

    @staticmethod
    def _parse(story: "raw.types.UpdateReadStories") -> "AllReadedStories":
        return AllReadedStories(
            user_id=story.user_id,
            max_id=story.max_id
        )
