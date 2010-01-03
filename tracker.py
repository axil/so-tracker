import urllib2
import html5lib
from sys import exit
f = urllib2.urlopen('http://stackoverflow.com/questions/tagged?tagnames=git%20or%20django%20or%20python%20or%20vim%20or%20django-models%20or%20django-admin%20or%20django-templates%20or%20django-forms%20or%20django-urls%20or%20pythonic%20or%20python-3.x%20or%20gvim%20or%20regex%20or%20numpy&sort=newest')
parser = html5lib.HTMLParser(tree=html5lib.treebuilders.getTreeBuilder('beautifulsoup'))
soup = parser.parse(f)
div = soup.find('div', 'question-summary')
try:
    f=open('prev_id.txt', 'rt')
    old_id = f.readline().strip()
    f.close()
except:
    old_id = ''
open('prev_id.txt', 'wt').write(div['id'])
if div['id'] != old_id:
    exit('')

