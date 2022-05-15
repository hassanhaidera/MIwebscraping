from urllib.request import urlopen
import bs4 as bs
sudanbid_HTML=urlopen('https://www.sudanbid.com/')
sudanbidssoup=bs.BeautifulSoup(sudanbid_HTML,'html.parser').find_all('a','a_homelist')
for x in sudanbidsuop:
    print(x.get_text())