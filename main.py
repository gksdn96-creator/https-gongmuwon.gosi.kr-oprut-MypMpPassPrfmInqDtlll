import streamlit as st

st.set_page_config(
    page_title="시험성적 조회 - 모의 화면",
    page_icon="📋",
    layout="wide"
)

# CSS
st.markdown("""
<style>
.demo-banner {
    background-color: #fff3cd;
    border: 1px solid #ffe69c;
    color: #664d03;
    padding: 12px 16px;
    border-radius: 5px;
    margin-bottom: 22px;
    font-weight: 700;
    text-align: center;
}

.section-title {
    font-size: 20px;
    font-weight: 700;
    margin-top: 20px;
    margin-bottom: 12px;
}

.result-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 17px;
}

.result-table th {
    background-color: #eef3f7;
    border-top: 2px solid #1d5da8;
    border-bottom: 1px solid #b9cde3;
    padding: 12px;
    text-align: center;
    color: #222;
}

.result-table td {
    border-bottom: 1px solid #c8d7e6;
    padding: 13px;
    text-align: center;
    color: #222;
}

.fail {
    color: #c62828 !important;
    font-weight: 700;
}

.minus {
    color: #555 !important;
}

.notice {
    margin-top: 25px;
    padding: 12px;
    background-color: #f5f5f5;
    border-radius: 5px;
    color: #555;
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)


# 모의 화면 안내
st.markdown("""
<div class="demo-banner">
    모의 화면 · 실제 공무원 시험 성적조회 시스템이 아니며 공식 성적을 나타내지 않습니다.
</div>
""", unsafe_allow_html=True)


# 합격여부
st.markdown(
    '<div class="section-title">합격여부</div>',
    unsafe_allow_html=True
)

st.markdown("""
<table class="result-table">
    <thead>
        <tr>
            <th style="width:10%;">차수</th>
            <th style="width:30%;">시험</th>
            <th style="width:30%;">합격여부</th>
            <th style="width:30%;">성적</th>
        </tr>
    </thead>

    <tbody>
        <tr>
            <td rowspan="3"><b>차수</b></td>
            <td>1차 시험</td>
            <td>합격</td>
            <td>
                <button style="
                    background:#06458f;
                    color:white;
                    border:none;
                    border-radius:4px;
                    padding:9px 27px;
                    font-weight:bold;
                ">
                    성적보기
                </button>
            </td>
        </tr>

        <tr>
            <td>2차 시험</td>
            <td class="fail">불합격</td>
            <td>
                <button style="
                    background:#06458f;
                    color:white;
                    border:none;
                    border-radius:4px;
                    padding:9px 27px;
                    font-weight:bold;
                ">
                    성적보기
                </button>
            </td>
        </tr>

        <tr>
            <td>3차 시험</td>
            <td class="minus">-</td>
            <td class="minus">-</td>
        </tr>
    </tbody>
</table>
""", unsafe_allow_html=True)


# 2차 시험 상세 성적
st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">＋　2차시험성적 상세보기</div>',
    unsafe_allow_html=True
)

st.markdown("""
<table class="result-table">
    <thead>
        <tr>
            <th style="width:70%;">과목명</th>
            <th style="width:30%;">점수</th>
        </tr>
    </thead>

    <tbody>
        <tr>
            <td>화학개론</td>
            <td>92.00</td>
        </tr>

        <tr>
            <td>화공열역학</td>
            <td>81.00</td>
        </tr>

        <tr>
            <td>전달현상</td>
            <td>76.00</td>
        </tr>

        <tr>
            <td>반응공학</td>
            <td>84.00</td>
        </tr>

        <tr>
            <td>평균</td>
            <td>83.25</td>
        </tr>

        <tr>
            <td>합격선</td>
            <td>88.00</td>
        </tr>
    </tbody>
</table>
""", unsafe_allow_html=True)


# 안내
st.markdown("""
<div class="notice">
    ※ 본 페이지는 UI 테스트 및 개인 학습을 위한 모의 화면입니다.
    실제 시험 결과 또는 공공기관의 공식 성적을 표시하지 않습니다.
</div>
""", unsafe_allow_html=True)
