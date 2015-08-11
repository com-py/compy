# Common library file to be placed in the Python path (e.g., C:\Python27)
#
# Program: FEM mesh file I/O (fileio.py, used by qmdot.py and meshhex.py)
# J Wang, Computational modeling and visualization with Python
#
def readmesh(filename):
    node, elm, bp, ip=[], [], [], []    # nodes, elements, bndry, intrnl
    name = [node, elm, bp, ip]          # alias
    marker = [']', ']',  ',', ',']      # end of line markers
    try:
        file = open(filename,'r')             # points to a file only
    except IOError:
        print('readmesh cannot open file: %s' %filename)    # io error
        return node, elm, bp, ip
    for i in range(4):
        for each_line in file:                # 'file' remembers last position
            each_line=each_line.strip()       # strip white spaces
            if (len(each_line)==0):           # blank line, or each_line=''
                if len(name[i]) > 0: break
                continue
            elif (each_line[0] == '#'):                  # comment
                continue
                
            n = each_line.rfind(marker[i])                       
            if (i==0 or i==1):  n+=1                     # incl. ending ']'
            if (each_line.count(marker[i]) > 1):
                name[i] +=eval(each_line[:n])            # add multiple nodes
            else:
                name[i].append(eval(each_line[:n]))      # append single entry
    file.close()
    return node, elm, bp, ip

def writemesh(filename, node, elm, bp, ip):
    name = [node, elm, bp, ip]          # alias
    txt = ['nodes', 'elements', 'boundary nodes', 'internal nodes']
    n = [2, 4, 10, 10]                  # number of items per line
    try:
        file = open(filename,'w')       # note: file is overwritten
    except IOError:
        print('writemesh cannot open file: %s' %filename)   # io error
        return
        
    for i in range(4):
        file.write('\n\n# ' + txt[i] + '\n')    # comment + blank lines
        for j in range(len(name[i])):
            if (i==0):
                file.write(' [%9g, %9g], ' %(node[j][0],node[j][1]))
            else:
                file.write(' %s,' %repr(name[i][j]))
            if ((j+1)%n[i] == 0): file.write('\n')
    file.close()
