import re

def make_regex_str_from_file(file_name):
    f = open(file_name, "r")

    result = ""

    for x in f:
        result += x[:-1]
        result += "|"

    return result[:-1]

places = make_regex_str_from_file("Files/places.txt")
vehicles = make_regex_str_from_file("Files/vehicles.txt")

stopwords_f = "از|در مسیر"
stopwords_t = "به|به سوی|به سمت|به طرف|سمت|تا|در راستای|در جهت|آمدم"
stopwords_v = "با|با یک| با خودروی|به کمک|به وسیله|بوسیله|با استفاده از|بکمک"

def print_output(text, interval):
    result = ""
    result_span = ""
    if (len(text) > 0):
        result = text[0][1]
        result_span = [interval[0][0] + len(text[0][0]) + 1, interval[0][1]]
    return (result, result_span)

def run_on_sentence(sentence: str):
    interval_from = [(m.start(0), m.end(0)) for m in re.finditer(f"({stopwords_f}) ({places})", sentence)]
    text_from = re.findall(f"({stopwords_f}) ({places})", sentence)

    interval_to = [(m.start(0), m.end(0)) for m in re.finditer(f"({stopwords_t}) ({places})", sentence)]
    text_to = re.findall(f"({stopwords_t}) ({places})", sentence)

    interval_vehicle = [(m.start(0), m.end(0)) for m in re.finditer(f"({stopwords_v}) ({vehicles})", sentence)]
    text_vehicle = re.findall(f"({stopwords_v}) ({vehicles})", sentence)

    fr = print_output(text_from, interval_from)
    to = print_output(text_to, interval_to)
    ve = print_output(text_vehicle, interval_vehicle)

    final_result = {
        "from": fr[0],
        "from_span": fr[1],
        "to": to[0],
        "to_span": to[1],
        "vehicle": ve[0],
        "vehicle_span": ve[1]
    }

    return final_result

def not_empty(dic):
    for key in dic:
        if dic[key] != "":
            return True
    return False

def run(input: str):
    sentences = re.split('\.|،|!|\?|!|؟', input)
    
    result = []
    
    for sentence in sentences:
        dic = run_on_sentence(sentence)
        if not_empty(dic):
            result.append(dic)
    
    print(result)

text = input()
run(text)