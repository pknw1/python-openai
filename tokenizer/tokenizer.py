import logging
from inspect import stack
import time
import datetime
import pandas as pd
import textract
import tiktoken


def tokenize(identifier):
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
  
  
  tokenizer = tiktoken.get_encoding("cl100k_base")

# Tokenize the text and save the number of tokens to a new column

# Visualize the distribution of the number of tokens per row using a histogram
  df = pd.DataFrame(data, columns = ['fname', 'text', 'sentences', 'ntokens'])
  df = pd.read_csv('../tests/'+identifier+'-file_text.csv', index_col=0, encoding='utf-8')
  df.head()
  print(f"{len(df)} rows in the data.")
  
  df.columns = ['fname', 'text']
  df_out = pd.DataFrame(data_out, columns = ['fname', 'text', 'sentences', 'n_tokens'])

  for row in df.iterrows():
    print(row[1].fname)
    sentences = row[1].text.split('.')
    print(len(sentences))
    for sentence in sentences:
      gen_tokens = len(tokenizer.encode(sentence))
      print(gen_tokens)
      
    tokens = tokenizer.encode(row[1].text)
    print(len(tokens))
    data_out.append(pd.DataFrame({"fname": [str(row[1].fname)], "text": [row[1].text], "sdentences": [len(sentences)], "n_tokens": [len(tokens)]}))

  df_out = pd.concat(data_out).reset_index(drop=True)
  df_out.to_csv('../tests/'+identifier+'-file_tokens.csv') 
  #df['n_tokens'] = df.text.apply(lambda x: len(tokenizer.encode(x)))
  #df.n_tokens.hist()
  #print(df.n_tokens.hist())
  
  #data_out.append(pd.DataFrame({"fname": [str(row[1].fname)], "text": [text]}))
  
  #         

  ####################################################################################
  end = time.time()
  ends = datetime.time().strftime('%s')
  elapsed_time = (end - start)
  

  print(elapsed_time)
  logging.info("function "+this_function_name+" end")
  logging.debug("function end time: "+ends)
  logging.debug(elapsed_time)


  return "test"
  
print(tokenize('local_files_source'))