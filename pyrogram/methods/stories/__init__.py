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

from .delete_stories import DeleteStories
from .edit_story import EditStory
from .export_story_link import ExportStoryLink
from .get_all_read_user_stories import GetAllReadUserStories
from .get_all_stories import GetAllStories
from .get_pinned_stories import GetPinnedStories
from .get_stories_archive import GetStoriesArchive
from .get_stories_by_id import GetStoriesByID
from .get_story_views_list import GetStoryViewsList
from .get_stories_views import GetStoriesViews
from .get_user_stories import GetUserStories
from .increment_story_views import IncrementStoryViews
from .read_stories import ReadStories
from .report_stories import ReportStories
from .send_story import SendStory
from .toggle_all_stories_hidden import ToggleAllStoriesHidden
from .toggle_stories_pinned import ToggleStoriesPinned


class Stories(
    DeleteStories,
    EditStory,
    ExportStoryLink,
    GetAllReadUserStories,
    GetAllStories,
    GetPinnedStories,
    GetStoriesArchive,
    GetStoriesByID,
    GetStoryViewsList,
    GetStoriesViews,
    GetUserStories,
    IncrementStoryViews,
    ReadStories,
    ReportStories,
    SendStory,
    ToggleAllStoriesHidden,
    ToggleStoriesPinned
):
    pass
