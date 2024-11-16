def filter_noun(text):
    noun=["Ramesh", "agra", 123, "patna"]
    return [word for word in text if word in noun]
# Testing the function
print(filter_noun(["Ramesh", "agra", 123, "patna", "Vinay", 234, "Kanpur"]))