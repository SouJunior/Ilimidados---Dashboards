import pandas as pd

# tabela alcance unificada
df_alcance1 = pd.read_csv("./tabela1/alcance.csv", encoding="utf-8", sep=",", skiprows=2)
df_alcance2 = pd.read_csv("./tabela2/alcance.csv", encoding="utf-8", sep=",", skiprows=2)
df_alcance3 = pd.read_csv("./tabela3/alcance.csv", encoding="utf-8", sep=",", skiprows=2)
df_alcance4 = pd.read_csv("./tabela4/alcance.csv", encoding="utf-8", sep=",", skiprows=2)

df_tabela_alcance = pd.concat([
    df_alcance1, 
    df_alcance2, 
    df_alcance3, 
    df_alcance4], 
    ignore_index=True)

print(df_tabela_alcance.head(40))

df_tabela_alcance.to_csv("tabela_alcance.csv", index=False, encoding="utf-8")

# tabela dados de publicação unificada
df_dados_de_publicacao1 = pd.read_csv("./tabela1/dados_de_publicacao.csv")
df_dados_de_publicacao2 = pd.read_csv("./tabela2/dados_de_publicacao.csv")
df_dados_de_publicacao4 = pd.read_csv("./tabela4/dados_de_publicacao.csv")

df_tabela_dados_de_publicacao = pd.concat([
    df_dados_de_publicacao1, 
    df_dados_de_publicacao2,  
    df_dados_de_publicacao4], 
    ignore_index=True)

print(df_tabela_dados_de_publicacao.head(20))

df_tabela_dados_de_publicacao.to_csv("tabela_dados_de_publicacao.csv", index=False, encoding="utf-8")

# tabela publico unificada
df_publico1 = pd.read_csv("./tabela1/publico.csv", encoding="utf-8", sep=";")
df_publico2 = pd.read_csv("./tabela2/publico.csv", encoding="utf-8", sep=";")
df_publico3 = pd.read_csv("./tabela3/publico.csv", encoding="utf-8", sep=";")
df_publico4 = pd.read_csv("./tabela4/publico.csv", encoding="utf-8", sep=";")

df_tabela_publico = pd.concat([
    df_publico1,
    df_publico2,
    df_publico3,
    df_publico4],
    ignore_index=True)

print(df_tabela_publico.head(40))

df_tabela_publico.to_csv("tabela_publico.csv", index=False, encoding="utf-8")

# tabela seguidores unificada
df_seguidores1 = pd.read_csv("./tabela1/seguidores.csv", encoding="utf-8", sep=";")
df_seguidores2 = pd.read_csv("./tabela2/seguidores.csv", encoding="utf-8", sep=";")
df_seguidores3 = pd.read_csv("./tabela3/seguidores.csv", encoding="utf-8", sep=";")
df_seguidores4 = pd.read_csv("./tabela4/seguidores.csv", encoding="utf-8", sep=";")

df_tabela_seguidores = pd.concat([
    df_seguidores1,
    df_seguidores2,
    df_seguidores3,
    df_seguidores4],
    ignore_index=True)

print(df_tabela_seguidores.head(50))

df_tabela_seguidores.to_csv("tabela_seguidores.csv", index=False, encoding="utf-8")

# tabela visitas
df_visitas1 = pd.read_csv("./tabela1/visitas.csv", encoding="utf-8", sep=";")
df_visitas2 = pd.read_csv("./tabela2/visitas.csv", encoding="utf-8", sep=";")
df_visitas3 = pd.read_csv("./tabela3/visitas.csv", encoding="utf-8", sep=";")
df_visitas4 = pd.read_csv("./tabela4/visitas.csv", encoding="utf-8", sep=";")

df_tabela_visitas = pd.concat([
    df_visitas1,
    df_visitas2,
    df_visitas3,
    df_visitas4],
    ignore_index=True)

print(df_tabela_visitas.head(50))

df_tabela_visitas.to_csv("tabela_visitas.csv", index=False, encoding="utf-8")

