import logging
from inspect import stack
import time
import datetime
import pandas as pd
import textract


def convert_to_text(identifier):
  this_function_name = stack()[0][3]
  start = time.time()
  starts = datetime.time().strftime('%s')
  logging.basicConfig(filename='../tests/'+identifier+'-convert_to_text.log', encoding='utf-8', level=logging.DEBUG)

  logging.info("function "+this_function_name+" start")
  logging.debug("function "+this_function_name+" invoked")
  logging.debug("called by "+stack()[1][3])
  logging.debug("function start time: "+starts)
  
  ####################################################################################
  data = []
  data_out = []
  
  
  df = pd.DataFrame(data, columns = ['fname', 'ftype'])
  df = pd.read_csv('../tests/'+identifier+'-file_reader.csv', index_col=0, encoding='utf-8')

  df_out = pd.DataFrame(data_out, columns = ['fname', 'text'])

  for row in df.iterrows():
    print(row[1].ftype)
    text = textract.process(row[1].fname, encoding='utf-8')
    text = str(text).replace('\\n','')
    text = str(text).replace('\n',' ')
    text = str(text).replace('\r',' ')
    text = str(text).replace(' | ',' ')

    print(text)
    data_out.append(pd.DataFrame({"fname": [str(row[1].fname)], "text": [text]}))
  
  df_out = pd.concat(data_out).reset_index(drop=True)
  df_out.to_csv('../tests/'+identifier+'-file_text.csv')          

  ####################################################################################
  end = time.time()
  ends = datetime.time().strftime('%s')
  elapsed_time = (end - start)
  

  print(elapsed_time)
  logging.info("function "+this_function_name+" end")
  logging.debug("function end time: "+ends)
  logging.debug(elapsed_time)


  return "test"
  
print(convert_to_text('local_files_source'))