import lambda_function


def pretty_print_dict(d, indent=0):
    res = ""
    for k, v in d.items():
        res += "\t"*indent + str(k) + "\n"
        if isinstance(v, dict) or isinstance(v, list):
            res += pretty_print_dict(v, indent+1)
        else:
            res += "\t"*(indent+1) + str(v) + "\n"
    return res

def basic_test():
    event1 = {
        "sandbox": False,
        "page": "keywords-analyze-volume-history",
        "args": {
            "keyword": "seo soetware",
            "location_code": 2840,
            "language_code": "en",

        }
    }

    event2 = {
        "sandbox": False,
        "page": "keywords-analyze-search-intent",
        "args": {
            "keyword": "seo soetware",
            "location_code": 2840,
            "language_code": "en",

        }
    }

    event3 = {
        "sandbox": False,
        "page": "keywords-analyze-trends-data",
        "args": {
            "keyword": "seo soetware",
            "location_code": 2840,
            "language_code": "en",

        }
    }

    event4 = {
        "sandbox": False,
        "page": "keywords-analyze-related-keywords",
        "args": {
            "keyword": "seo soetware",
            "location_code": 2840,
            "language_code": "en",

        }
    }            

    context = {}
    resp =  (lambda_function.lambda_handler(event1, context))
    resp =  (lambda_function.lambda_handler(event2, context))
    resp =  (lambda_function.lambda_handler(event3, context))
    resp =  (lambda_function.lambda_handler(event4, context))


basic_test()