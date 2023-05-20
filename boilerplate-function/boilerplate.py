import logging
from inspect import stack
import time
import datetime

def boilerplate():
  this_function_name = stack()[0][3]
  start = time.time()
  starts = datetime.time().strftime('%s')
  logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

  logging.info("function "+this_function_name+" start")
  logging.debug("function "+this_function_name+" invoked")
  logging.debug("called by "+stack()[1][3])
  logging.debug("function start time: "+starts)
  
  ####################################################################################
  

  
  
  ####################################################################################
  end = time.time()
  ends = datetime.time().strftime('%s')
  elapsed_time = (end - start)
  

  print(elapsed_time)
  logging.info("function "+this_function_name+" end")
  logging.debug("function end time: "+ends)
  logging.debug(elapsed_time)


  return "test"
  
boilerplate()