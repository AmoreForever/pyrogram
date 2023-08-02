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

from typing import Union

import pyrogram
from pyrogram import raw
from pyrogram import types


class GetPinnedStories:
    async def get_pinned_stories(
        self: "pyrogram.Client",
        user_id: Union[int, str],
        offset_id: int = 0,
        limit: int = 0,
    ) -> "types.Stories":
        """Get pinned stories.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            user_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target user.

            offset_id (``int``, *optional*):
                Offset ID of the pinned stories to return.

            limit (``int``, *optional*):
                Limits the number of pinned stories to be retrieved.

        Returns:
            :obj:`~pyrogram.types.Stories`: On success, a list of pinned stories is returned.

        Example:
            .. code-block:: python

                # Get pinned stories
                stories = app.get_pinned_stories("onetimeusername")

                for story in stories:
                    print(story)
        """
        r = await self.invoke(
            raw.functions.stories.GetPinnedStories(
                user_id=await self.resolve_peer(user_id),
                offset_id=offset_id,
                limit=limit,
            )
        )
        return types.Stories._parse(r)
