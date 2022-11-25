# Statement

문제 지문을 설정하는 페이지입니다.

![image](https://user-images.githubusercontent.com/79046106/203825369-1d9a0c3c-6caf-4dac-af44-a22b61ac3505.png)

<br/>
<br/>

## Edit with Preview
---

![image](https://user-images.githubusercontent.com/79046106/203825601-0dec659c-3db0-4858-8375-365cdd80cdba.png)

현재까지 작성한 결과물을 바로바로 확인해보며 문제를 추가 및 수정을 할 수 있습니다.

<br/>
<br/>

## Review
---

![image](https://user-images.githubusercontent.com/79046106/203825821-195ca283-faa5-4f7c-9289-b06a38cd657d.png)

문제 지문 / ```Validator``` / ```Checker```를 모두 확인할 수 있습니다.

<br/>
<br/>

## 결과물 확인
---

![image](https://user-images.githubusercontent.com/79046106/203826167-dc79a4ce-0376-4f44-a817-3896ebbaab74.png)

```In HTML```만 확인해서 들어가보면 되는데, ```Edit with Preview```랑 똑같아서 굳이 확인하지 않아도 됩니다.

<br/>
<br/>


## 문제 지문 작성하기
![image](https://user-images.githubusercontent.com/79046106/203826818-1113b7fa-dabd-4f9d-b41d-6ceb715568b0.png)

1. ```Name``` : 문제 이름
2. ```Legend``` : 문제 본문
3. ```Input format``` : 입력 제한 범위
4. ```Output format``` : 어떤 것을 출력해야 하는지에 대한 설명
5. ```Notes``` : 힌트

주의할 점: 수식이나 숫자의 경우엔 달러 표시(```$```)로 감싸주고, 안에는 LaTeX 문법을 사용해야함 ([여기서 빠르게 만들 수 있음](https://www.codecogs.com/latex/eqneditor.php))

```text
지문에 목록 적용하기 

1. 순서 없는 목록  

\begin{itemize}
  \item 내용 1
  \item 내용 2
\end{itemize}

2. 순서 있는 목록

\begin{enumerate}
  \item 내용 1
  \item 내용 2
\end{enumberate}

```

<br/>
<br/>

## 문제에 그림 추가하기
---

![image](https://user-images.githubusercontent.com/79046106/203829953-0057c9a2-f27f-4515-9afa-6092221c439b.png)

```Add Files``` → 파일 선택 → 파일들 추가 → ```Add Files```

```text

1. 바로 사용하기
\includegraphics{cpp.png}

2. 테두리 그리기
\begin{tabular}{|l|c|r|} \hline
  \includegraphics{board1.png} \\ \hline
\end{tabular}

```

