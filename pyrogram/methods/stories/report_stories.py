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


class ReportStories:
    async def report_stories(
        self: "pyrogram.Client",
        user_id: Union[int, str],
        stories_ids: Union[int, Iterable[int]],
        message: str,
        reason: raw.base.ReportReason = raw.types.InputReportReasonSpam,
    ) -> bool:
        """Get stories by id.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            user_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target user.

            stories_ids (List of ``int`` ``32-bit``):
                List of unique identifiers of the target stories.

            reason (:obj:`~pyrogram.raw.base.ReportReason`, *optional*):
                Reason for reporting the stories.

            message (``str``):
                Additional information about the report.

        Returns:
            ``bool``: On success, True is returned.

        Example:
            .. code-block:: python

                # Report stories
                await app.report_stories("@onetimeusername", [1, 2, 3])
        """
        stories_ids = [stories_ids] if isinstance(stories_ids, int) else list(stories_ids)

        r = await self.invoke(
            raw.functions.stories.Report(
                user_id=await self.resolve_peer(user_id),
                id=stories_ids,
                message=message,
                reason=reason
            )
        )
        return types.Stories._parse(r)
