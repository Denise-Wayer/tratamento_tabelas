import pandas as pd
import plotly.express as px

def importaDados(): 
    tabela = pd.read_csv("telecom_users.csv") #irá buscar a tabela e importar ela
    trataTabela(tabela) #chama a função de tratamento  e sobrescreve a variavel com a tabela já tratada
       
def trataTabela(tabela): 
    tabela = tabela.drop("IDCliente",axis=1) #irá exluir a coluna do id que nao será util
    tabela = tabela.drop("unnamed",axis=1) #irá excluir a coluna unnamed que também não será util
    tabela = tabela.dropna(how="all", axis = 1)#irá eliminar todas as colunas e linhas em que há campos em branco(NaN)
    tabela = tabela.dropna(how="any", axis = 0)#irá eliminar todas as colunas e linhas em que há campos em branco(NaN)
    global tabelaPronta    
    tabelaPronta=tabela    
        
def imprimeGraficos(tabelaPronta):
    print(tabelaPronta)
    for coluna in tabelaPronta.columns: #irá exibir diversos gráficos, levando em conta todas as colunas existentes
        grafico = px.histogram(tabelaPronta, x=coluna, color="Churn")#gera os graficos sempre levando para a comparação a coluna churn, enquanto houverem colunas a serem comparadas
        grafico.show()#imprime o gráfico  
    #grafico = px.histogram(tabelaPronta, x="Genero", color="Churn") #esta sintaxe, fora do for, gera os graficos sempre levando para a comparação a coluna churn e mais uma estipulada no x
  
importaDados()
imprimeGraficos(tabelaPronta)