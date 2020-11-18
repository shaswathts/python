text = "X-DSPAM-Confidence:    0.8475";
find = text.find(':')
strip = text[19:]
fl = float(strip)
print(strip.lstrip())
