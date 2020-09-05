from translate import Translator
to_lan=['hindi','Spanish','French','Chinese','japanese']
for x in to_lan:
    translator=Translator(from_lang='english',to_lang=x)
    result=translator.translate('I love you')
    print(result)