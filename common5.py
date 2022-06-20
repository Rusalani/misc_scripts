def write_chunks_of_five(words,fname):
    '''
    write out chucks of 5 words
    '''
    
    with open(fname, 'w') as f:
        out = []
        for x in words:
            if len(out)==5:
                t='{} {} {} {} {}\n'.format(out[0],out[1],out[2],out[3],out[4])
                f.write(str(t))
                out = []
            
            out.append(x)

        for x in range(len(out)-1):
             f.write(str(out[x])+' ')
        if len(out) !=0 :
            f.write(str(out[-1]))
                   
            
#write_columns([10.0,.1],'temp.txt')
#write_chunks_of_five(['the', 'of', 'and', 'to', 'a', 'in', 'for', 'is', 'on', 'that', 'by'],'temp.txt')
