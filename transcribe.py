from tkinter.filedialog import askopenfilename
import re
from tkinter import filedialog

def delete_strings(text):
    pattern = r"uh|Uh|um|Um|mm-hmm|Mm-hmm|uh-huh|you know|Speaker 0|Speaker 1|Speaker 2"
    text = re.sub(pattern, "", text)
    lines = text.split("\n")
    timestamp_pattern = r"^    \d\d:\d\d:\d\d    $"
    lines = [line for line in lines if not re.match(timestamp_pattern, line)]
    text = "\n".join(lines)

    # Remove repetitions and false starts
    words = text.split()
    new_words = []
    prev_word = None
    for word in words:
        if word != prev_word:
            new_words.append(word)
            prev_word = word

    # Remove false starts (words that start with "-")
    new_words = [word for word in new_words if not word.startswith("-")]

    return " ".join(new_words)

root = filedialog.Tk()
root.filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("text files","*.txt"),("all files","*.*")))
print(root.filename)

with open(root.filename, "r") as f:
    text = f.read()

text = delete_strings(text)

with open(root.filename, "w") as f:
    f.write(text)

root.mainloop()
