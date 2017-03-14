# -*- coding: utf-8 -*-
"""
     
    Copyright (C) 2016 Twitch-on-Kodi
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

from common import kodi
from common.url_dispatcher import URL_Dispatcher
from twitch import scopes


def __enum(**enums):
    return type('Enum', (), enums)


DISPATCHER = URL_Dispatcher()

ADDON_DATA_DIR = kodi.translate_path('special://profile/addon_data/{0!s}/'.format(kodi.get_id()))

MODES = __enum(
    MAIN='main',
    FEATUREDSTREAMS='featured_streams',
    GAMES='games',
    CHANNELS='channels',
    FOLLOWING='following',
    SEARCH='search',
    NEWSEARCH='new_search',
    SEARCHRESULTS='search_results',
    SETTINGS='settings',
    FOLLOWED='followed',
    CHANNELVIDEOS='channel_videos',
    CHANNELVIDEOLIST='channel_video_list',
    GAMESTREAMS='game_streams',
    RESETCACHE='reset_cache',
    CLEARLIVEPREVIEWS='clear_live_previews',
    INSTALLIRCCHAT='install_ircchat',
    PLAY='play',
    TOKENURL='get_token_url'
)

LINE_LENGTH = 60

ICON = kodi.get_icon()
FANART = kodi.get_fanart()

CLIENT_ID = 'NjdlYnBmaHlvaWNhYjVrcjB5N3B6b2NzZm9oczd0eQ=='

LIVE_PREVIEW_TEMPLATE = '%://static-cdn.jtvnw.net/previews-ttv/live_user_%-%___x%___.jpg'  # sqlite LIKE pattern


class Images:
    ICON = ICON
    THUMB = ICON
    POSTER = ICON
    FANART = FANART
    BANNER = ''
    CLEARART = ''
    CLEARLOGO = ''
    LANDSCAPE = ''
    #
    VIDEOTHUMB = 'http://static-cdn.jtvnw.net/ttv-static/404_preview-320x180.jpg'
    BOXART = 'http://static-cdn.jtvnw.net/ttv-static/404_boxart.jpg'


class Keys:
    BITRATE = 'bitrate'
    CHANNEL = 'channel'
    CHANNELS = 'channels'
    CONNECT = 'connect'
    BACKGROUND = 'background'
    DISPLAY_NAME = 'display_name'
    FEATURED = 'featured'
    FOLLOWS = 'follows'
    GAME = 'game'
    LOGO = 'logo'
    BOX = 'box'
    LARGE = 'large'
    MEDIUM = 'medium'
    NAME = 'name'
    NEEDED_INFO = 'needed_info'
    PLAY = 'play'
    PLAYPATH = 'playpath'
    QUALITY = 'quality'
    RTMP = 'rtmp'
    STREAMS = 'streams'
    RTMP_URL = 'rtmpUrl'
    STATUS = 'status'
    STREAM = 'stream'
    SWF_URL = 'swfUrl'
    TEAMS = 'teams'
    TOKEN = 'token'
    TOP = 'top'
    TOTAL = '_total'
    VIDEOS = 'videos'
    VIDEO_BANNER = 'video_banner'
    PROFILE_BANNER = 'profile_banner'
    VIDEO_HEIGHT = 'video_height'
    VIEWERS = 'viewers'
    CURRENT_VIEWERS = 'current_viewers'
    PREVIEW = 'preview'
    TITLE = 'title'
    LENGTH = 'length'
    META_GAME = 'meta_game'
    URL = 'url'
    CHUNKS = 'chunks'
    SIG = 'sig'
    LIVE = 'live'
    OTHERS = 'others'
    IMAGE = 'image'
    SIZE600 = 'size600'
    VIEWS = 'views'
    MATURE = 'mature'
    PARTNER = 'partner'
    DELAY = 'delay'
    BROADCASTER_LANGUAGE = 'broadcaster_language'
    DESCRIPTION = 'description'
    CREATED_AT = 'created_at'
    GAMES = 'games'
    ID = '_id'


SCOPES = [scopes.user_read, scopes.user_blocks_edit, scopes.user_blocks_read, scopes.user_follows_edit, scopes.user_subscriptions,
          scopes.channel_feed_edit, scopes.channel_feed_read, scopes.chat_login]
