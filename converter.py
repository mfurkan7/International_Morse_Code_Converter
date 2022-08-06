class Converter:
    def __init__(self,sentence_input):
        self.character_list = list(sentence_input.lower())
        #print(self.character_list)
        self.morse_message=[]
        self.translation(self.character_list)
        self.message=' '.join(self.morse_message)
    def translation(self,transcripted_message):
        for character in transcripted_message:
            if character=='a':
                self.morse_message.append('* |||-')
            elif character=='b':
                self.morse_message.append('||| * * *-')
            elif character=='c':
                self.morse_message.append('||| * ||| *-')
            elif character=='d':
                self.morse_message.append('||| * *-')
            elif character=='e':
                self.morse_message.append('*-')
            elif character=='f':
                self.morse_message.append('* * ||| *-')
            elif character=='g':
                self.morse_message.append('||| ||| *-')
            elif character=='h':
                self.morse_message.append('* * * *-')
            elif character=='i':
                self.morse_message.append('* *-')
            elif character=='j':
                self.morse_message.append('* ||| ||| |||-')
            elif character=='k':
                self.morse_message.append('||| * |||-')
            elif character=='l':
                self.morse_message.append('* ||| * *-')
            elif character=='m':
                self.morse_message.append('||| |||-')
            elif character=='n':
                self.morse_message.append('||| *-')
            elif character=='o':
                self.morse_message.append('||| ||| |||-')
            elif character=='p':
                self.morse_message.append('* ||| ||| *-')
            elif character=='q':
                self.morse_message.append('||| ||| |||-')
            elif character=='r':
                self.morse_message.append('* ||| *- ')
            elif character=='s':
                self.morse_message.append('* * *-')
            elif character=='t':
                self.morse_message.append('|||-')
            elif character=='u':
                self.morse_message.append('* * |||-')
            elif character=='v':
                self.morse_message.append('* * * |||-')
            elif character=='w':
                self.morse_message.append('* ||| |||-')
            elif character=='x':
                self.morse_message.append('||| * * |||- ')
            elif character=='y':
                self.morse_message.append('||| * ||| |||-')
            elif character=='z':
                self.morse_message.append('||| ||| * *-')
            elif character=='0':
                self.morse_message.append('||| ||| ||| ||| |||-')
            elif character=='1':
                self.morse_message.append('* ||| ||| ||| |||-')
            elif character=='2':
                self.morse_message.append('* * ||| ||| |||-')
            elif character=='3':
                self.morse_message.append('* * * ||| |||-')
            elif character=='4':
                self.morse_message.append('* * * * |||-')
            elif character=='5':
                self.morse_message.append('* * * * *-')
            elif character=='6':
                self.morse_message.append('||| * * * *- ')
            elif character=='7':
                self.morse_message.append('||| ||| * * *-')
            elif character=='8':
                self.morse_message.append('||| ||| ||| * *-')
            elif character=='9':
                self.morse_message.append('||| ||| ||| ||| *-')
            elif character==' ':
                self.morse_message.append('* * * * * * *-')
            else:
                continue
