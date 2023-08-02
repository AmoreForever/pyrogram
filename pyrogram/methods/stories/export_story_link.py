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


class ExportStoryLink:
    async def export_story_link(
        self: "pyrogram.Client",
        user_id: Union[int, str],
        story_id: int,
    ) -> "types.ExportedStoryLink":
        """Export a story link.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            user_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target user.

            story_id (``int``):
                Unique identifier of the target story.

        Returns:
            :obj:`~pyrogram.types.ExportedStoryLink`: On success, a link to the exported story is returned.

        Example:
            .. code-block:: python

                # Export a story link
                app.export_story_link("onetimeusername", 1)
        """
        r = await self.invoke(
            raw.functions.stories.ExportStoryLink(
                user_id=await self.resolve_peer(user_id),
                id=story_id
            )
        )
        return r.link
