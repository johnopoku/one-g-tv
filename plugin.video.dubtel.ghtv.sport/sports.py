import sys
import xbmcaddon
import xbmcgui
import xbmcplugin

handler_for_addon = int(sys.argv[1])
addon = xbmcaddon.Addon('plugin.video.dubtel.ghtv.sport')
name = addon.getAddonInfo('name')
icon = addon.getAddonInfo('icon')
xbmcplugin.setContent(handler_for_addon, 'video')

link = 'http://erp.dubtel.tv/XBMC/boxing.mp4'
li = xbmcgui.ListItem(label='Ghana Street Boxing', iconImage=icon, thumbnailImage=icon, path=link)
li.setInfo(type='Video', infoLabels={"Title": 'Ghana Street Boxing'})
li.setProperty('IsPlayable', 'true')
xbmcplugin.addDirectoryItem(handle=handler_for_addon, url=link, listitem=li)

link1 = 'http://erp.dubtel.tv/XBMC/gha-ept.mp4'
li = xbmcgui.ListItem(label='Highlights of Ghana vs Egypt - World Cup Qualifiers', iconImage=icon, thumbnailImage=icon, path=link1)
li.setInfo(type='Video', infoLabels={"Title": 'Highlights of Ghana vs Egypt - World Cup Qualifiers'})
li.setProperty('IsPlayable', 'true')
xbmcplugin.addDirectoryItem(handle=handler_for_addon, url=link1, listitem=li)

link2 = 'http://erp.dubtel.tv/XBMC/chel-man.mp4'
li = xbmcgui.ListItem(label='English Premier League - Chelsea vs Man. United', iconImage=icon, thumbnailImage=icon, path=link2)
li.setInfo(type='Video', infoLabels={"Title": 'English Premier League - Chelsea vs Man. United'})
li.setProperty('IsPlayable', 'true')
xbmcplugin.addDirectoryItem(handle=handler_for_addon, url=link2, listitem=li)

link3 = 'http://erp.dubtel.tv/XBMC/strongest.mp4'
li = xbmcgui.ListItem(label="TV3 Ghana's Strongest winner storms Kumasi", iconImage=icon, thumbnailImage=icon, path=link3)
li.setInfo(type='Video', infoLabels={"Title": "TV3 Ghana's Strongest winner storms Kumasi"})
li.setProperty('IsPlayable', 'true')
xbmcplugin.addDirectoryItem(handle=handler_for_addon, url=link3, listitem=li)

xbmcplugin.endOfDirectory(handler_for_addon)
