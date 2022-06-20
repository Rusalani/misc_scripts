import fileinput
import os
def split_by_n(fname,n=3):
    '''
    Split files into sub files of near same size
    fname : Input file name
    n is the number of segments
    '''


    length = os.path.getsize(fname)

    goal = length / n
    hold = None
    master=False
    masterSum=0
    with open(fname,'rt') as file1:
        for x in range(n):
            summ = 0
            with open(fname + '_'+f"{x:03}" + '.txt', 'wt') as file2:
                if hold is not None:
                    file2.write(hold)
                    file2.write('\r')
                    summ+=len(hold.encode("utf8"))
                    master= False
                for line in file1:
                    if summ < goal and summ + len(line.encode("utf8")) >goal and x != n-1:
                        hold = line[:-1]

                        break
                    if not master:
                        master = True
                    else:
                        temp=True
                    summ += len(line.encode("utf8"))

                    file2.write(line[:-1])
                    file2.write('\r')

            #print(summ)
            masterSum+=summ
    #print(masterSum)



#split_by_n('book.txt',n=3)
