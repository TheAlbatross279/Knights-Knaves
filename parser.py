import re 

class Parser(object):
    def convert(self, text):
        paragraphs = text.split("\n")

        #print len(paragraphs)
        main_par = paragraphs[1]

        #print main_par
        sentences = main_par.split(".")
        
        name_map = self.get_names(sentences)
 #       print sentences
        sentences = self.replace_names(sentences, name_map)
   #     print sentences
        sentences = self.remove_intro(sentences)

        sentences = self.replace_knikna(sentences)
        #print sentences
        sentences = self.replace_keywords(sentences)
#        print sentences

        for idx, _ in enumerate(sentences):
            subject = "A" if idx is 0 else "B"
#            sentences[idx] = "( " + sentences[idx] + " )"

            sentences[idx] = self.replace_both(sentences[idx]) 

            tmp = self.replace_at_least(sentences[idx])

            if tmp is not None:
               sentences[idx] = tmp
            else:
               sentences[idx] = self.replace_or(sentences[idx])
           
            sentences[idx] = self.replace_ne(sentences[idx]) 
            sentences[idx] = self.replace_eq(sentences[idx])
            sentences[idx] = self.replace_asserts(sentences[idx], subject) 
            sentences[idx] = self.replace_nor(sentences[idx]) 
            sentences[idx] = self.replace_and(sentences[idx]) 
            #if res != None:
                #print res
        
        #its not the case that
        #its false that
        #abney could say that
        #at least one of the following is true
        
        
        #check for simple patterns
#        print sentences[0]
#        print sentences[1]

        statements = []
        return sentences

    def replace_and(self, sentence):
        sentence = re.sub("A +and +B (.*)", r"(A \g<1>) and (B \g<1>)", sentence)
        return re.sub("(.*) +and +(.*)", r"(\g<1>) and (\g<2>)", sentence)

    def replace_both(self, sentence):
        if re.search("both (True|False) or both (True|False)", sentence) is not None:
            return "A is B"
        else:
            return re.sub("[bB]oth", "", sentence)

    def replace_nor(self, sentence):
        res = re.search("(A|B) +nor +(A|B) is +(True|False)", sentence)

        if res is not None:
            return "(A is not " + res.group(3) + ") and (B is not " + res.group(3) + ")"
        else:
            return sentence

    def replace_asserts(self, sentence, subject):
        res = re.search("(A|B) +asserts (.*)", sentence)

        if res is not None:
            #return "( " + res.group(2) + ") is " + res.group(1)
            ret =  "( " + res.group(2) + ") "
            ret += ("is " + res.group(1)) if res.group(1) is not subject and re.match("(True|False)", res.group(1)) is None else ""
            return ret

        res = re.search("(True|False) +asserts (.*)", sentence)

        if res is not None:
            if res.group(1) is "True":
                return res.group(2)
            else:
                return "not (" + res.group(2) + ")"

        return sentence

    def replace_eq(self, sentence):
        if len(re.findall("((True|False) +\^ +(False|True)|is the same)", sentence)) > 0:
            return "A is B"
        else:
            return sentence

    def replace_ne(self, sentence):
        if len(re.findall("(exactly one is|is different|not the same)", sentence)) > 0:
            return "A != B"
        else:
            return sentence

    def replace_or(self, sentence):
        sentence = re.sub("[eE]ither ", " ", sentence)
        return re.sub("(.*) +or +(.*)", r"( \g<1> ) ^ ( \g<2> )", sentence)

    def replace_at_least(self, sentence):
        sentence, n = re.subn("[aA]t least one  the following is true +(.*) +or +(.*)", r"(\g<1>) or (\g<2>)", sentence)

        return sentence if n > 0 else None

    def get_names(self, sentences) :
        for sent in sentences: 
            sent = re.sub("[^A-Za-z ]", "", sent)
         #   print sent

        #parse names
        names = []
        words = sentences[0].split(" ")
        for word in words:
            if re.findall("[A-Z*.]", word) and word != "You":
                names.append(word)
        symbol_names = ["A", "B"]

        name_map = dict()
        
        #put the names into a map
        for ndx in range(0, len(names)):
            name_map[names[ndx]] = symbol_names[ndx]

        return name_map

    def replace_names(self, sentences, name_map):
        temp_sentences = sentences[1:]
        valid_sentences = []

        #replace names
        for sent in temp_sentences:
            for name, sym in name_map.items():
                sent = re.sub(name, sym, sent)
            valid_sentences.append(sent)
        return valid_sentences

    def remove_intro(self, sentences):
        cleaned = []
        for sent in sentences:
            sent = re.sub("(.*(?:claims|tells you|says),? (?:that)?)", "", sent)
            sent = re.sub("[^A-Za-z ]", "", sent)
            if len(sent) != 0:
                cleaned.append(sent)
        return cleaned

    def replace_keywords(self, sentences):
        cleans = []
        for sent in sentences:
            if sent == sentences[0]:
                sent = re.sub("I ", " A ", sent)
            elif sent == sentences[1]:
                sent = re.sub("I ", " B ", sent)
            sent = re.sub("[Oo]nly ", " ", sent)
            sent = re.sub(" (would|could) (say|claim|tell you) that ", " asserts ", sent)
            sent = re.sub("[iI]ts (?:not the case|false) that (.*)", r' not ( \g<1> )', sent)
            sent = re.sub(" are ", " is ", sent)
            sent = re.sub(" a ", " ", sent)
#            sent = re.sub("[bB]oth ", " ", sent)
            sent = re.sub("[oO]f ", " ", sent)
            sent = re.sub("[nN]either", " ", sent)
            sent = re.sub(" am ", " is ", sent)
            sent = re.sub(" that ", " ", sent)
            cleans.append(sent)
        return cleans 


    def replace_knikna(self, sentences):
        cleans = []
        for sent in sentences:
            sent = re.sub("[kK]naves?", "False", sent)
            sent = re.sub("[kK]nights?", "True", sent)
            cleans.append(sent)
        return cleans
        

text = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Zoey and Mel. Zoey tells you that Mel is a knave. Mel says, `Neither Zoey nor I are knaves.'
Can you determine who is a knight and who is a knave?'''

#p = Parser()
#p.convert(text)
