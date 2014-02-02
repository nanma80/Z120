import os
import datetime

filename_init = 'solved.log'
filename_current = 'scrambled.log'

n_stickers_per_cell = 1 + 12 + 30 + 20 # 63
n_cells = 120

# C123mask = {1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 
#    0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 
#    0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0};

index_vertex = [7,11,13,14]
index_edge = [4,5,6,9,10,12]
index_face = [1,2,3,8]
index_cell = [0]
index_types = [{'name': 'Cells', 'ind': index_cell,'nColor':1},{'name': 'Faces', 'ind': index_face,'nColor':2},{'name': 'Edges', 'ind': index_edge,'nColor':5},{'name': 'Verti', 'ind': index_vertex,'nColor':20}]


def readStatus(filename):
  file = open(filename,'r')
  counter = 0
  status_code = ''
  for line in file:
    counter += 1
    if counter <= 13:
      continue
    status_code += line[:-1]
    if counter > 71: 
      break

  for line in file:
    timemille = line[7:]
    timedt = datetime.timedelta(milliseconds = eval(timemille))
    break
  
  file.close()
  
  status_for_cell = [status_code[index_cell * n_stickers_per_cell * 2 : (index_cell+1) * n_stickers_per_cell * 2] for index_cell in range(0, n_cells)]
  status = [ [ entry[i:i+2] for i in range(0,len(entry),2)   ]        for entry in status_for_cell ]
  
  return (timedt, status)

def main_old():
  (initTime, initStatus) = readStatus (filename_init)  
  (curTime, curStatus) = readStatus (filename_current)
  
  
  progressVector = []
  for i in range(0, n_stickers_per_cell):
    progressVector.append(0)
  
  completedType = {}
  for type in index_types:
    completedType[type['name']] = 0
  
  
  for i in range(0,n_cells):
    for j in range(0,n_stickers_per_cell):
      if initStatus[i][j] == curStatus[i][j]:
        progressVector [j] += 1
        # if (j in [1,2,3,8]):
          # print i, j, initStatus[i][0]
    for type in index_types:
      flag = True
      for j in type['ind']:
        if initStatus[i][j] != curStatus[i][j]:
          flag = False
          break
      if flag:
        completedType [type['name']] += 1
          
        
  print '----------------------------------------------------------------------------'
  print 'Type \tSolved Pieces\tSolved Stickers\tPercentage\tCompleted Cells'
  print '----------------------------------------------------------------------------'
  
  for type in index_types:
    totalSolvedSticker = sum([progressVector[i] for i in type['ind']])
    totalSticker = n_cells * len(type['ind'])
    totalSolvedPiece = totalSolvedSticker/type['nColor']
    totalPiece = totalSticker/type['nColor']
    
    percentage = 100.0 * totalSolvedPiece / totalPiece
    
    print type['name']+': \t%4d/%4d, \t%4d/%4d, \t%6.2f'%(totalSolvedPiece, totalPiece, totalSolvedSticker,totalSticker,percentage)+'%, '+('\t%3d/%3d'%(completedType[type['name']],n_cells))
    
  print '----------------------------------------------------------------------------'
  hours = curTime.seconds/3600
  totalhours = curTime.days * 24 + hours
  minutes = (curTime.seconds%3600)/60
  minutesStr = str(100 + minutes)[1:]
  seconds = curTime.seconds%60
  secondsStr = str(100 + seconds)[1:]
  milliseconds = curTime.microseconds/1000
  millisecondsStr = str(1000 + milliseconds)[1:]
  print ('Current solving time is: %d:%s:%s.%s,   %s'%(totalhours, minutesStr, secondsStr, millisecondsStr,str(curTime)[:-3]))
  
def main():
  (initTime, initStatus) = readStatus (filename_init)
  print initTime

if __name__ == '__main__':
  main()