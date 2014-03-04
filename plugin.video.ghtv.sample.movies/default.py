import sys
import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon

addon_handler = int(sys.argv[1])
addon = xbmcaddon.Addon('plugin.video.ghtv.sample.movies')
title = addon.getAddonInfo('name')
icon = addon.getAddonInfo('icon')
xbmcplugin.setContent(addon_handler, 'video')
playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
playlist.clear()
playlist.add('http://erp.dubtel.tv/XBMC/Bed-Mate1.mp4')
playlist.add('http://erp.dubtel.tv/XBMC/Bed-Mate2.mp4')
li = xbmcgui.ListItem(label=title, iconImage=icon, thumbnailImage=icon)
li.setInfo(type='Video', infoLabels={"Title": title})
li.setProperty('IsPlayable', 'true')
xbmcplugin.setResolvedUrl(addon_handler, True, li)
xbmc.Player(xbmc.PLAYER_CORE_MPLAYER).play(item=playlist, listitem=li)
