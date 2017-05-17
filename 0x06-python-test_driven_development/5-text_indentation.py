#!/usr/bin/python3
def text_indentation(text):
   if not isinstance(text, str):
      raise TypeError("text must be a string")
   [i.strip for i in text.split(".")]
   text = text.replace(". ",".\n\n")
   [i.strip for i in text.split("?")]
   text = text.replace("? ","?\n\n")
   [i.strip for i in text.split(":")]
   text = text.replace(": ",":\n\n")
   print(text)
