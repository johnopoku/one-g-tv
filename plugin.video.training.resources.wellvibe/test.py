
import sys
import xbmcaddon
import xbmcgui
import xbmcplugin
from BeautifulSoup import BeautifulSoup, SoupStrainer
import xbmc
import urllib
import urllib2

USER_AGENT = "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko)" \
             " Version/4.0.5 Mobile/8A293 Safari/6531.22.7"
test_url = "https://qa.wellvibe.com/manual_scripts/plugin_script.php"
base_url = sys.argv[0]
addon_handler = int(sys.argv[1])
addon_base = xbmcaddon.Addon('plugin.video.training.resources.wellvibe')
title = addon_base.getAddonInfo('name')
icon = addon_base.getAddonInfo('icon')
xbmcplugin.setContent(addon_handler, 'video')
playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
playlist.clear()


def index():
    add_home_directory(title, test_url, 1, icon)


def build_directory(video_url):
    req = urllib2.Request(video_url)
    req.add_header('User-Agent', USER_AGENT)
    response = urllib2.urlopen(req)
    soup = BeautifulSoup(response.read())
    for a in soup.findAll('a', attrs={'class': 'test'}):
        movie_name = a['title']
        link = a['href'].replace(' ', '%20')
        if len(movie_name) > 0:
            add_directory(movie_name, link, 2, icon)


def add_home_directory(video_name, video_url, video_mode, image):
    u = base_url+"?url="+urllib.quote_plus(video_url.encode('utf-8', 'ignore'))+"&mode="+str(video_mode)+"&name="+urllib.quote_plus(video_name.encode('utf-8', 'ignore'))+"&iconimage="+str(image)
    ok = True
    li = xbmcgui.ListItem(video_name, iconImage=icon, thumbnailImage=icon)
    li.setProperty('IsPlayable', 'true')
    li.setInfo(type="Video", infoLabels={"Title": video_name})
    ok = xbmcplugin.addDirectoryItem(addon_handler, url=u, listitem=li, isFolder=True)
    return ok


def add_directory(video_name, video_url, video_mode, video_icon):
    u = video_url
    ok = True
    li = xbmcgui.ListItem(video_name, iconImage=icon, thumbnailImage=video_icon)
    li.setProperty('IsPlayable', 'true')
    li.setInfo(type="Video", infoLabels={"Title": video_name})
    playlist.add(url=u, listitem=li)
    ok = xbmcplugin.addDirectoryItem(addon_handler, url=u, listitem=li)
    return ok


def get_params():
        param = []
        paramstring = sys.argv[2]
        if len(paramstring) >= 2:
                params = sys.argv[2]
                cleanedparams = params.replace('?', '')
                if (params[len(params)-1]=='/'):
                        params = params[0:len(params)-2]
                pairsofparams = cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams = {}
                        splitparams = pairsofparams[i].split('=')
                        if (len(splitparams)) == 2:
                                param[splitparams[0]] = splitparams[1]

        return param


params = get_params()
image = None
url = None
name = None
mode = None

try:
        image = urllib.unquote_plus(params["image"])
except:
        pass
try:
        url = urllib.unquote_plus(params["url"])
except:
        pass
try:
        name = urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode = int(params["mode"])
except:
        pass

print("Mode: "+str(mode))
print("URL: "+str(url))
print("Name: "+str(name))
print("Image: "+str(image))

#main execution of menu navigation
if mode is None or url is None or len(url) < 1:
        print("")
        index()

elif mode == 1:
        print(""+url)
        build_directory(url)

customPlayer = xbmc.Player(xbmc.PLAYER_CORE_AUTO)
xbmc.executebuiltin('PlayerControl(RepeatAll)')
customPlayer.play(item=playlist)

xbmcplugin.endOfDirectory(addon_handler)




