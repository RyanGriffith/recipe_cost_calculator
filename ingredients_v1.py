ingredients = [
    {"milk"}, {"m"},
    {"egg"}, {"e"},
    {"flour"}, {"f"},
    {"butter"}, {"b"},
    {"sugar"}, {"s"},
    {"salt"}, {"slt"},
    {"oil"}, {"o"},
    {"cheese"}, {"c"},
]
print("while inputting ingredients leave exit code blank")
print("once finished put in exit code")
exit_code = ""

while exit_code != "quit":
    recipe_ingredients = input("what ingredients are used?: ").strip().lower()
    exit_code = input("exit code: ")
