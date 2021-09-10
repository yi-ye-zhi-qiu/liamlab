import scrapy

#Create opgg that inherits from base
#scrapy spider class.
class OPGG(scrapy.Spider):

    def __init__(self):
        '''Class constructor used to instantiate class attributes.
        '''
        pass;

    #Name of spider to call in 'scrapy crawl opgg'
    name = 'opgg'

    #If no start_requests f(x) and pagination handled in self.parse:
    #start_urls = ['https://na.op.gg/ranking/ladder/page=1']

    def start_requests(self):
        '''Feeds urls for leaderboards, pages=p
        (this is pagination)
        '''
        p = 2

        for i in range(1, p+1):
            url_str = f'https://na.op.gg/ranking/ladder/page={i}'
            request = scrapy.Request(url_str, callback=self.leaderboards)
            yield request

    def remove_tabnewline(self, s: 'str') -> 'str':
        '''Removes \t or \n from string'''
        s = s.replace('\n','')
        s = s.replace('\t','')
        return s

    def leaderboards(self, response):
        '''Function to start at leaderboards,
        read all users and urls to user pages,
        and send Scrapy requests per url.
        '''

        content = response.xpath('//div[@class="Content"]')

        h_un = content.xpath('//a[@class="ranking-highest__name"]')

        #Non highest-ranking users
        table = response.xpath('//table[contains(@class, "ranking-table")]//tbody')


        def chain_req(username: 'str', userlink: 'str') -> 'scrapy.Request':
            #userlink is un-necessarily prefixed by //
            url_str = 'https://' + userlink[2:]
            return scrapy.Request(url_str, callback=self.user, meta={'username': username})

        usernames = table.xpath('//td[contains(@class,"ranking-table__cell--summoner")]//span/text()').extract()
        userlinks = table.xpath('//td[contains(@class,"ranking-table__cell--summoner")]//a/@href').extract()
        userranks = table.xpath('//td[contains(@class,"ranking-table__cell--tier")]/text()').extract()
        userlps = table.xpath('//td[contains(@class,"ranking-table__cell--lp")]/text()').extract()

        for i, v in enumerate(usernames):

            username = self.remove_tabnewline(v)
            userlink = userlinks[i]
            userlink = self.remove_tabnewline(userlink)
            userrank = userranks[i]
            userrank = self.remove_tabnewline(userrank)
            userlp = userlps[i]
            userlp = self.remove_tabnewline(userlp)

            s = f'User {username} ({userlink}) is {userrank} LP: {userlp}'

            print(s)

            request = chain_req(username=username, userlink=userlink)
            yield request

    def user(self, response):
        '''Takes response object from start_requests and
        parses HTML for recent games and information therein'''

        username = response.meta['username']

        games = response.xpath('//div[@class="GameItemList"]')
        champs = response.xpath('//div[@class="GameItemList"]//div[@class="ChampionName"]/a/text()').extract()
        results = response.xpath('//div[@class="GameResult"]/text()').extract()

        print(f'For user: {username}')

        for i in range(len(champs)):

            champ = self.remove_tabnewline(champs[i])
            result = self.remove_tabnewline(results[i])

            print(f'{champ} {result}')

            d = {'champ': champ, 'result': result}
