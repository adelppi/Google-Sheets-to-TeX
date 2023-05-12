import streamlit as st

st.title("スプレッドシートをTeXの表形式に変換できるマシン")

raw = st.text_area("スプレッドシートの表をここにコピペ", "", height=500)
raw = raw.split("\n")
columns = len(raw[0].split("\t"))
rows = len(raw)
raw = [" & ".join(i.split("\t")) + r" \\\\" for i in raw]
result = r"\begin{table}[h] \begin{center} \caption{表の名前} \begin{tabular}{|"\
        + "l|" * columns + "} \hline " + raw[0] + " \hline "

for i in range(1, rows):
    result += raw[i]

result = result + r" \hline \end{tabular} \end{center} \end{table}"
if st.button('TeXに変換'):
    pass
st.text("↓↓↓このテキストをコピーしてTeXファイルに貼り付ける↓↓↓")
st.write(result)
