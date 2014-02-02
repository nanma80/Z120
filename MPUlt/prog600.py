import os
import datetime

filenameInit = '600cell_init.log'
filenameCurrent = '600cell_solving.log'
# filenameCurrent = '600cell_test.log'

nStickersPerCell = 1+4+6+4 # for the 600-cell
nCells = 600
indVertex = [7,11,13,14]
indEdge =[4,5,6,9,10,12]
indFace =[1,2,3,8]
indCell=[0]
indTypes = [{'name': 'Cells', 'ind': indCell,'nColor':1},{'name': 'Faces', 'ind': indFace,'nColor':2},{'name': 'Edges', 'ind': indEdge,'nColor':5},{'name': 'Verti', 'ind': indVertex,'nColor':20}]


def readStatus(filename):
  file = open(filename,'r')
  counter = 0
  statusCode = ''
  for line in file:
    counter += 1
    if counter<=13:
      continue
    statusCode += line[:-1]
    if counter >83: 
      break
  
  for line in file:
    timemille = line[7:]
    timedt = datetime.timedelta(milliseconds = eval(timemille))
    break
  
  file.close()
  
  statusForCell = [statusCode[indexCell * nStickersPerCell * 2 : (indexCell+1) * nStickersPerCell * 2] for indexCell in range(0, nCells)]
  status = [ [ entry[i:i+2] for i in range(0,len(entry),2)   ]        for entry in statusForCell ]
  
  return (timedt, status)

def main():
  (initTime, initStatus) = readStatus (filenameInit)  
  (curTime, curStatus) = readStatus (filenameCurrent)
  
  
  progressVector = []
  for i in range(0, nStickersPerCell):
    progressVector.append(0)
  
  completedType = {}
  for type in indTypes:
    completedType[type['name']] = 0
  
  
  for i in range(0,nCells):
    for j in range(0,nStickersPerCell):
      if initStatus[i][j] == curStatus[i][j]:
        progressVector [j] += 1
        # if (j in [1,2,3,8]):
          # print i, j, initStatus[i][0]
    for type in indTypes:
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
  
  for type in indTypes:
    totalSolvedSticker = sum([progressVector[i] for i in type['ind']])
    totalSticker = nCells * len(type['ind'])
    totalSolvedPiece = totalSolvedSticker/type['nColor']
    totalPiece = totalSticker/type['nColor']
    
    percentage = 100.0 * totalSolvedPiece / totalPiece
    
    print type['name']+': \t%4d/%4d, \t%4d/%4d, \t%6.2f'%(totalSolvedPiece, totalPiece, totalSolvedSticker,totalSticker,percentage)+'%, '+('\t%3d/%3d'%(completedType[type['name']],nCells))
    
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
  
  
  
if __name__ == '__main__':
  main()