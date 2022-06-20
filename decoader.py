def encrypt_message(message,fname):
      '''


      :param message:
      :param fname:
      :return:
      '''
      masterList=[]
      assert isinstance(message,str)
      messageList = message.split(' ')
      lineNum=0
      with open(fname,'r') as file1:
            for m in messageList:
                  for line in file1:
                        lineNum+=1
                        insideLine = line.split(' ')
                        if m in insideLine:
                              masterList.append((lineNum,insideLine.index(m)))
                              break


      return masterList

def decrypt_message(inlist,fname):
      '''
      Given `inlist`, which is a list of 2-tuples`fname` which is the
      name of a text file source for the codebook, return the encrypted message.

      :param message: inlist to decrypt
      :type message: list
      :param fname: filename for source text
      :type fname: str
      '''
      assert isinstance(inlist, list)

      lineNum = 0
      message=''
      with open(fname,'r') as file1:
            for m in inlist:
                  assert isinstance(m,tuple)
                  for line in file1:
                        lineNum += 1
                        insideLine = line.split(' ')

                        if m[0] ==lineNum:
                              word = insideLine[m[1]]
                              message += ' '+word
                              break
      return " ".join(message.split())

#l=encrypt_message('it it it it it','book.txt')
#print(decrypt_message(l,'book.txt'))