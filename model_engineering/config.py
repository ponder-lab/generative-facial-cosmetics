########## Configs ##########

###### Imports ######

###### Constants ###### 
CURRENT_OS = 'Windows'                # manually change this field every time before deploying (maybe at gdrive)

if CURRENT_OS.lower()[0] == 'w':
  DIR = '.'
elif CURRENT_OS.lower()[0] == 'c':
  DIR = 'drive/My Drive/Live Workspace/generative-facial-cosmetics/dataset_engineering/'
else:
  raise NotImplementedError('OS is not supported yet')

###### Functions ######
def isWindows():
  return bool(CURRENT_OS.lower()[0] == 'w')
def isColab():
  return bool(CURRENT_OS.lower()[0] == 'c')

###### Execution ######