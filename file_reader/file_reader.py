import logging
from inspect import stack
import time
import datetime
import pathlib
import filetype
import pandas


def file_reader_dir(identifier, source):
  
  this_function_name = stack()[0][3]
  start = time.time()
  starts = datetime.time().strftime('%s')
  logging.basicConfig(filename='../tests/'+identifier+'-file_reader.log', encoding='utf-8', level=logging.DEBUG)

  logging.info("function "+this_function_name+" start")
  logging.debug("function "+this_function_name+" invoked")
  logging.debug("called by "+stack()[1][3])
  logging.debug("function start time: "+starts)
  
  ####################################################################################
  # https://realpython.com/get-all-files-in-directory-python/
  
  data = []
  source_path = pathlib.Path(source)
  logging.debug(source_path)
  df = pandas.DataFrame(data, columns = ['fname', 'ftype'])

  for source_file in source_path.rglob('*'):
    if source_file.is_file():
      kind = filetype.guess(source_file)
      match kind:
        case None: 
          logging.info(str(source_file)+" unsupported")
          suffix = (str(pathlib.Path(source_file).suffix))
          match suffix:
            case ".html": 
              res_type = ('text/html')
            case ".txt":
              res_type = ('text/plain')
            case _:
              logging.info(str(source_file)+" unsupported")
        case _: 
          logging.debug(str(source_file)+" "+kind.mime)
          res_type = kind.mime
          
    data.append(pandas.DataFrame({"fname": [str(source_file)], "ftype": [res_type]}))
  
  df = pandas.concat(data).reset_index(drop=True)
  df.to_csv('../tests/'+identifier+'-file_reader.csv')          
  
  ####################################################################################
  end = time.time()
  ends = datetime.time().strftime('%s')
  elapsed_time = (end - start)
  

  #print(elapsed_time)
  logging.info("function "+this_function_name+" end")
  logging.debug("function end time: "+ends)
  logging.debug(elapsed_time)


  return df
  
print(file_reader_dir('local_files_source','../tests/source_files/'))