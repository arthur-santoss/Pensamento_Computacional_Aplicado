import traceback

try:
  nome_arquivo = input('Nome do arquivo: ').strip()
  arquivo = open(nome_arquivo)
except:
  traceLog = traceback.format_exc()
  print("Erro que aconteceu: ", traceLog)
  open("traceLog.log", 'a').write(traceLog)