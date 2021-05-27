import scrapy


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['www.bhhsamb.com/agents']
    start_urls = ['http://www.bhhsamb.com/agents/']
    base_url = 'http://www.bhhsamb.com/agents/'

    
    def parse(self, response):
        all_agents = response.xpath('//div[@class="agent-cell-container background-3"]')

        for agent in all_agents:
            image_url = self.start_urls[0] + agent.xpath('.//a/@href/img/@src').extract_first()
            yield scrapy.Request(image_url, callback=self.parse_agent)

        next_page_partial_url = response.xpath('//li[@class="next"]/a/@href')
        next_page_url = self.base_url + next_page_partial_url

        yield scrapy.Request(next_page_url, callback=self.parse)

        
    def parse_agent(self, response):
        name = agent.xpath('.//span[@class="agent-name"]/a/@href/text()').extract_first()
        job_title = agent.xpath('.//span[@class="agent-title"]/text()').extract_first()
        image_url = self.start_urls[0] + agent.xpath('.//a/@href/img/@src').extract_first()
        address = agent.xpath('.//div/@class/text()').extract_first()
        contact_details = agent.xpath('.//span/@class/text()/a/@href/text()').extract_first()
        social_accounts = agent.xpath('.//div[@class="agent-social-icons social"]/a/@href').extract_first()
        offices = agent.xpath('.//h2/text()/a/@href/text()').extract_first()
        languages = agent.xpath('.//h2/text()/ul/li/text()').extract_first()
        description = agent.xpath('.//div/@class/following-sibling::p/text()').extract_first()
            
        yield {
            'name' : name,
            'job_title' : job_title,
            'image_url' : image_url,
            'address' : address,
            'contact_details' : contact_details,
            'social_accounts' : social_accounts,
            'offices': offices,
            'languages' : languages,
            'description' : description,
            }

