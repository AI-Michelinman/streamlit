import pandas as pd
import streamlit as st
import streamlit.components.v1 as stc
import yfinance as yf

 
st.sidebar.button('Reload')
st.title('Tatsuro note')


def main():
         
    col1, col2, col3 = st.columns(3)

    with col1:
        agree = st.checkbox('投資関連')
        if agree == True :
            st.write('こんにちわ!')
            st.header('自動車関連株式（工事中）’)
            st.sidebar.markdown("## Settings")   
            stc.html('<div class="flourish-embed flourish-bar-chart-race" data-src="visualisation/8529391"><script src="https://public.flourish.studio/resources/embed.js"></script></div>',height=500)

            selected_len = st.sidebar.radio('期間',
                                    ['1ヶ月','1年','当会計年度','全てのデータ'])
            if selected_len == '1ヶ月':
                selected_len = '1mo'
            elif selected_len == '1年':
                selected_len = '1y'
            elif selected_len == '当会計年度':
                selected_len = 'ytd'
            elif selected_len == '全てのデータ':
                selected_len = 'max'
                
            selected_interval = st.sidebar.radio('時間足',
                                    ['1日','5日','1週間','1ヶ月', '3ヶ月'])
            if selected_interval == '1日':
                selected_interval = '1d'
            elif selected_interval == '5日':
                selected_interval = '5d'
            elif selected_interval == '1週間':
                selected_interval = '1wk'
            elif selected_interval == '1ヶ月':
                selected_interval = '1mo'
            elif selected_interval == '3ヶ月':
                selected_interval = '3mo'
                
                
            df = pd.DataFrame(yf.download(['7203.T','7201.T','7261.T','7267.T','7270.T','7269.T','7211.T',
                                                '5108.T','5101.T','5110.T','5105.T'], period=selected_len, interval = selected_interval)["Close"])
            df.columns = ['TOYOTA','日産','マツダ','ホンダ','スバル','スズキ','三菱',
                                'BS','横浜ゴム','住友ゴム','TOYO TIRE']

            st.subheader('銘柄')

            all = st.checkbox("Select all")
            
            if all:
                selected_options = st.sidebar.multiselect('自動車メーカー', 
                    sorted(df.columns),sorted(df.columns))
            else:
                selected_options =  st.sidebar.multiselect('自動車メーカー', 
                    sorted(df.columns))
            view_motor = df[selected_options]
            st.line_chart(view_motor,width=1000)

    with col2:
        st.header("お天気")

    with col3:
        st.header("勉強")
if __name__ == '__main__':
    main()
