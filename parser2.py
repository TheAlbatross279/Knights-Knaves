"""

"""

import re
import copy

class Parser(object):
    def convert(self, text):
        #split paragraphs
        paragraphs = text.split("\n")

        #print len(paragraphs)
        main_par = paragraphs[1]

        #print main_par
        sentences = main_par.split(".")
        
        for sent in sentences: 
            sent = re.sub("[^A-Za-z ]", "", sent)
#            print sent

        #parse names
        names = []
        words = sentences[0].split(" ")
        for word in words:
            if re.findall("[A-Z*.]", word) and word != "You":
                names.append(word)

        #print names
        symbol_names = ["A", "B"]

        name_map = dict()
        
        #put the names into a map
        for ndx in range(0, len(names)):
            name_map[names[ndx]] = symbol_names[ndx]

        #remove the first sentence (since not helpful)
        logic_statements = sentences[1:]
            
        #loop for parsing all sentences
        statements = []
        
        allowed = ["one", "we", "I", 
                   "nor", "both", "could", "would",
                   "case", "is", "same", "different",
                   "exactly", "and"]
        
        logic = {"are": "is",
                 "false": "not", 
                 "am": "is",
                 "or": "^"
                 }

        keywords = {"same": False,
                    "different": False,
                    "both": False,
                    "would": False,
                    "could": False,
                    "one": False,
                    "exactly": False,
                    "and": False,
                    "or": False,
                    "is": False,
                    "nor": False }

        for sentence in logic_statements:
            #clean input
            sentence = re.sub("[^A-Za-z ]", "", sentence)
            sentence = sentence.strip()
            words = sentence.split(" ")
            
            arguments = []
            assertions = []
            output = []
            final_output = []
            is_opperands = False
            is_complex = False
            #second loop to break up words
            for word in words:
                if word == "knaves" or word == "knave":
                    assertions.append("False")
                elif word == "knight" or word == "knights":
                    assertions.append("True")
                elif word in names:
                    arguments.append(name_map[word])
                elif word == "I":
                    arguments.append(name_map[words[0]])
            for word in words:
                if word in allowed or word in logic:
                    #same, different, both, would, could, one, exactly
                    #nor, not, ^, and, or, is
                    if word == "one":
                        output.append("( $ ) ^ ( @ )")                    
                        is_complex = True
                    if word == "same":
                        output.append("$ == @")
                        is_opperands = True
                    if word =="different":
                        output.append("$ != @")
                        is_opperands = True
                    if word == "and":
                        output.append(" $ and @")
                        is_complex = True
                    if word == "or":
                        output.append("$ ^ @")
                        is_complex = True
                    if word == "is":
                        output.append("$ is @")
                        is_complex = True
                    if word == "nor":
                        output.append("not ( $ ) and not ( @ )")
                        is_complex = True
                    if word == "are":
                        output.append("$ is @")
                        is_complex = True
                    if word == "only":
                            pass

                    if is_opperands:
                        final = re.sub("\$", arguments[1], output[0])
                        final = re.sub("\@", arguments[2], final)
                        is_opperands = False

                        print final
                        
                    # CAN WE COMBINE THESE?

            #if and, assert applies to each statement
            #if is, assert is an equals statement

                        
#            print arguments
 #           print output
            count_assert = 0
            count_operands = 0

            final_output = ""
            #if and there, combine 

            if len(arguments) > 0:
               statements.append(final_output)
               print statements
        return statements

text = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Zoey and Mel. Zoey tells you that Mel is a knave. Mel says, `Neither Zoey nor I are knaves.'
Can you determine who is a knight and who is a knave?'''

text2 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Peggy and Zippy.  Peggy tells you that 'of Zippy and I, exactly one is a knight'.  Zippy tells you that only a knave would say that Peggy is a knave.
Can you determine who is a knight and who is a knave?'''


p = Parser()
p.convert(text2)



