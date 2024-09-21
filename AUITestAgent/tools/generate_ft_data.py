import json

with open("ft_input.json", "r") as f:
    msg = json.load(f)["messages"]

with open('ft_output.jsonl', 'a') as f:
    f.write("\n")
    f.write("{\"message\": [")
    _len = len(msg)
    for cnt, entry in enumerate(msg):
        json.dump(entry, f)
        if cnt == _len - 1:
            break
        f.write(', ')
    f.write("]}")
