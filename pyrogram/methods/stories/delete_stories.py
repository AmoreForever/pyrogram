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

from typing import List, Union, Iterable

import pyrogram
from pyrogram import raw


class DeleteStories:
    async def delete_stories(
        self: "pyrogram.Client",
        stories_ids: Union[int, Iterable[int]],
    ) -> List[int]:
        """Delete stories.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            stories_ids (``int`` | ``list``):
                Unique identifier (int) or list of unique identifiers (list of int) for the target stories.

        Returns:
            List of ``int``: List of deleted stories IDs

        Example:
            .. code-block:: python

                # Delete a single story
                app.delete_stories(123456789)

                # Delete multiple stories
                app.delete_stories([123456789, 987654321])
        """
        stories_ids = [stories_ids] if isinstance(stories_ids, int) else list(stories_ids)

        r = await self.invoke(
            raw.functions.stories.DeleteStories(
                id=stories_ids
            )
        )
        return r
