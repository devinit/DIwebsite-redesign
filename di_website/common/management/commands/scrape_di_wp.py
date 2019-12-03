import os
import json
import requests
from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    """Management command that scrapes Wordpress content"""

    help = 'Scrape types of Wordpress content'

    def handle(self, *args, **options):
        """Implement the command handler."""

        old_keep = [
            # Blogs
            "di-analyst-viewpoint-ian-townsend-ending-poverty",
            "economic-growth-wont-enough-help-ugandas-poorest",
            "future-oda-targeting-people-countries-end-poverty-2030",
            "humanitarian-accountability-report-2013-how-far-have-we-come",
            "humanitarian-aid-in-conflict-more-money-more-problems",
            "humanitarian-aid-in-the-dac-context",
            "non-dac-donors-and-the-transparency-of-aid-information",
            "response-typhoon-haiyan-comparison",
            "role-private-sector-financing-post-2015-agenda-sustainable-development",
            "thailands-worst-floods-in-50-years-international-response-and-preparing-for-future-disasters",
            "the-international-red-cross-and-red-crescent-movement-the-full-financial-picture",
            "the-united-arab-emirates-reports-to-the-dac-one-step-closer-to-better-aid-information",
            "top-100-best-ngos-ranking-by-the-global-journal",
            "understanding-role-zakat-humanitarian-response",
            # News
            "together-can-end-poverty-progress-priorities-changing-world",
            "international-resources",
            "domestic-public-resources",
            "afghanistan-beyond-2014-aid-transformation-decade",
            "data-manifesto-2",
            "gha-report-2014",
            "ngo-resources-development",
            "kenya-case-study-global-partnership-effective-development-cooperation-2",
            "humanitarian-assistance-non-state-donors",
            "global-aid-trends-need-know",
            "using-data-get-better-results-poverty-eradication-need-know",
            "using-resources-available-end-poverty",
            "investments-to-end-poverty",
            "post-oda",
            "0-7-aid-target-2",
            "counting-the-cost-of-humanitarian-aid-delivered-through-the-military",
            "private-funding-for-humanitarian-assistance",
            "gha-report-2013",
            "south-sudan-resources-for-poverty-eradication",
            "official-development-assistance-essential-guide",
            "kenya-resources-for-poverty-eradication",
            "gha-report-2012",
            "private-funding-an-emerging-trend-in-humanitarian-donorship-2",
            "disaster-risk-reduction-spending-where-it-should-count",
            "arab-donors",
            "gha-report-2011",
            "non-dac-donors-and-humanitarian-aid",
            "kenya-red-cross-resource-flows-and-the-humanitarian-contribution",
            "gha-report-2010",
            # Pubs
            "together-can-end-poverty-progress-priorities-changing-world",
            "international-resources",
            "domestic-public-resources",
            "afghanistan-beyond-2014-aid-transformation-decade",
            "data-manifesto-2",
            "gha-report-2014",
            "ngo-resources-development",
            "kenya-case-study-global-partnership-effective-development-cooperation-2",
            "humanitarian-assistance-non-state-donors",
            "global-aid-trends-need-know",
            "using-data-get-better-results-poverty-eradication-need-know",
            "using-resources-available-end-poverty",
            "investments-to-end-poverty",
            "post-oda",
            "0-7-aid-target-2",
            "counting-the-cost-of-humanitarian-aid-delivered-through-the-military",
            "private-funding-for-humanitarian-assistance",
            "gha-report-2013",
            "south-sudan-resources-for-poverty-eradication",
            "official-development-assistance-essential-guide",
            "kenya-resources-for-poverty-eradication",
            "gha-report-2012",
            "private-funding-an-emerging-trend-in-humanitarian-donorship-2",
            "disaster-risk-reduction-spending-where-it-should-count",
            "arab-donors",
            "gha-report-2011",
            "non-dac-donors-and-humanitarian-aid",
            "kenya-red-cross-resource-flows-and-the-humanitarian-contribution",
            "gha-report-2010",
        ]

        first_blog_page = "http://devinit.org/api/posts/di_format=data-blog,commentary,innovation/"
        blogs = json.loads(requests.get(first_blog_page).content)
        blog_count = len(blogs)
        all_blogs = blogs.copy()

        while len(blogs) > 0:
            print(blog_count)
            page_url = "http://devinit.org/api/posts/offset={}&di_format=data-blog,commentary,innovation/".format(blog_count)
            blogs = json.loads(requests.get(page_url).content)
            blog_count += len(blogs)
            all_blogs += [post for post in blogs if int(post["date"][-4:]) >= 2015 or post["slug"] in old_keep]

        for i in range(0, len(all_blogs)):
            print(i)
            blog = all_blogs[i]
            blog_url = "http://devinit.org/post/{}/".format(blog["slug"])
            blog_response = requests.get(blog_url)
            soup = BeautifulSoup(blog_response.content, "html.parser")
            meta_elem = soup.findAll(attrs={"name": "description"})
            if len(meta_elem) == 0:
                meta_text = ""
            elif len(meta_elem) == 1:
                meta_text = meta_elem[0]['content']
            else:
                meta_text = meta_elem[1]['content']
            all_blogs[i]["meta_description"] = meta_text

            author_elems = soup.findAll("h3", {"class": "h5 m-t--0"})
            if author_elems:
                all_blogs[i]["authors"] = [auth_elem.text for auth_elem in author_elems]
            else:
                all_blogs[i]["authors"] = []

            body = soup.findAll("div", {"class": "col-md-8"})[1]
            if body:
                all_blogs[i]["body"] = "".join([str(con) for con in body.contents if con != "\n"][2:])
            else:
                all_blogs[i]["body"] = ""

            title = soup.find("h2", {"class", "h2 m-t--05 m-b--05"})
            all_blogs[i]["full_title"] = title.text

        parsed_content = [
            {
                "title": elem["full_title"],
                "author": elem["authors"],
                "format": "; ".join([form["name"] for form in elem["di_format"]]),
                "date": elem["date"],
                "description": elem["meta_description"],
                "url": "http://devinit.org/post/{}/".format(elem["slug"]),
                "body": elem["body"]
            } for elem in all_blogs
        ]
        with open(os.path.join(settings.BASE_DIR, 'migrated_content/di_blogs.json'), 'w') as outfile:
            json.dump(parsed_content, outfile)

        first_news_page = "http://devinit.org/api/posts/di_format=news/"
        news = json.loads(requests.get(first_news_page).content)
        news_count = len(news)
        all_news = news.copy()

        while len(news) > 0:
            print(news_count)
            page_url = "http://devinit.org/api/posts/offset={}&di_format=news/".format(news_count)
            news = json.loads(requests.get(page_url).content)
            news_count += len(news)
            all_news += [post for post in news if int(post["date"][-4:]) >= 2015 or post["slug"] in old_keep]

        for i in range(0, len(all_news)):
            print(i)
            news_page = all_news[i]
            news_page_url = "http://devinit.org/post/{}/".format(news_page["slug"])
            news_page_response = requests.get(news_page_url)
            soup = BeautifulSoup(news_page_response.content, "html.parser")
            meta_elem = soup.findAll(attrs={"name": "description"})
            if len(meta_elem) == 0:
                meta_text = ""
            elif len(meta_elem) == 1:
                meta_text = meta_elem[0]['content']
            else:
                meta_text = meta_elem[1]['content']
            all_news[i]["meta_description"] = meta_text

            author_elems = soup.findAll("h3", {"class": "h5 m-t--0"})
            if author_elems:
                all_news[i]["authors"] = [auth_elem.text for auth_elem in author_elems]
            else:
                all_news[i]["authors"] = []

            body = soup.findAll("div", {"class": "col-md-8"})[1]
            if body:
                all_news[i]["body"] = "".join([str(con) for con in body.contents if con != "\n"][2:])
            else:
                all_news[i]["body"] = ""

            title = soup.find("h2", {"class", "h2 m-t--05 m-b--05"})
            all_news[i]["full_title"] = title.text

        parsed_content = [
            {
                "title": elem["full_title"],
                "author": elem["authors"],
                "format": "; ".join([form["name"] for form in elem["di_format"]]),
                "date": elem["date"],
                "description": elem["meta_description"],
                "url": "http://devinit.org/post/{}/".format(elem["slug"]),
                "body": elem["body"]
            } for elem in all_news
        ]
        with open(os.path.join(settings.BASE_DIR, 'migrated_content/di_news.json'), 'w') as outfile:
            json.dump(parsed_content, outfile)

        pub_errs = []
        first_pub_page = "http://devinit.org/api/posts/di_format=report,briefing,factsheet,case-study,discussion-paper,background-paper,publication,crisis-briefing/"
        pubs = json.loads(requests.get(first_pub_page).content)
        pub_count = len(pubs)
        all_pubs = pubs.copy()

        while len(pubs) > 0:
            print(pub_count)
            page_url = "http://devinit.org/api/posts/offset={}&di_format=report,briefing,factsheet,case-study,discussion-paper,background-paper,publication,crisis-briefing/".format(pub_count)
            pubs = json.loads(requests.get(page_url).content)
            pub_count += len(pubs)
            all_pubs += [post for post in pubs if int(post["date"][-4:]) >= 2015 or post["slug"] in old_keep]

        for i in range(0, len(all_pubs)):
            print(i)
            pub = all_pubs[i]
            pub_url = "http://devinit.org/post/{}/".format(pub["slug"])
            pub_response = requests.get(pub_url)
            soup = BeautifulSoup(pub_response.content, "html.parser")
            meta_elem = soup.findAll(attrs={"name": "description"})
            if len(meta_elem) == 0:
                meta_text = ""
            elif len(meta_elem) == 1:
                meta_text = meta_elem[0]['content']
            else:
                meta_text = meta_elem[1]['content']
            all_pubs[i]["meta_description"] = meta_text

            author_elems = soup.findAll("h3", {"class": "h5 m-t--0"})
            if author_elems:
                all_pubs[i]["authors"] = [auth_elem.text for auth_elem in author_elems]
            else:
                all_pubs[i]["authors"] = []

            try:
                body = soup.findAll("div", {"class": "col-md-8"})[1]
                title = soup.findAll("h2", {"class", "h2 m-t--05 m-b--05"})[0].text
            except IndexError:
                pub_errs.append(pub_url)
                body = None
                title = None
            if body:
                all_pubs[i]["body"] = "".join([str(con) for con in body.contents if con != "\n"][2:])
            else:
                all_pubs[i]["body"] = ""

            all_pubs[i]["full_title"] = title

        parsed_content = [
            {
                "title": elem["full_title"],
                "authors": elem["authors"],
                "format": "; ".join([form["name"] for form in elem["di_format"]]),
                "date": elem["date"],
                "description": elem["meta_description"],
                "url": "http://devinit.org/post/{}/".format(elem["slug"]),
                "body": elem["body"]
            } for elem in all_pubs
        ]
        with open(os.path.join(settings.BASE_DIR, 'migrated_content/di_pubs.json'), 'w') as outfile:
            json.dump(parsed_content, outfile)

        for pub_err in pub_errs:
            print(pub_err)

        staff_index_url = "http://devinit.org/about/meet-the-team/"
        staff_index_response = requests.get(staff_index_url)
        soup = BeautifulSoup(staff_index_response.content, "html.parser")
        staff_cards = soup.findAll("a", attrs={"class": "col-xs-6 col-sm-3 col-md-3 card person-card"})
        staff_dataset = []
        for card in staff_cards:
            staff_url = "http://devinit.org{}/".format(card["href"])
            staff_name = card.find("h4").text
            print(staff_name)
            staff_position = card.find("p").text
            staff_department = card["type"]
            try:
                staff_img = card.find("img")["src"]
            except TypeError:
                staff_img = ""
            staff_response = requests.get(staff_url)
            sub_soup = BeautifulSoup(staff_response.content, "html.parser")
            staff_body = "".join([str(con) for con in sub_soup.find("div", attrs={"class": "body-text"}).contents if con != "\n"])
            staff_dat = {
                "url": staff_url,
                "name": staff_name,
                "position": staff_position,
                "department": staff_department,
                "img": staff_img,
                "body": staff_body
            }
            staff_dataset.append(staff_dat)
        with open(os.path.join(settings.BASE_DIR, 'migrated_content/di_staff.json'), 'w') as outfile:
            json.dump(staff_dataset, outfile)

        first_event_page = "http://devinit.org/api/posts/di_format=event/"
        events = json.loads(requests.get(first_event_page).content)
        event_count = len(events)
        all_events = events.copy()

        while len(events) > 0:
            print(event_count)
            page_url = "http://devinit.org/api/posts/offset={}&di_format=event/".format(event_count)
            events = json.loads(requests.get(page_url).content)
            event_count += len(events)
            all_events += [post for post in events if int(post["date"][-4:]) >= 2015]

        for i in range(0, len(all_events)):
            print(i)
            event = all_events[i]
            event_url = "http://devinit.org/post/{}/".format(event["slug"])
            event_response = requests.get(event_url)
            soup = BeautifulSoup(event_response.content, "html.parser")
            meta_elem = soup.findAll(attrs={"name": "description"})
            if len(meta_elem) == 0:
                meta_text = ""
            elif len(meta_elem) == 1:
                meta_text = meta_elem[0]['content']
            else:
                meta_text = meta_elem[1]['content']
            all_events[i]["meta_description"] = meta_text

            body = soup.find("div", {"class": "body-text"})
            if body:
                all_events[i]["body"] = "".join([str(con) for con in body.contents if con != "\n"][2:])
            else:
                all_events[i]["body"] = ""

            title = soup.find("h2", {"class", "h2 m-t--05 m-b--05"})
            all_events[i]["full_title"] = title.text

        parsed_content = [
            {
                "title": elem["full_title"],
                "date": elem["date"],
                "format": "; ".join([form["name"] for form in elem["di_format"]]),
                "description": elem["meta_description"],
                "url": "http://devinit.org/post/{}/".format(elem["slug"]),
                "body": elem["body"]
            } for elem in all_events
        ]
        with open(os.path.join(settings.BASE_DIR, 'migrated_content/di_events.json'), 'w') as outfile:
            json.dump(parsed_content, outfile)
