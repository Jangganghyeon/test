import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta

# 글로벌 시가총액 Top 10 (2025년 기준 추정)
top_10_companies = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Saudi Aramco": "2222.SR",
    "Alphabet (Google)": "GOOGL",
    "Amazon": "AMZN",
    "Nvidia": "NVDA",
    "Berkshire Hathaway": "BRK-B",
    "Meta Platforms": "META",
    "TSMC": "TSM",
    "Eli Lilly": "LLY"
}

st.title("📈 글로벌 시가총액 Top 10 기업 주가 변화 (최근 1년)")

# 날짜 설정
end_date = datetime.today()
start_date = end_date - timedelta(days=365)

# Plotly 그래프 객체
fig = go.Figure()

for name, ticker in top_10_companies.items():
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        if not data.empty:
            fig.add_trace(go.Scatter(
                x=data.index,
                y=data['Adj Close'],
                mode='lines',
                name=name
            ))
    except Exception as e:
        st.warning(f"{name} 데이터 로딩 실패: {e}")

fig.update_layout(
    title="Top 10 Global Companies - Stock Price (Last 1 Year)",
    xaxis_title="Date",
    yaxis_title="Stock Price (Adjusted Close)",
    template="plotly_dark",
    hovermode="x unified"
)

st.plotly_chart(fig, use_container_width=True)
