import sys
import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon

addon_handler = int(sys.argv[1])
addon = xbmcaddon.Addon('plugin.video.tester.joynews')
title = addon.getAddonInfo('name')
icon = addon.getAddonInfo('icon')

link = 'http://erp.dubtel.tv/XBMC/audio1.mp4'
xbmcplugin.setContent(addon_handler, 'video')

playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
playlist.clear()
playlist.add(link)
li = xbmcgui.ListItem(label=title, iconImage=icon, thumbnailImage=icon, path=link)
li.setInfo(type='Video', infoLabels={"Title": title})
li.setProperty('IsPlayable', 'true')
xbmcplugin.setResolvedUrl(addon_handler, True, li)
xbmc.Player(xbmc.PLAYER_CORE_MPLAYER).play(item=playlist, listitem=li)
