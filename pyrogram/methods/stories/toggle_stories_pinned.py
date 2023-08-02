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


class ToggleStoriesPinned:
    async def toggle_stories_pinned(
        self: "pyrogram.Client",
        stories_ids: Union[int, Iterable[int]],
        pinned: bool,
    ) -> List[int]:
        """Toggle stories pinned.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            stories_ids (List of ``int`` ``32-bit``):
                List of unique identifiers of the target stories.

            pinned (``bool``):
                If set to ``True``, the stories will be pinned.

        Returns:
            List of ``int``: List of pinned stories IDs

        Example:
            .. code-block:: python

                # Pin a single story
                await app.toggle_stories_pinned(123456789, True)

        """
        stories_ids = [stories_ids] if isinstance(stories_ids, int) else list(stories_ids)

        r = await self.invoke(
            raw.functions.stories.TogglePinned(
                id=stories_ids,
                pinned=pinned
            )
        )
        return r
