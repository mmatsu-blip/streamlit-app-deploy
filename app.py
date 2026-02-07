import streamlit as st

<<<<<<< HEAD
st.title("サンプルアプリ②: 少し複雑なWebアプリ")

st.write("##### 動作モード1: 文字数カウント")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことで文字数をカウントできます。")
st.write("##### 動作モード2: BMI値の計算")
st.write("身長と体重を入力することで、肥満度を表す体型指数のBMI値を算出できます。")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["文字数カウント", "BMI値の計算"]
)

st.divider()

if selected_item == "文字数カウント":
    input_message = st.text_input(label="文字数のカウント対象となるテキストを入力してください。")
    text_count = len(input_message)

else:
    height = st.text_input(label="身長（cm）を入力してください。")
    weight = st.text_input(label="体重（kg）を入力してください。")

if st.button("実行"):
    st.divider()

    if selected_item == "文字数カウント":
        if input_message:
            st.write(f"文字数: **{text_count}**")

        else:
            st.error("カウント対象となるテキストを入力してから「実行」ボタンを押してください。")

    else:
        if height and weight:
            try:
                bmi = round(int(weight) / ((int(height)/100) ** 2), 1)
                st.write(f"BMI値: {bmi}")

            except ValueError as e:
                st.error("身長と体重は数値で入力してください。")

        else:
            st.error("身長と体重をどちらも入力してください。")   
=======
st.title("LLMアプリ")
st.write("Hello Streamlit")

from dotenv import load_dotenv

load_dotenv()

import streamlit as st
from dotenv import load_dotenv
import os
from openai import OpenAI

# .env を読み込む
load_dotenv()

# APIキー取得
api_key = os.getenv("OPENAI_API_KEY")

st.title("LLMアプリ テスト")

if not api_key:
    st.error("OPENAI_API_KEY が読み込めていません")
else:
    st.success("APIキーを読み込みました")

    if st.button("LLMに質問する"):
        client = OpenAI(api_key=api_key)

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": "こんにちは。あなたは誰ですか？"}
            ]
        )

        st.write(response.choices[0].message.content)
