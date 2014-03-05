import sys
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin

handler_for_addon = int(sys.argv[1])
addon = xbmcaddon.Addon('plugin.video.wellvibe.training.resource')
name = addon.getAddonInfo('name')
icon = addon.getAddonInfo('icon')
xbmcplugin.setContent(handler_for_addon, 'video')
playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
playlist.clear()

link = 'http://www.studiomb.tv/video/studiomb/wellvibe/Add_A_News_Article.mp4'
li = xbmcgui.ListItem(label='Add A News Article', iconImage=icon, thumbnailImage=icon, path=link)
li.setInfo(type='Video', infoLabels={"Title": 'Add A News Article'})
li.setProperty('IsPlayable', 'true')
playlist.add(url=link, listitem=li)
xbmcplugin.addDirectoryItem(handle=handler_for_addon, url=link, listitem=li)

link1 = 'http://www.studiomb.tv/video/studiomb/wellvibe/AddEditDeleteEmployee.mp4'
li = xbmcgui.ListItem(label='Add/Edit/Delete Employee', iconImage=icon, thumbnailImage=icon, path=link1)
li.setInfo(type='Video', infoLabels={"Title": 'Add/Edit/Delete Employee'})
li.setProperty('IsPlayable', 'true')
playlist.add(url=link1, listitem=li)
xbmcplugin.addDirectoryItem(handle=handler_for_addon, url=link1, listitem=li)

link2 = 'http://www.studiomb.tv/video/studiomb/wellvibe/Add%20a%20Track%20with%20Default%20Scan%20Form.mp4'
li = xbmcgui.ListItem(label='Add a Track with Default Scan Form', iconImage=icon, thumbnailImage=icon, path=link2)
li.setInfo(type='Video', infoLabels={"Title": 'Add a Track with Default Scan Form'})
li.setProperty('IsPlayable', 'true')
playlist.add(url=link2, listitem=li)
xbmcplugin.addDirectoryItem(handle=handler_for_addon, url=link2, listitem=li)

link3 = 'http://www.studiomb.tv/video/studiomb/wellvibe/Add_an_Event.mp4'
li = xbmcgui.ListItem(label="Add an Event", iconImage=icon, thumbnailImage=icon, path=link3)
li.setInfo(type='Video', infoLabels={"Title": "Add an Event"})
li.setProperty('IsPlayable', 'true')
playlist.add(url=link3, listitem=li)
xbmcplugin.addDirectoryItem(handle=handler_for_addon, url=link3, listitem=li)

link4 = 'http://www.studiomb.tv/video/studiomb/wellvibe/RunReports.mp4'
li = xbmcgui.ListItem(label="Run Reports", iconImage=icon, thumbnailImage=icon, path=link4)
li.setInfo(type='Video', infoLabels={"Title": "Run Reports"})
li.setProperty('IsPlayable', 'true')
playlist.add(url=link4, listitem=li)
xbmcplugin.addDirectoryItem(handle=handler_for_addon, url=link4, listitem=li)

link5 = 'http://www.studiomb.tv/video/studiomb/wellvibe/Additional%20Resources.mp4'
li = xbmcgui.ListItem(label="Additional Resources", iconImage=icon, thumbnailImage=icon, path=link5)
li.setInfo(type='Video', infoLabels={"Title": "Additional Resources"})
li.setProperty('IsPlayable', 'true')
playlist.add(url=link5, listitem=li)
xbmcplugin.addDirectoryItem(handle=handler_for_addon, url=link5, listitem=li)

li = xbmcgui.ListItem(label='WellVibe Training Resources', iconImage=icon, thumbnailImage=icon)
xbmc.Player(xbmc.PLAYER_CORE_MPLAYER).play(item=playlist, listitem=li)

xbmcplugin.endOfDirectory(handler_for_addon)



