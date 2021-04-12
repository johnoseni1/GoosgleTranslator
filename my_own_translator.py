from googletrans import Translator
translator = Translator()
text = '''Hi Mr enoch My name is John and am in ss3
'''

dt = translator.detect(text)
print(dt)

translate = translator.translate(text, dest="ja")
print(translate)