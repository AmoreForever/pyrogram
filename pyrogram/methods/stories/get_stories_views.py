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

from typing import Union, Iterable

import pyrogram
from pyrogram import raw
from pyrogram import types


class GetStoriesViews:
    async def get_stories_views(
        self: "pyrogram.Client",
        stories_ids: Union[int, Iterable[int]],
    ) -> "types.StoryViews":
        """Get stories views.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            stories_ids (List of ``int`` ``32-bit``):
                List of unique identifiers of the target stories.

        Returns:
            :obj:`~pyrogram.types.StoryViews`: On success, a list of stories views is returned.

        Example:
            .. code-block:: python

                # Get stories views
                views = await app.get_stories_views([1, 2, 3])

                for view in views:
                    print(view)
        """
        stories_ids = [stories_ids] if isinstance(stories_ids, int) else list(stories_ids)

        r = await self.invoke(
            raw.functions.stories.GetStoriesViews(
                id=stories_ids
            )
        )
        return types.StoryViews._parse(r)
