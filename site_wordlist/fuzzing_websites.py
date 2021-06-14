from selenium import webdriver
from time import sleep
import requests as re

driver = webdriver.Firefox()

# This is our target URL. The curly braces is where we will inject our fuzz values:
target_url = "https://mysite.local/authenticate.php?username=placeholder{}"
# Note the presence of "placeholder". We'll use this later on to look for results.

# Start with a couple of basic values
fuzz_values = ["<img>", "<img onerror='alert(1)'"]

# Let's try every possible character to see which if it triggers errors, or if the output is encoded.
for i in range(256):
    fuzz_values.append("%{}aaa".format(i)) # We add "aaa" at the end to see if anything gets truncated.

# Let's try the big list of naughty strings (https://github.com/minimaxir/big-list-of-naughty-strings):
with open("blns.txt") as blns:
    cur_line = blns.readline()
    while cur_line:
        if cur_line[0] != "#":
            fuzz_values.append(cur_line.strip())
        cur_line = blns.readline()

# Write results.
with open("fuzz_results.txt", "wb") as fuzz_results:
    for fuzz_value in fuzz_values:
        fuzz_results.write(b"Fuzz value: {}".format(fuzz_value)) # We track what was tested in the results file.
        driver.get(target_url.format(fuzz_value))
        sleep(1) # Pause while waiting for the form submission's effect. Adjust this time to your convenience.
        page_source = driver.page_source

        # If the page is empty, we assume there is an error.
        if len(page_source.split("\n")) == 0:
            fuzz_results.write(u"\tResult: Error.\n")
            continue

        # Now we go through the page's source code, looking for our "placeholder".
        for line in page_source.split("\n"):
            if 'placeholder' in line:
                m = re.search('(?<=placeholder).*', line)
                if m is not None:
                    result = m.group(0).encode("utf-8")
                    fuzz_results.write(b"\tResult: {}\n".format(result))
                else:
                    fuzz_results.write(u"Result: Error.\n")

        fuzz_results.flush()

driver.close()