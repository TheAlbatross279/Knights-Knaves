from parser import Parser

text = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Zoey and Mel. Zoey tells you that Mel is a knave. Mel says, `Neither Zoey nor I are knaves.'
Can you determine who is a knight and who is a knave?'''


text2 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Peggy and Zippy.  Peggy tells you that 'of Zippy and I, exactly one is a knight'.  Zippy tells you that only a knave would say that Peggy is a knave.
Can you determine who is a knight and who is a knave?'''


text3 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Sue and Zippy.  Sue says that Zippy is a knave.  Zippy says, 'I and Sue are knights.'
Can you determine who is a knight and who is a knave?'''


text4 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Sally and Zippy.  Sally claims, 'I and Zippy are not the same.'  Zippy says, 'Of I and Sally, exactly one is a knight.'
Can you determine who is a knight and who is a knave?'''

text5 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Homer and Bozo.  Homer tells you, 'At least one of the following is true: that I am a knight or that Bozo is a knight.'  Bozo claims, 'Homer could say that I am a knave.'
Can you determine who is a knight and who is a knave?'''


text6 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Marge and Zoey.  Marge says, 'Zoey and I are both knights or both knaves.'  Zoey claims, 'Marge and I are the same.'
Can you determine who is a knight and who is a knave?'''

text7 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Mel and Ted.  Mel tells you, 'Either Ted is a knight or I am a knight.'  Ted tells you that Mel is a knave.
Can you determine who is a knight and who is a knave?'''

text11 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Zed and Alice.  Zed tells you, 'I am a knight or Alice is a knave.'  Alice tells you, 'Of Zed and I, exactly one is a knight.'
Can you determine who is a knight and who is a knave?'''


text8 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Ted and Zeke.  Ted claims, 'Zeke could say that I am a knave.'  Zeke claims that it's not the case that Ted is a knave.
Can you determine who is a knight and who is a knave?'''


text9 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Ted and Zippy.  Ted says, 'Of I and Zippy, exactly one is a knight.'  Zippy says that Ted is a knave.
Can you determine who is a knight and who is a knave?'''


text10 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Zed and Bart.  Zed says, 'Bart is a knight or I am a knight.'  Bart tells you, 'Zed could claim that I am a knave.'
Can you determine who is a knight and who is a knave?'''

text12 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Bob and Betty.  Bob claims that Betty is a knave.  Betty tells you, 'I am a knight or Bob is a knight.'
Can you determine who is a knight and who is a knave?'''

text13 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Bart and Ted.  Bart claims, 'I and Ted are both knights or both knaves.'  Ted tells you, 'Bart would tell you that I am a knave.'
Can you determine who is a knight and who is a knave?'''

text14 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Bart and Mel.  Bart claims, 'Both I am a knight and Mel is a knave.'  Mel tells you, 'I would tell you that Bart is a knight.'
Can you determine who is a knight and who is a knave?'''

text15 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Betty and Peggy.  Betty tells you that Peggy is a knave.  Peggy tells you, 'Betty and I are both knights.'
Can you determine who is a knight and who is a knave?'''

text16 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Bob and Mel.  Bob tells you, 'At least one of the following is true: that I am a knight or that Mel is a knave.'  Mel claims, 'Only a knave would say that Bob is a knave.'
Can you determine who is a knight and who is a knave?'''

text17 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Zed and Alice.  Zed tells you, 'Alice could say that I am a knight.'  Alice claims, 'It's not the case that Zed is a knave.'
Can you determine who is a knight and who is a knave?'''

text18 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Alice and Ted.  Alice tells you, 'Either Ted is a knave or I am a knight.'  Ted tells you, 'Of I and Alice, exactly one is a knight.'
Can you determine who is a knight and who is a knave?'''

text19 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Zeke and Dave.  Zeke tells you, 'Of I and Dave, exactly one is a knight.'  Dave claims, 'Zeke could claim that I am a knight.'
Can you determine who is a knight and who is a knave?'''

text20 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Zed and Zoey.  Zed says that it's false that Zoey is a knave.  Zoey claims, 'I and Zed are different.'
Can you determine who is a knight and who is a knave?'''

text21 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Sue and Marge.  Sue says that Marge is a knave.  Marge claims, 'Sue and I are not the same.'
Can you determine who is a knight and who is a knave?'''


text22 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Bob and Ted.  Bob says, 'I am a knight or Ted is a knave.'  Ted says that only a knave would say that Bob is a knave.
Can you determine who is a knight and who is a knave?'''

text23 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Zed and Peggy.  Zed says that Peggy is a knave.  Peggy tells you, 'Either Zed is a knight or I am a knight.'
Can you determine who is a knight and who is a knave?'''

text24 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Zed and Bob.  Zed says, 'Both I am a knight and Bob is a knave.'  Bob says, 'Zed could say that I am a knight.'
Can you determine who is a knight and who is a knave?'''

text25 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Rex and Marge.  Rex tells you, 'I and Marge are knights.'  Marge says, 'I would tell you that Rex is a knight.'
Can you determine who is a knight and who is a knave?'''

text26 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Bozo and Marge.  Bozo tells you, 'Marge and I are different.'  Marge says that only a knave would say that Bozo is a knave.
Can you determine who is a knight and who is a knave?'''

text27 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Peggy and Carl.  Peggy tells you that only a knave would say that Carl is a knave.  Carl tells you, 'Peggy and I are different.'
Can you determine who is a knight and who is a knave?'''

text28 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Mel and Homer.  Mel tells you, 'I would tell you that Homer is a knave.'  Homer tells you, 'Either I am a knight or Mel is a knave.'
Can you determine who is a knight and who is a knave?'''

text29 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Carl and Betty.  Carl says, 'Neither Betty nor I are knaves.'  Betty claims, 'Carl and I are the same.'
Can you determine who is a knight and who is a knave?'''

text30 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Marge and Ted.  Marge tells you, 'Ted and I are different.'  Ted claims, 'Only a knave would say that Marge is a knave.'
Can you determine who is a knight and who is a knave?'''

text31 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Abe and Bozo.  Abe says, 'I and Bozo are not the same.'  Bozo tells you, 'I am a knight or Abe is a knight.'
Can you determine who is a knight and who is a knave?'''

text32 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Rex and Abe.  Rex tells you, 'I would tell you that Abe is a knight.'  Abe tells you that it's false that Rex is a knave.
Can you determine who is a knight and who is a knave?'''

text33 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Sue and Joe.  Sue says, 'I and Joe are different.'  Joe claims, 'It's false that Sue is a knave.'
Can you determine who is a knight and who is a knave?'''

text34 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Marge and Homer.  Marge claims, 'I would tell you that Homer is a knight.'  Homer tells you that Marge is a knave.
Can you determine who is a knight and who is a knave?'''

text35 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Sally and Ted.  Sally says, 'I and Ted are different.'  Ted says, 'I and Sally are both knights or both knaves.'
Can you determine who is a knight and who is a knave?'''

text36 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Bart and Sally.  Bart tells you, 'Sally and I are not the same.'  Sally tells you, 'I could claim that Bart is a knave.'
Can you determine who is a knight and who is a knave?'''

text37 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Bob and Sally.  Bob tells you, 'At least one of the following is true: that I am a knight or that Sally is a knave.'  Sally says, 'I would tell you that Bob is a knave.'
Can you determine who is a knight and who is a knave?'''

text38 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Alice and Zippy.  Alice says, 'Zippy and I are not the same.'  Zippy claims, 'I am a knight or Alice is a knave.'
Can you determine who is a knight and who is a knave?'''

text39 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Peggy and Alice.  Peggy says, 'I and Alice are both knights or both knaves.'  Alice says, 'Peggy and I are the same.'
Can you determine who is a knight and who is a knave?'''

text40 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Alice and Zed.  Alice tells you, 'At least one of the following is true: that Zed is a knave or that I am a knight.'  Zed says, 'It's not the case that Alice is a knave.'
Can you determine who is a knight and who is a knave?'''

text41 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Rex and Marge.  Rex claims, 'Both Marge is a knave and I am a knight.'  Marge says that only a knave would say that Rex is a knave.
Can you determine who is a knight and who is a knave?'''

text42 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Homer and Bill.  Homer tells you that it's not the case that Bill is a knave.  Bill tells you, 'Homer and I are not the same.'
Can you determine who is a knight and who is a knave?'''

text43 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Marge and Betty.  Marge tells you, 'Betty is a knave and I am a knight.'  Betty says, 'I could claim that Marge is a knight.'
Can you determine who is a knight and who is a knave?'''

text44 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Zippy and Zeke.  Zippy claims, 'Zeke is a knave or I am a knight.'  Zeke claims, 'Zippy could claim that I am a knave.'
Can you determine who is a knight and who is a knave?'''

text45 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Carl and Bill.  Carl says, 'I and Bill are both knights or both knaves.'  Bill claims, 'Only a knave would say that Carl is a knave.'
Can you determine who is a knight and who is a knave?'''

text46 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Homer and Abe.  Homer claims that it's false that Abe is a knave.  Abe tells you, 'I could claim that Homer is a knave.'
Can you determine who is a knight and who is a knave?'''

text47 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Peggy and Joe.  Peggy tells you, 'Joe is a knave.'  Joe claims that of Peggy and I, exactly one is a knight.
Can you determine who is a knight and who is a knave?'''

text48 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Betty and Sally.  Betty says, 'At least one of the following is true: that Sally is a knight or that I am a knight.'  Sally claims, 'I and Betty are not the same.'
Can you determine who is a knight and who is a knave?'''


text49 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Bob and Bill.  Bob says, 'Bill is a knave.'  Bill says, 'Bob and I are different.'
Can you determine who is a knight and who is a knave?'''

text50 = '''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
You meet two inhabitants: Abe and Homer.  Abe tells you that Homer is a knave.  Homer says, 'Abe could say that I am a knave.'
Can you determine who is a knight and who is a knave?'''

list = [text, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11, text12, 
        text13, text14, text15, text16, text17, text18, text19, text20, text21, text22, text23, text24,
        text25, text26, text27, text28, text29, text30, text31, text32, text33, text34, text35, text36, text37, text38, text39, text40, 
        text41, text42, text43, text44, text45, text46, text47, text48, text49, text50]

results = [
['(B is False)', '!(A is False) and !(B is False)'],
['(A is True if !(B is True)) or (B is True if !(A is True))', '!(A is False)'],
['(B is False)', '(A is True and B is True)'],
['(A != B)', '(A is True if !(B is True)) or (B is True if !(A is True))'],
['(A is True or B is True)', '(A is True if B is False)'],
['(A is True and B is True) or (A is False and B is False)', '(A == B)'],
['(A is True or B is True)', '(A is False)'],
['(B is True if A is False)', '(!(A is False))'],
['(A is True if !(B is True)) or (B is True if !(A is True))', '(A is False)'],
['(A is True or B is True)', '(A is True if B is False)'],
['(A is True or B is False)', '(A is True if !(B is True)) or (B is True if !(A is True))'],
['(B is False)', '(A is True or B is True)'],
['(A is True and B is True) or (A is False and B is False)', '(A is True if B is False)'],
['(A is True is False and B is True is False)', '(B is True if A is True)'], # broken
['(B is False)', '(A is True and B is True)'], ###
['(A is True or B is False)', '!(A False is False)'], ###
['(B is True if A is True)', '(!(A is False))'],
['(A is False or B is True)', '(A is True if !(B is True)) or (B is True if !(A is True))'],#
['(A is True if !(B is True)) or (B is True if !(A is True))', '(A is True if B is True)'],
['(!(B is False))', '(A != B)'],
['(B is False)', '(A != B)'],
['(A is True or B is False)', '!(A False is False)'],
['(B is False)', '(A is True or B is True)'],
['(A is True is False and B is True is False)', '(A is True if B is True)'],
['(A is True and B is True)', '(B is True if A is True)'],
['(A != B)', '!(A False is False)'],
['!(B False is False)', '(A != B)'],
['(A is True if B is False)', '(A is True or B is False)'],
['!(A is False) and !(B is False)', '(A == B)'],
['(A != B)', '!(A False is False)'],
['(A != B)', '(A is True or B is True)'],
['(A is True if B is True)', '(!(A is False))'],
['(A != B)', '(!(A is False))'],
['(A is True if B is True)', '(A is False)'],
['(A != B)', '(A is True and B is True) or (A is False and B is False)'],
['(A != B)', '(B is True if A is False)'],
['(A is True or B is False)', '(B is True if A is False)'],
['(A != B)', '(A is True or B is False)'],
['(A is True and B is True) or (A is False and B is False)', '(A == B)'],
['(A is False or B is True)', '(!(A is False))'],
['(A is False is True and B is False is True)', '!(A False is False)'],
['(!(B is False))', '(A != B)'],
['(A is False is True and B is False is True)', '(B is True if A is True)'],
['(A is False or B is True)', '(A is True if B is False)'],
['(A is True and B is True) or (A is False and B is False)', '!(A False is False)'],
['(!(B is False))', '(B is True if A is False)'],
['(B is False)', '(A is True if !(B is True)) or (B is True if !(A is True))'],
['(A is True or B is True)', '(A != B)'],
['(B is False)', '(A != B)'],
['(B is False)', '(A is True if B is False)']
    ]

retrieved = []
p = Parser();
for t in list:
 #   print "TESTING text....."
    statements = p.convert(t)    
    retrieved.append(statements)
#    print "DONE"

for ndx in range(0, len(retrieved)):
    print "Testing results..." + str(ndx)
    if retrieved[ndx][0] != results[ndx][0]:
        print "Error: "
        print "     " + retrieved[ndx][0]
        print  "     " + results[ndx][0]
    if retrieved[ndx][1] != results[ndx][1]:
        print "Error: "
        print  "     " + retrieved[ndx][1]
        print  "     " + results[ndx][1]
    
        



    

