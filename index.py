import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

def criar_dados_vendas(num_vendas=1000):
    np.random.seed(42)
    produtos = ['Produto A', 'Produto B', 'Produto C', 'Produto D']
    data = {
        'Data': pd.date_range(start='2023-01-01', periods=num_vendas, freq='D'),
        'Produto': np.random.choice(produtos, num_vendas),
        'Quantidade': np.random.randint(1, 10, num_vendas),
        'Preco': np.random.uniform(10, 100, num_vendas)
    }
    return pd.DataFrame(data)

def preparar_dados(df):
    df['Total'] = df['Quantidade'] * df['Preco']
    return df

def analise_exploratoria(df):
    print("Resumo Estatístico:")
    print(df.describe())
    
    total_por_produto = df.groupby('Produto')['Total'].sum().reset_index()
    print("\nTotal de Vendas por Produto:")
    print(total_por_produto)

def visualizar_dados(df):
    plt.figure(figsize=(10, 6))
    
    total_por_produto = df.groupby('Produto')['Total'].sum().reset_index()
    sns.barplot(x='Produto', y='Total', data=total_por_produto)
    
    plt.title('Total de Vendas por Produto')
    plt.xlabel('Produto')
    plt.ylabel('Total Vendido')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def gerar_relatorio(df):
    relatorio = df.groupby('Data').agg({'Total': 'sum'}).reset_index()
    relatorio.to_csv('relatorio_vendas.csv', index=False)
    print("\nRelatório gerado: relatorio_vendas.csv")

def main():
    df_vendas = criar_dados_vendas()
    
    df_vendas = preparar_dados(df_vendas)
    
    analise_exploratoria(df_vendas)
    
    visualizar_dados(df_vendas)
    
    gerar_relatorio(df_vendas)

if __name__ == "__main__":
    main()
