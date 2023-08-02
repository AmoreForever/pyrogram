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

import os
import re
from typing import Optional, List, Union, BinaryIO, Callable

import pyrogram
from pyrogram import StopTransmission, raw, enums
from pyrogram import types
from pyrogram import utils
from pyrogram.errors import FilePartMissing
from pyrogram.raw.types import InputPrivacyValueAllowAll


class EditStory:
    async def edit_story(
            self: "pyrogram.Client",
            story_id: int,
            media: Union[str, BinaryIO],
            caption: Optional[str] = None,
            parse_mode: Optional["enums.ParseMode"] = None,
            caption_entities: List["types.MessageEntity"] = None,
            duration: int = 0,
            width: int = 0,
            height: int = 0,
            thumb: Union[str, BinaryIO] = None,
            privacy_rules: List["raw.base.InputPrivacyRule"] = [InputPrivacyValueAllowAll()],
            progress: Callable = None,
            progress_args: tuple = ()
    ) -> "raw.base.Updates":
        """Edit Story

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            story_id (``int`` ``32-bit``):
                Unique identifier (int) for the target story.

            media (:obj:`InputMedia <pyrogram.raw.base.InputMedia>`):
                Support video and photo.

            caption (``str``, *optional*):
                Story caption, 0-1024 characters.

            parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
                By default, texts are parsed using both Markdown and HTML styles.
                You can combine both syntaxes together.

            caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
                List of special entities that appear in message text, which can be specified instead of *parse_mode*.

            duration (``int``, *optional*):
                Duration of sent video in seconds.

            width (``int``, *optional*):
                Video width.

            height (``int``, *optional*):
                Video height.

            thumb (``str`` | ``BinaryIO``, *optional*):
                Thumbnail of the video sent.
                The thumbnail should be in JPEG format and less than 200 KB in size.
                A thumbnail's width and height should not exceed 320 pixels.
                Thumbnails can't be reused and can be only uploaded as a new file.

            privacy_rules (:obj:`InputPrivacyRule <pyrogram.raw.base.InputPrivacyRule>`):
                Privacy rules.

            progress (``Callable``, *optional*):
                Pass a callback function to view the file transmission progress.
                The function must take *(current, total)* as positional arguments (look at Other Parameters below for a
                detailed description) and will be called back each time a new file chunk has been successfully
                transmitted.

            progress_args (``tuple``, *optional*):
                Extra custom arguments for the progress callback function.
                You can pass anything you need to be available in the progress callback scope; for example, a Message
                object or a Client instance in order to edit the message with the updated progress status.

        Other Parameters:
            current (``int``):
                The amount of bytes transmitted so far.

            total (``int``):
                The total size of the file.

            *args (``tuple``, *optional*):
                Extra custom arguments as defined in the ``progress_args`` parameter.
                You can either keep ``*args`` or add every single extra argument in your function signature.

        Returns:
            :obj:`Updates <pyrogram.raw.base.Updates>`

        Example:
            .. code-block:: python

            # Edit a story
            app.edit_story(
                media="video.mp4",
                caption="New caption!"
            )
        """

        message, entities = (await utils.parse_text_entities(self, caption, parse_mode, caption_entities).values())

        try:
            if isinstance(media, str):
                if os.path.isfile(media):
                    thumb = await self.save_file(thumb)
                    file = await self.save_file(media, progress=progress, progress_args=progress_args)
                    mime_type = self.guess_mime_type(file.name)
                    if mime_type == "video/mp4":
                        media = raw.types.InputMediaUploadedDocument(
                            mime_type=mime_type,
                            file=file,
                            thumb=thumb,
                            attributes=[
                                raw.types.DocumentAttributeVideo(
                                    duration=duration,
                                    w=width,
                                    h=height,
                                )
                            ]
                        )
                    else:
                        media = raw.types.InputMediaUploadedPhoto(
                            file=file,
                        )
                elif re.match("^https?://", media):
                    mime_type = self.guess_mime_type(media)
                    if mime_type == "video/mp4":
                        media = raw.types.InputMediaDocumentExternal(
                            url=media,
                        )
                    else:
                        media = raw.types.InputMediaPhotoExternal(
                            url=media,
                        )
                else:
                    media = utils.get_input_media_from_file_id(media)
            else:
                thumb = await self.save_file(thumb)
                file = await self.save_file(media, progress=progress, progress_args=progress_args)
                mime_type = self.guess_mime_type(file.name)
                if mime_type == "video/mp4":
                    media = raw.types.InputMediaUploadedDocument(
                        mime_type=mime_type,
                        file=file,
                        thumb=thumb,
                        attributes=[
                            raw.types.DocumentAttributeVideo(
                                duration=duration,
                                w=width,
                                h=height,
                            )
                        ]
                    )
                else:
                    media = raw.types.InputMediaUploadedPhoto(
                        file=file,
                    )

                while True:
                    try:
                        r = await self.invoke(
                            raw.functions.stories.EditStory(
                                id=story_id,
                                media=media,
                                caption=message,
                                entities=entities,
                                privacy_rules=privacy_rules,
                            )
                        )
                    except FilePartMissing as e:
                        await self.save_file(media, file_id=file.id, file_part=e.value)
                    else:
                        for i in r.updates:
                            if isinstance(i, (raw.types.UpdateShortSentMessage,
                                              raw.types.UpdateShort)):
                                return await types.UpdateStory._parse(
                                    i.id, i.media
                                )
        except StopTransmission:
            return None
