import client
import json
import time

from collections import defaultdict 


class keywordsAPI:
    def __init__(self, sandbox):

        self.api = client.API(sandbox=sandbox)
    def Volume_History(self, keyword, location_code, language_code):
        
        kwargs =  {
            "keywords": [keyword],
            "location_code": location_code,
            "language_code": language_code,
            }
        
        historical_search_volume_response, cost = self.api.call('dataforseo_labs/google/historical_search_volume/live', kwargs, method="post")
         
        mainObject = historical_search_volume_response["tasks"][0]["result"][0]["items"][0]
        search_queerie_info = {
            "Keyword": mainObject["keyword"],
            "Language Code": mainObject["language_code"],
            "Location Code": mainObject["location_code"]
            }        
        monthly_searches = mainObject["keyword_info"]["monthly_searches"]
        keyword_info = {
            "Competition": {
                "Competition": mainObject["keyword_info"]["competition"],
                "competition_level": mainObject["keyword_info"]["competition_level"],
                "keyword_difficulty": mainObject["keyword_properties"]["keyword_difficulty"],
            },
            "Information": {
                "cpc": mainObject["keyword_info"]["cpc"],
                "search_volume": mainObject["keyword_info"]["search_volume"],
                "low_top_of_page_bid": mainObject["keyword_info"]["low_top_of_page_bid"],
                "high_top_of_page_bid": mainObject["keyword_info"]["high_top_of_page_bid"],

            },
            "Categories": {
                "categories": mainObject["keyword_info"]["categories"],
            },
            "impression_info": {
                "Ad Position": {
                    "Min": mainObject["impressions_info"]["ad_position_min"],
                    "Average": mainObject["impressions_info"]["ad_position_average"],
                    "Max": mainObject["impressions_info"]["ad_position_max"]
                },
                "CPC": {
                    "Min": mainObject["impressions_info"]["cpc_min"],
                    "Average": mainObject["impressions_info"]["cpc_average"],
                    "Max": mainObject["impressions_info"]["cpc_max"]
                },     
                "Daily Impressions": {
                    "Min": mainObject["impressions_info"]["daily_impressions_min"],
                    "Average": mainObject["impressions_info"]["daily_impressions_average"],
                    "Max": mainObject["impressions_info"]["daily_impressions_max"]
                },       
                "Daily Clicks": {
                    "Min": mainObject["impressions_info"]["daily_clicks_min"],
                    "Average": mainObject["impressions_info"]["daily_clicks_average"],
                    "Max": mainObject["impressions_info"]["daily_clicks_max"]
                },         
                "Daily Cost": {
                    "Min": mainObject["impressions_info"]["daily_cost_min"],
                    "Average": mainObject["impressions_info"]["daily_cost_average"],
                    "Max": mainObject["impressions_info"]["daily_cost_max"]
                },                                                      

            }
            
        }
    
        ret = {
            "cost": cost,
            "search queerie info": search_queerie_info,
            "monthly search": monthly_searches,
            "keyword info": keyword_info
            }
        return ret

    def Search_Intent(self, keyword, location_code, language_code):
        #HISTORICAL SEARCH VOLUME
        kwargs =  {
            "keywords": [keyword],
            "location_code": location_code,
            "language_code": language_code,
            }
        
        search_intent_response, cost = self.api.call('dataforseo_labs/google/search_intent/live', kwargs, method="post")
        search_intent = search_intent_response["tasks"][0]["result"][0]["items"][0]

        search_intent_obj = {
            "cost": cost,
            "Intent": search_intent["keyword_intent"]["label"],
            "Probability": search_intent["keyword_intent"]["probability"]

        }
        return search_intent_obj
    

    def Trends_Data(self, keyword):
        #HISTORICAL SEARCH VOLUME
        try:
            kwargs =  {
                "keywords": [keyword]
                }
            
            trends_data_response, cost = self.api.call('keywords_data/dataforseo_trends/merged_data/live', kwargs, method="post")
            trends_data_response = trends_data_response["tasks"][0]["result"][0]["items"]
            Geography = trends_data_response[1]["interests"][0]["values"]
            print(Geography)
            if Geography:
                Geography = sorted(Geography, key= lambda x: x["value"])
        
            
            DemographyAge = {}
            for ageRange in trends_data_response[2]["demography"]["age"][0]["values"]:
                DemographyAge[ageRange["type"]] = ageRange["value"]
            
            DemographyGender = {}
            for gender in trends_data_response[2]["demography"]["gender"][0]["values"]:
                DemographyGender[gender["type"]] = gender["value"]
        except:
            cost = None
            Geography = None
            DemographyAge = None
            DemographyGender = None
        ret = {
            "cost": cost,
            "Geography": Geography,
            "Demography": {
                "Age": DemographyAge,
                "Gender": DemographyGender
            }
        }
        return ret


    def Related_Keywords(self, keyword, location_code, language_code):
        try:
            kwargs =  {
                "keyword": keyword,
                "location_code": location_code,
                "language_code": language_code,
                "depth": 1,
                "ignore synonyms": True,
                "replace_with_core_keyword": True
                }
            
            related_keywords_response, cost = self.api.call('dataforseo_labs/google/related_keywords/live', kwargs, method="post")
            related_keywords = related_keywords_response["tasks"][0]["result"][0]["items"]
            
            ret = []
            for kw in related_keywords:
                ret.append(
                    {
                        "Keyword": kw["keyword_data"]["keyword"],
                        "Search Volume": kw["keyword_data"]["keyword_info"]["search_volume"],
                        "CPC": kw["keyword_data"]["keyword_info"]["cpc"],
                        "Competition Level": kw["keyword_data"]["keyword_info"]["competition_level"],
                        "Competition": kw["keyword_data"]["keyword_info"]["competition"],
                        "Low Top of Page Bid": kw["keyword_data"]["keyword_info"]["low_top_of_page_bid"],
                        "High Top of Page Bid": kw["keyword_data"]["keyword_info"]["high_top_of_page_bid"],
                        "Keyword Difficulty": kw["keyword_data"]["keyword_properties"]["keyword_difficulty"],
                        "Search Intent": kw["keyword_data"]["search_intent_info"]["main_intent"],


                    }
                )     
        except:
            cost = -1
            ret = None
        returnDict = {"cost": cost, "array": ret}
        return returnDict


    # def call(self, endpoint, kwargs):
    #     print("CALLING: ", endpoint)
    #     start = time.time()

    #     try:
    #         response = self.api.call('dataforseo_labs/google/' + endpoint + '/live', kwargs, method="post")
    #         cost = response["tasks"][0]["cost"]

    #         print("TOTAL TIME ELAPSED: ", time.time() - start)
    #         return response["tasks"][0]["result"][0], cost
    #     except:
    #         return {"Error":True}, -1
    # def callTrendsAPI(self, kwargs):
    #     print("CALLING TRENDS: ")
    #     start = time.time()        

    #     try:
    #         response = self.api.call('keywords_data/dataforseo_trends/merged_data/live', kwargs, method="post")
    #         # print(json.dumps(kwargs))
            
    #         # print(json.dumps(response))
    #         print("TOTAL TIME ELAPSED: ", time.time() - start)
    #         cost = response["tasks"][0]["cost"]
    #         return response["tasks"][0]["result"][0], cost
    #     except:
    #         return {"Error":True}, -1        
    # def populate_related_array(self, items):
    #     ret = []
    #     for kw in items:
    #         ret.append(
    #             {
    #                 "Keyword": kw["keyword_data"]["keyword"],
    #                 "Search Volume": kw["keyword_data"]["keyword_info"]["search_volume"],
    #                 "CPC": kw["keyword_data"]["keyword_info"]["cpc"],
    #                 "Competition Level": kw["keyword_data"]["keyword_info"]["competition_level"],
    #                 "Competition": kw["keyword_data"]["keyword_info"]["competition"],
    #                 "Low Top of Page Bid": kw["keyword_data"]["keyword_info"]["low_top_of_page_bid"],
    #                 "High Top of Page Bid": kw["keyword_data"]["keyword_info"]["high_top_of_page_bid"],
    #                 "Keyword Difficulty": kw["keyword_data"]["keyword_properties"]["keyword_difficulty"],
    #                 "Search Intent": kw["keyword_data"]["search_intent_info"]["main_intent"],


    #             }
    #         )    
    #     return ret   
    # def populate_suggested_array(self, items):
    #     ret = []
    #     for kw in items:
    #         ret.append(
    #             {
    #                 "Keyword": kw["keyword"],
    #                 "Search Volume": kw["keyword_info"]["search_volume"],
    #                 "CPC": kw["keyword_info"]["cpc"],
    #                 "Competition Level": kw["keyword_info"]["competition_level"],
    #                 "Competition": kw["keyword_info"]["competition"],
    #                 "Low Top of Page Bid": kw["keyword_info"]["low_top_of_page_bid"],
    #                 "High Top of Page Bid": kw["keyword_info"]["high_top_of_page_bid"],
    #                 "Keyword Difficulty": kw["keyword_properties"]["keyword_difficulty"],
    #                 "Search Intent": kw["search_intent_info"]["main_intent"],


    #             }
    #         )    
    #     return ret        
    # def related_keywords_and_keyword_info(self, keyword, location_code, language_code):
    #     try:
    #         #RELATED KEYWORDS
    #         related_keywords_response, related_cost = self.call('related_keywords', {
    #         "keyword": keyword,
    #         "location_code": location_code,
    #         "language_code": language_code,
    #         "include_seed_keyword": True,
    #         "depth": 2,
    #         "ignore_synonyms": True,
    #         "include_serp_info": True

    #         })
    #         related_keywords = related_keywords_response["items"]


    #         related_keywords_ret = self.populate_related_array(related_keywords)
            
    #         #SEED KEYWORD DATA FROM RELATED KEYWORDS
    #         seed_keyword_data = related_keywords_response["seed_keyword_data"]

    #     except:
    #         print("A")
    #         related_keywords_ret, seed_keyword_data = {"Error", True}, {"Error", True}


    #     try:
    #         #SEARCH INTENT
    #         search_intent, search_intent_cost = self.call('search_intent', {
    #             "keywords": [keyword],
    #             "location_code": location_code,
    #             "language_code": language_code,
    #             })
            
    #         search_intent = search_intent["items"][0]
    #     except:
    #         print("B")
    #         search_intent = {"Error", True}

    #     try:
    #         #HISTORICAL SEARCH VOLUME
    #         historical_search_volume, historical_cost = self.call('historical_search_volume', {
    #             "keywords": [keyword],
    #             "location_code": location_code,
    #             "language_code": language_code,
    #             })
    #         historical_search_volume = historical_search_volume["items"][0]["keyword_info"]["monthly_searches"]
    #     except:
    #         print("C")
    #         historical_search_volume = {"Error", True}


    #     #DEMOGRAPHICS AND GEOGRAPHY
    #     #[trends_Costs,Geography,DemographyAge,DemographyGender] = self.trends(keyword)
    #     #KEYWORD INFORMATION
    #     print("D")
    #     keyword_information = {
    #         "Search Information":
    #             {
    #                 "Keyword": seed_keyword_data["keyword"],
    #                 "Location": seed_keyword_data["location_code"],
    #                 "Language": seed_keyword_data["language_code"]
    #             },
            
    #         "Keyword Info":
    #             {
    #                 "General Information":
    #                     {
    #                         "Search Volume": seed_keyword_data["keyword_info"]["search_volume"],
    #                         "CPC": seed_keyword_data["keyword_info"]["cpc"]
    #                     },
    #                 "Difficulty": seed_keyword_data["keyword_properties"]["keyword_difficulty"],
    #                 "Catagories": seed_keyword_data["keyword_info"]["categories"],
    #                 "Bid Information":
    #                     {
    #                         "Low Top Of Page Bid": seed_keyword_data["keyword_info"]["low_top_of_page_bid"],
    #                         "High Top Of Page Bid": seed_keyword_data["keyword_info"]["high_top_of_page_bid"]
    #                     },
    #                 "Competition":
    #                     {
    #                         "Competition": seed_keyword_data["keyword_info"]["competition"],
    #                         "Competition Level": seed_keyword_data["keyword_info"]["competition_level"],
    #                     },
    #                 "SERP Information":
    #                     {
    #                         "Item Types": seed_keyword_data["serp_info"]["serp_item_types"],
    #                         "Number of Results": seed_keyword_data["serp_info"]["se_results_count"]
    #                     },
    #                 "Backlink Information":
    #                     {
    #                         "Backlinks":
    #                             {
    #                                 "Backlinks": seed_keyword_data["avg_backlinks_info"]["backlinks"],
    #                                 "DoFollow Links": seed_keyword_data["avg_backlinks_info"]["dofollow"],
    #                             },
    #                         "Referrers":
    #                             {
    #                                 "Referring Pages": seed_keyword_data["avg_backlinks_info"]["referring_pages"],
    #                                 "Referring Domains": seed_keyword_data["avg_backlinks_info"]["referring_domains"],
    #                                 "Referring Main Domains": seed_keyword_data["avg_backlinks_info"]["referring_main_domains"]
    #                             },
    #                         "Rank":
    #                             {
    #                                 "Rank":seed_keyword_data["avg_backlinks_info"]["rank"],
    #                                 "Main Domain Rank":seed_keyword_data["avg_backlinks_info"]["main_domain_rank"]
    #                             }
    #                     },
    #                 "Search Intent":
    #                     {
    #                         "Main Intent": 
    #                             {
    #                                 "Label": search_intent["keyword_intent"]["label"],
    #                                 "Probability": search_intent["keyword_intent"]["probability"]
    #                             },
    #                         "Secondary Intents": 
    #                             [{"Label": intent["label"], "Probability": intent["Probability"] } for intent in search_intent["secondary_keyword_intents"]] if search_intent["secondary_keyword_intents"] else None
    #                     },
    #                 "Historical Search Volume":
    #                     {
    #                         "6 Month":historical_search_volume[:6],
    #                         "1 Year":historical_search_volume[:12],
    #                         "2 Year":historical_search_volume[:24],
    #                         "3 Year":historical_search_volume[:36],
    #                         "4 Year":historical_search_volume[:48]
    #                     },
    #                 # "Geography": Geography,
    #                 # "Demography":
    #                 #     {
    #                 #         "Age": DemographyAge,
    #                 #         "Gender": DemographyGender
    #                 #     }
    #             }
    #     }
    #     print("E")
    #     return related_keywords_ret, keyword_information, related_cost + search_intent_cost + historical_cost# + trends_Costs
    # def analyze_keyword(self, keyword, location_code, language_code):
    #     start = time.time()
    #     #try:
    #     related_keywords, keyword_information, related_cost = self.related_keywords_and_keyword_info(keyword, location_code, language_code)
    #     #except:
    #         #related_keywords, keyword_information, related_cost = {"Error":True}, {"Error": True},-1
     

    #     try:
    #         keyword_suggestions, suggestion_cost= self.call('keyword_suggestions', {
    #             "keyword": keyword,
    #             "location_code": location_code,
    #             "language_code": language_code,
    #             "ignore_synonyms": True,
    #             "limit": 8
    #             })
    #         keyword_suggestions = keyword_suggestions["items"]
    #         keyword_suggestions = self.populate_suggested_array(keyword_suggestions)
    #     except:
    #         keyword_suggestions = {"Error", True}


    #     try:
    #         keyword_ideas, idea_cost = self.call('keyword_ideas', {
    #             "keywords": [keyword],
    #             "location_code": location_code,
    #             "language_code": language_code,
    #             "ignore_synonyms": False,
    #             "limit": 8
    #             })
    #         keyword_ideas = keyword_ideas["items"]
    #         keyword_ideas = self.populate_suggested_array(keyword_ideas)        
    #     except:
    #         keyword_ideas = {"Error", True}


    #     end = time.time()
    #     return {
    #         "time elapsed": {
    #             "total": end - start                },
    #         "cost": idea_cost + suggestion_cost + related_cost,
    #         "keyword information": keyword_information,
    #         "related keywords": related_keywords,
    #         "keyword suggestions": keyword_suggestions,
    #         "keyword ideas": keyword_ideas,
    #     }
    # def keyword_planner(self, keyword, location_code, language_code, closely_variants,ignore_synonyms, filters):
    #     keyword_ideas, idea_cost = self.call('keyword_ideas', {
    #         "keywords": [keyword],
    #         "location_code": location_code,
    #         "language_code": language_code,
    #         "closely_variants": closely_variants,
    #         "ignore_synonyms": ignore_synonyms,
    #         "filters": filters,
    #         "limit": 50
    #         })
    #     keyword_ideas = keyword_ideas["items"]
    #     keyword_ideas = self.populate_suggested_array(keyword_ideas) 
    #     return {
    #         "cost": idea_cost,
    #         "keyword ideas": keyword_ideas,
    #     }               

    # def trends(self, keyword):
    #     trendsAPI, API_costs = self.callTrendsAPI({
    #         "keywords": [keyword]})
    #     trendsAPI = trendsAPI["items"]
    #     Geography = trendsAPI[1]["interests"][0]["values"]

    #     Geography = sorted(Geography, key= lambda x: x["value"])
       

    #     if len(Geography) >= 25:
    #         Geography= Geography[-25:]
        
    #     DemographyAge = {}
    #     for ageRange in trendsAPI[2]["demography"]["age"][0]["values"]:
    #         DemographyAge[ageRange["type"]] = ageRange["value"]
        
    #     DemographyGender = {}
    #     for gender in trendsAPI[2]["demography"]["gender"][0]["values"]:
    #         DemographyGender[gender["type"]] = gender["value"]
                
        
    #     return [API_costs,Geography,DemographyAge,DemographyGender]

        