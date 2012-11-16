"""


"""
import re
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

        statements = []

        #parse first statement
        allowed = ["or", "one", "we", "I", 
                   "nor", "both", "could", "would",
                   "case", "is", "same", "different",
                   "exactly", "and"]
        
        logic = {"are": "is",
                 "false": "!", 
                 "not": "!",
                 "am": "is"
                 }
        
        for sentence in sentences:
            cleaned = []
            if sentence != sentences[0]:
                sentence = re.sub("[^A-Za-z ]", "", sentence)
                sentence = sentence.strip()
                words = sentence.split(" ")
                for word in words: 
                    if word == "knaves" or word == "knave":
                        cleaned.append("False")
                    elif word == "knight" or word == "knights":
                        cleaned.append("True")
                    elif word in names:
                        cleaned.append(name_map[word])
                    elif word == "I":
                        cleaned.append(name_map[words[0]])
                    elif word in allowed:
                        cleaned.append(word)
                    elif word in logic:
                        cleaned.append(logic[word])

                #trim off first name
                cleaned = cleaned[1:]
                #print cleaned        
                #print "DONE GATHERING.."
                if len(cleaned) > 0:
                    output =  " ".join(cleaned)

                    assertion = []
                    prefix = []

                    words = output.split(" ")
                    
                    #split it into the assertion (is false or is true) and the prefix
                    for word in words: 
                        if word == "is" or word == "False" or word == "True":
                            assertion.append(word)
                        else:
                            prefix.append(word)

                    #print assertion
                    #print prefix

                    #it is false that B is a knave
                    if "!" in prefix:
                        if "B" in prefix: 
                            output = "!(B " + " ".join(assertion) +")"
                        if "A" in prefix: 
                            output = "!(A " + " ".join(assertion) +")"

                    #A nor B is False
                    if "nor" in prefix: 
                        output = "!(A " + " ".join(assertion) + ") and !(B " + " ".join(assertion) + ")"

                    #exactly one of us is a knave
                    elif "one" in prefix and "exactly" in prefix:
                        output = "(A " + " ".join(assertion) + " if !(B " + " ".join(assertion) + \
                            ")) or (B " + " ".join(assertion) + " if !(A " + " ".join(assertion) + \
                            "))"

                    #only a knave would say A is a knave
                    elif "would" in prefix:
                        if assertion[0] == "False":
                            output = "!"
                        if "A" in prefix and "B" in prefix:
                            if prefix[0] == "A":
                                output = "(A is True if B " + " ".join(assertion) + ")"
                            elif prefix[0] == "B":
                                output = "(B is True if A " + " ".join(assertion) + ")"
                        else:
                            if "A" in prefix: 
                                output += "(A " + " ".join(assertion) + ")"
                            if "B" in prefix: 
                                output += "(B " + " ".join(assertion) + ")"

                    #! the case that A is False
                    elif "case" in prefix:
                        if "!" in prefix:
                            if "A" in prefix:
                                output = "(!(A" 
                            elif "B" in prefix: 
                                output = "(!(B"
                            output += " " + " ".join(assertion) + "))"
                        else:
                            output = " ".join(output[1:])

                    #are the same or not the same
                    elif "same" in prefix:
                        if "!" in prefix: 
                            output = "(A != B)"
                        else:
                            output = "(A == B)" 


                    elif "different" in prefix:
                        if "!" in prefix: 
                            output = "(A == B)"
                        else:
                            output = "(A != B)" 
                            
                    #could say that I am knave
                    elif "could" in prefix: 
                        if prefix[0] == "A":
                            output = "(A is True if B " + " ".join(assertion) + ")"
                        else:
                            output = "(B is True if A " + " ".join(assertion) + ")"

                    #A and B
                    elif "and" in prefix:
                        if "both" in prefix: 
                            output1 = ""
                            output2 = ""
                            #print assertion
                            if "True" in assertion:
                                output1 = "(A is True and B is True)"
                            if "False" in assertion:
                                output2 = "(A is False and B is False)" 
                            if "or" in prefix :
                                output2 = " or " + output2
                            output = output1 + output2
                        else:
                            output = "(A " + " ".join(assertion) + " and B " + " ".join(assertion) + ")"

                    #A or B
                    elif "or" in prefix:
                        if len(assertion) > 2:
                            assertions = []
                            for word in assertion:
                                #print word
                                if word == "True" or word == "False":
                                    assertions.append(word)
                            output = "(A is " + assertions[0] + " or " + "B is " + assertions[1] +")"
                        else:
                            output = "(A is " + " ".join(assertion) + " or " + " B is "+ \
                                " ".join(assertion) +")"
                    else:
                        output = "(" + output+ ")"
                    statements.append(output)
#        print statements        

        return statements
        
        


        
    
    
