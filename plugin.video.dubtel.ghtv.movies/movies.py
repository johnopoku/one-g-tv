import sys
import xbmcaddon
import xbmcgui
import xbmcplugin

handler_for_addon = int(sys.argv[1])
addon = xbmcaddon.Addon('plugin.video.dubtel.ghtv.movies')
name = addon.getAddonInfo('name')
icon = addon.getAddonInfo('icon')
xbmcplugin.setContent(handler_for_addon, 'video')

link = 'http://erp.dubtel.tv/XBMC/Bed-Mate1.mp4'
li = xbmcgui.ListItem(label='Ghanaian Movie: Bed Mate Part 1', iconImage=icon, thumbnailImage=icon, path=link)
li.setInfo(type='Video', infoLabels={"Title": 'Ghanaian Movie: Bed Mate Part 1'})
li.setProperty('IsPlayable', 'true')
xbmcplugin.addDirectoryItem(handle=handler_for_addon, url=link, listitem=li)

link1 = 'http://erp.dubtel.tv/XBMC/Bed-Mate2.mp4'
li = xbmcgui.ListItem(label="Ghanaian Movie: Bed Mate Part 2", iconImage=icon, thumbnailImage=icon, path=link1)
li.setInfo(type='Video', infoLabels={"Title": "Ghanaian Movie: Bed Mate Part 2"})
li.setProperty('IsPlayable', 'true')
xbmcplugin.addDirectoryItem(handle=handler_for_addon, url=link1, listitem=li)

link2 = 'http://erp.dubtel.tv/XBMC/bachelor.mp4'
li = xbmcgui.ListItem(label="Ghanaian Movie: Bachelors-Trailer", iconImage=icon, thumbnailImage=icon, path=link2)
li.setInfo(type='Video', infoLabels={"Title": "Ghanaian Movie: Bachelors-Trailer"})
li.setProperty('IsPlayable', 'true')
xbmcplugin.addDirectoryItem(handle=handler_for_addon, url=link2, listitem=li)

link3 = 'http://erp.dubtel.tv/XBMC/sika.mp4'
li = xbmcgui.ListItem(label="Ghanaian Movie: Sika Mpe Rough Part 1", iconImage=icon, thumbnailImage=icon, path=link3)
li.setInfo(type='Video', infoLabels={"Title": "Ghanaian Movie: Sika Mpe Rough Part 1"})
li.setProperty('IsPlayable', 'true')
xbmcplugin.addDirectoryItem(handle=handler_for_addon, url=link3, listitem=li)

xbmcplugin.endOfDirectory(handler_for_addon)



