import os
import datetime

filename_init = 'solved.log'
# filename_current = 'trying.log'
filename_current = 'solving.log'

n_stickers_per_cell = 1 + 12 + 30 + 20 # 63
n_cells = 120

# C123mask = {1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 
#    0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 
#    0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0};

index_vertex = [7, 11, 15, 19, 21, 25, 29, 31, 35, 37, 41, 43, 47, 49, 51, 55, 57, 59, 61, 62]
index_edge = [3, 5, 6, 9, 10, 13, 14, 17, 18, 20, 23, 24, 27, 28, 30, 33, 34, 36, 39, 40, 42, 45, 46, 48, 50, 53, 54, 56, 58, 60]
index_face = [1, 2, 4, 8, 12, 16, 22, 26, 32, 38, 44, 52]
index_cell = [0]

# index_vertex = range(43, 63)
# index_edge = range(13, 43)
# index_face = range(1, 13)

index_types = [
  {'name': 'Cells', 'ind': index_cell,'nColor':1},
  {'name': 'Faces', 'ind': index_face,'nColor':2},
  {'name': 'Edges', 'ind': index_edge,'nColor':3},
  {'name': 'Verti', 'ind': index_vertex,'nColor':4}]

def read_status(filename):
  file = open(filename,'r')
  counter = 0
  status_code = ''
  for line in file:
    counter += 1
    if counter <= 12:
      continue
    status_code += line[:-1]
    if counter > 71: 
      break

  for line in file:
    timemille = line[7:]
    timedt = datetime.timedelta(milliseconds = eval(timemille))
    break
  
  file.close()
  
  status_for_cell = [status_code[i_cell * n_stickers_per_cell * 2 : (i_cell+1) * n_stickers_per_cell * 2] for i_cell in range(n_cells)]
  status = [ [ entry[i:i+2] for i in range(0, len(entry), 2)   ]        for entry in status_for_cell ]
  return (timedt, status)

def compare():
  (initTime, initStatus) = read_status (filename_init)  
  (curTime, curStatus) = read_status (filename_current)

  solved = [True] * n_stickers_per_cell
  for i in range(n_cells):
    for j in range(n_stickers_per_cell):
      if solved[j]:
        solved[j] = (initStatus[i][j] == curStatus[i][j])

  solved_indices = [i for i, x in enumerate(solved) if x]
  unsolved_indices = [i for i, x in enumerate(solved) if not x]
  return solved_indices, unsolved_indices


def main():
  (initTime, initStatus) = read_status (filename_init)  
  (curTime, curStatus) = read_status (filename_current)
  
  
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
  
# def main():
#   # (initTime, initStatus) = read_status (filename_current)
#   # print initTime
#   # print len(compare()[1])
#   print compare()[1]
#   # print [i for i in compare()[1] if i not in index_vertex]

if __name__ == '__main__':
  main()