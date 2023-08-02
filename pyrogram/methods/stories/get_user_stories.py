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


class GetUserStories:
    async def get_user_stories(
        self: "pyrogram.Client",
        user_id: Union[int, str],
    ) -> "types.UserStories":
        """Get stories by id.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            user_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target user.

        Returns:
            :obj:`~pyrogram.types.UserStories`: On success, a list of user stories is returned.

        Example:
            .. code-block:: python

                # Get user stories
                stories = await app.get_user_stories("@onetimeusername")

                for story in stories:
                    print(story)
        """
        r = await self.invoke(
            raw.functions.stories.GetUserStories(
                user_id=await self.resolve_peer(user_id)
            )
        )
        return types.UserStories._parse(r)
