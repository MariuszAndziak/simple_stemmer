import string
import re

class TextCleaner(object):
    """
    Text cleaner. This class can remove any digits and punctuation from a given
    text. It also makes the text lowercase.

    Args:
        object (str): a sentence as a single string
    """
    def __init__(self, text):
        self.text = text
    
    def __len__(self):
        return len(self.text)
    
    def __repr__(self):
        return self.text

    def lower(self):
        self.text = self.text.lower()
        return self.text

    def remove_punctuations(self):
        self.text = self.text.translate(self.text.maketrans('', '', string.punctuation))
        return self.text

    def remove_digits(self):
        self.text = re.sub(r'[\d+]','', self.text)
        return self.text
    
    def clean(self):
        self.lower()
        self.remove_punctuations()
        self.remove_digits()
        return self.text

class TextStemmer(object):
    """
    Simple stemmer based on a Porter stemmer for polish language
    Stemming procedure was taken from
    https://github.com/Tutanchamon/pl_stemmer/blob/master/pl_stemmer.py'

    Args:
        object (str): a sentence as a single string

    Returns:
        _type_: _description_
    """
    def __init__(self, text):
        self.text = text
        # self.word = word
    
    def __repr__(self):
        return self.text

    def remove_general_ends(word):
        if len(word) > 4 and word[-2:] in {"ia", "ie"}:
            return word[:-2]
        if len(word) > 4 and word[-1:] in {"u", u"ą", "i", "a", u"ę", "y", u"ę", u"ł"}:
            return word[:-1]
        return word
        
    def remove_diminutive(word):
        if len(word) > 6:
            if word[-5:] in {"eczek", "iczek", "iszek", "aszek", "uszek"}:
                return word[:-5]
            if word[-4:] in {"enek", "ejek", "erek"}:
                return word[:-2]
        if len(word) > 4:
            if word[-2:] in {"ek", "ak"}:
                return word[:-2]
        return word
        
    def remove_verbs_ends(word):
        if len(word) > 5 and word.endswith("bym"):
            return word[:-3]
        if len(word) > 5 and word[-3:] in {"esz", "asz", "cie", u"eść", u"aść", u"łem", "amy", "emy"}:
            return word[:-3]
        if len(word) > 3 and word[-3:] in {"esz", "asz", u"eść", u"aść", u"eć", u"ać"}:
            return word[:-2]
        if len(word) > 3 and word[-3:] in {"aj"}:
            return word[:-1]
        if len(word) > 3 and word[-2:] in {u"ać", "em", "am", u"ał", u"ił", u"ić", u"ąc"}:
            return word[:-2]
        return word

    def remove_nouns(word):
        if len(word) > 7 and word[-5:] in {"zacja", u"zacją", "zacji"}:
            return word[:-4]
        if len(word) > 6 and word[-4:] in {"acja", "acji", u"acją", "tach", "anie", "enie",
        "eniu", "aniu"}:
            return word[:-4]
        if len(word) > 6 and word.endswith("tyka"):
            return word[:-2]
        if len(word) > 5 and word[-3:] in {"ach", "ami", "nia", "niu", "cia", "ciu"}:
            return word[:-3]
        if len(word) > 5 and word[-3:] in {"cji", "cja", u"cją"}:
            return word[:-2]
        if len(word) > 5 and word[-2:] in {"ce", "ta"}:
            return word[:-2]
        return word
        
    def remove_adjective_ends(word):
        if len(word) > 7 and word.startswith("naj") and (word.endswith("sze")
        or word.endswith("szy")):
            return word[3:-3]
        if len(word) > 7 and word.startswith("naj") and word.endswith("szych"):
            return word[3:-5]
        if len(word) > 6 and word.endswith("czny"):
            return word[:-4]
        if len(word) > 5 and word[-3:] in {"owy", "owa", "owe", "ych", "ego"}:
            return word[:-3]
        if len(word) > 5 and word[-2:] in {"ej"}:
            return word[:-2]
        return word
        
    def remove_adverbs_ends(word):
        if len(word) > 4 and word[:-3] in {"nie", "wie"}:
            return word[:-2]
        if len(word) > 4 and word.endswith("rze"):
            return word[:-2]
        return word

    def remove_plural_forms(word):
        if len(word) > 4 and (word.endswith(u"ów") or word.endswith("om")):
            return word[:-2]
        if len(word) > 4 and word.endswith("ami"):
            return word[:-3]
        return word
    
    def make_stems(self):
        result = []
        for word in self.text.split():
            stem = word[:]
            stem = self.remove_nouns(stem)
            stem = self.remove_diminutive(stem)
            stem = self.remove_adjective_ends(stem)
            stem = self.remove_verbs_ends(stem)
            stem = self.remove_adverbs_ends(stem)
            stem = self.remove_plural_forms(stem)
            stem = self.remove_general_ends(stem)
            result.append((word, stem))
        return result

if __name__ == "main":
    text = 'czerwony czerwonawy. czerwieńszy czerwona, czerwonawa CZerwono'

    data = TextCleaner(text)
    data = data.clean()

    stemmer_object = TextStemmer(data)
    result = stemmer_object.make_stems()
    print(result)