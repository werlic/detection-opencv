import os
import sys, getopt

def generate_negative_description_file(dir: str):
  if dir[len(dir) - 1] == '/':
      dir = dir[:-1]

  dir = dir
  # open the output file for writing. will overwrite all existing data in there
  output, _ = os.path.split(dir)
  with open(os.path.join(output + '/', 'negative.txt'), 'w') as f:
    # loop over all the filenames
    for filename in os.listdir(dir):
      f.write(dir + '/' + filename + '\n')

if __name__ == '__main__':
  directory = ''
  argv = sys.argv[1:]
  try:
    opts, args = getopt.getopt(argv, 'h:d:', ['directory='])
  except getopt.GetoptError:
    print('Invalid argument')
    print('Example command :')
    print('python generate_description.py -d <path_to_folder>')
  
  for opt, arg in opts:
    if opt == 'h':
      print('python generate_description.py -d <path_to_folder>')
      sys.exit()
    elif opt in ('-d', '--directory'):
      directory = arg
  
  if len(directory) == 0: 
    assert "Directory not set!!"

  generate_negative_description_file(directory)
