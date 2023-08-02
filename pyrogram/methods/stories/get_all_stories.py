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

import pyrogram
from pyrogram import raw
from pyrogram import types


class GetAllStories:
    async def get_all_stories(
        self: "pyrogram.Client",
        next: Optional[bool] = None,
        hidden: Optional[bool] = None,
        state: Optional[str] = None,
    ) -> List["types.AllStories"]:
        """Get all stories.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            next (``bool``, *optional*):
                If set to ``True``, the next stories will be returned.

            hidden (``bool``, *optional*):
                If set to ``True``, the hidden stories will be returned.

            state (``str``, *optional*):
                The state of the stories to return.

        Returns:
            :obj:`~pyrogram.types.AllStories`: On success, a list of all stories is returned.

        Example:
            .. code-block:: python

                # Get all stories
                stories = app.get_all_stories()

                for story in stories:
                    print(story)
        """
        r = await self.invoke(
            raw.functions.stories.GetAllStories(
                next=next,
                hidden=hidden,
                state=state
            )
        )
        return types.AllStories._parse(r)
