import re

def make_regex_str_from_file(file_name):
    f = open(file_name, "r")

    result = ""

    for x in f:
        result += x[:-1]
        result += "|"

    return result[:-1]

#def normalize(self, inputs):
    #         normalized = Normalizer().normalize(inputs)
    #         samples = sent_tokenize(normalized)
    #         return samples

def print_output(obj, result):
    print(obj, ":", end=' ')
    answer = ""
    if (len(result) > 0):
        answer = result[0][1]
    print(answer)

places = make_regex_str_from_file("Files/places.txt")
vehicles = make_regex_str_from_file("Files/vehicles.txt")

stopwords_f = "از"
stopwords_t = "به|به سوی|به سمت|به طرف|به مقصد|سمت|تا|در راستای|در جهت"
stopwords_v = "با|با یک| با خودروی|به کمک|به وسیله|بوسیله|با استفاده از|بکمک"

text = input()

result_from = re.findall(f"({stopwords_f}) ({places})", text)
result_to = re.findall(f"({stopwords_t}) ({places})", text)
result_vehicle = re.findall(f"({stopwords_v}) ({vehicles})", text)

print_output("from", result_from)
print_output("to", result_to)
print_output("vehicle", result_vehicle)
