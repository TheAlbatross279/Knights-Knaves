import re 

class Parser(object):
    def convert(self, text):
        paragraphs = text.split("\n")

        #print len(paragraphs)
        main_par = paragraphs[1]

        #print main_par
        sentences = main_par.split(".")
        
        name_map = self.get_names(sentences)
  #      print sentences
        sentences = self.replace_names(sentences, name_map)
   #     print sentences
        sentences = self.remove_intro(sentences)

        sentences = self.replace_knikna(sentences)
        #print sentences
        sentences = self.replace_keywords(sentences)
        print sentences



        #its not the case that
        #its false that
        #abney could say that
        
        #check for simple patterns
        statements = []
        return sentences

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
            sent = re.sub(" are ", " is ", sent)
            sent = re.sub(" a ", " ", sent)
            sent = re.sub(" [oO]f ", " ", sent)
            sent = re.sub("[nN]either", "", sent)
            sent = re.sub(" am ", " is ", sent)
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
