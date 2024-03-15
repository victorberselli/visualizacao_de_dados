import pandas as pd
import streamlit as st
import altair as alt

arq1 = './data/campeonato-brasileiro-gols.csv'
arq2 = './data/campeonato-brasileiro-full.csv'
df1 = pd.read_csv(arq1)
df2 = pd.read_csv(arq2)

df1.rename(columns={'partida_id': 'ID'}, inplace = True)
df_campeonato = pd.merge(df1, df2, how='inner', on='ID')

atleta = df_campeonato['atleta'].value_counts().index.sort_values(ascending=True)
atlet = st.sidebar.selectbox("Atleta", atleta)
df_goleador=df_campeonato[df_campeonato["atleta"] == atlet]

df_goleador_formatado=df_goleador.reindex(columns=['clube', 'atleta', 'minuto','tipo_de_gol','data','mandante','visitante','formacao_mandante', 
                                                   'formacao_visitante', 'tecnico_mandante', 'tecnico_visitante', 'vencedor', 'arena', 'mandante_Placar', 'visitante_Placar'])

c=alt.Chart(df_goleador_formatado).mark_bar(interpolate='monotone').encode(
   x='data',
   y='minuto',
   color='clube',
   tooltip = [alt.Tooltip('data'),
               alt.Tooltip('minuto'),
               alt.Tooltip('clube'),
               alt.Tooltip('tipo_de_gol'),
               ]
   ).interactive()

st.title('Gols no Campeonato Brasileiro')
#st.write(df_campeonato)
st.dataframe(df_goleador_formatado, use_container_width=True)
st.altair_chart(c, use_container_width=True)
st.sidebar.markdown('##### Desenvolvido por [Victor A. Berselli](https://www.linkedin.com/in/victorberselli/)')