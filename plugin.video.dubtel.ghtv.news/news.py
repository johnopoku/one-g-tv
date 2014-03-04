import sys
import xbmcaddon
import xbmcgui
import xbmcplugin

handler_for_addon = int(sys.argv[1])
addon = xbmcaddon.Addon('plugin.video.dubtel.ghtv.news')
name = addon.getAddonInfo('name')
icon = addon.getAddonInfo('icon')
xbmcplugin.setContent(handler_for_addon, 'video')

link = 'http://erp.dubtel.tv/XBMC/audio1.mp4'
li = xbmcgui.ListItem(label='Accommodation in Ghana', iconImage=icon, thumbnailImage=icon, path=link)
li.setInfo(type='Video', infoLabels={"Title": 'Accommodation in Ghana'})
li.setProperty('IsPlayable', 'true')
xbmcplugin.addDirectoryItem(handle=handler_for_addon, url=link, listitem=li)

link1 = 'http://erp.dubtel.tv/XBMC/primetime.mp4'
li = xbmcgui.ListItem(label='JOY Primetime News', iconImage=icon, thumbnailImage=icon, path=link1)
li.setInfo(type='Video', infoLabels={"Title": 'JOY Primetime News'})
li.setProperty('IsPlayable', 'true')
xbmcplugin.addDirectoryItem(handle=handler_for_addon, url=link1, listitem=li)

link2 = 'http://erp.dubtel.tv/XBMC/emelia.mp4'
li = xbmcgui.ListItem(label='Actress Emelia Brobbey arrives in Ghana and speak after shoplifting scandal', iconImage=icon, thumbnailImage=icon, path=link2)
li.setInfo(type='Video', infoLabels={"Title": 'Actress Emelia Brobbey arrives in Ghana and speak after shoplifting scandal'})
li.setProperty('IsPlayable', 'true')
xbmcplugin.addDirectoryItem(handle=handler_for_addon, url=link2, listitem=li)

link3 = 'http://erp.dubtel.tv/XBMC/todaynews.mp4'
li = xbmcgui.ListItem(label="Today News on Joy", iconImage=icon, thumbnailImage=icon, path=link3)
li.setInfo(type='Video', infoLabels={"Title": "Today News on Joy"})
li.setProperty('IsPlayable', 'true')
xbmcplugin.addDirectoryItem(handle=handler_for_addon, url=link3, listitem=li)

xbmcplugin.endOfDirectory(handler_for_addon)



