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

from typing import List

import pyrogram
from pyrogram import raw
from pyrogram import types


class GetAllReadedStories:
    async def get_all_readed_stories(
        self: "pyrogram.Client",
    ) -> List["types.AllReadedStories"]:
        """Get all readed stories.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            No parameters required.

        Returns:
            List of :obj:`~pyrogram.types.AllReadedUserStories`: On success, a list of all read user stories is returned.

        Example:
            .. code-block:: python

                # Get all read user stories
                stories = app.get_all_read_user_stories()

                for story in stories:
                    print(story)
        """
        r = await self.invoke(
            raw.functions.stories.GetAllReadUserStories()
        )
        return types.AllReadedStories._parse(r)
