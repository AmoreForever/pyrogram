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

import pyrogram
from pyrogram import raw
from pyrogram import types


class GetStoryViewsList:
    async def get_story_views_list(
        self: "pyrogram.Client",
        story_id: int,
        offset_date: int = 0,
        offset_id: int = 0,
        limit: int = 0,
    ) -> "types.StoryViewsList":
        """Get stories views list.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            story_id (``int``):
                Unique identifier of the target story.

            offset_date (``int``, *optional*):
                Offset date of the views to return.

            offset_id (``int``, *optional*):
                Offset ID of the views to return.

            limit (``int``, *optional*):
                Limits the number of views to be retrieved.

        Returns:
            :obj:`~pyrogram.types.StoryViewsList`: On success, stories views list is returned.

        Example:
            .. code-block:: python

                # Get stories views list
                views = await app.get_story_views_list(123456789)

                for view in views:
                    print(view)
        """
        r = await self.invoke(
            raw.functions.stories.GetStoryViewsList(
                id=story_id,
                offset_date=offset_date,
                offset_id=offset_id,
                limit=limit,
            )
        )
        return types.StoryViewsList._parse(r)
