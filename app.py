import streamlit as st
import pandas as pd

bank_data=pd.DataFrame({
    '은행':['국민은행','국민은행','국민은행','국민은행','국민은행','국민은행',
            '신한은행','신한은행','신한은행','신한은행','신한은행','신한은행',
            '하나은행','하나은행','하나은행','하나은행','하나은행','하나은행',
            '우리은행','우리은행','우리은행','우리은행','우리은행','우리은행'],
    '적금':['온국민 건강적금-골든라이프','청년도약계좌','특한적금','국민행복적금','미소드림적금','장병내일준비적금',
          '패밀리상생적금','신한SK LPG쏠쏠한 행복적금','청년도약계좌','군인행복적금','연금저축왕적금','쓸수록모이는 소비적금',
        '아이키움적금','청년도약계좌','급여하나 월복리 적금','트래블로그 여행 적금','도전365적금','주거래하나적금',
        '데일리워킹적금','N일적금','우리퍼스트 정기적금','Super주거래 정기적금','우리 으쓱 적금','첫급여 우리적금'],
    '기간(개월수)':[6,12,12,12,24,24,
               12,12,12,24,24,12,
               12,6,12,24,6,12,
               12,24,24,24,24,12],
    '최고금리(%)':[11,6,3,2.6,8,13,
            11,12,7,8.7,6.2,3,
            2,2.5,9,10,3.4,2.5,
            2.2,2.4,5,6,6.7,8],
    '기본금리(%)':[4,2,3,2.5,2.1,3,
               2,2.3,2.1,3,3,2,
               2,2.4,3.1,3,2.6,2,
               2.1,2.1,2.3,4,3.1,2.2]                       
})

st.title('원하는 조건의 적금을 찾아보세요!')

selected_bank = st.multiselect('은행을 선택하시오:', bank_data['은행'].unique())
selected_duration = st.multiselect('기간(개월수)를 선택하시오:', bank_data['기간(개월수)'].unique())
selected_best = st.multiselect('최고금리(%)를 선택하시오:', bank_data['최고금리(%)'].unique())

if selected_best:
    selected_bank = bank_data[bank_data['은행'].isin(selected_bank)]
    selected_duration= selected_bank[selected_bank['기간(개월수)'].isin(selected_duration)]
    selected_best=selected_duration[selected_duration['최고금리(%)'].isin(selected_best)]
    st.write(selected_best) 
