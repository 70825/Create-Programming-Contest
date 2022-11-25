# Checker

Checker는 입력값을 통해 얻은 정답과 실제 정답을 비교하는 기능입니다.  

Checker는 코드를 직접 작성하여 만들 수도 있지만, 보통 기본으로 제공되는 Checker 코드를 사용하는 편입니다.  

Checker는 모든 경우에 대해서 확인을 해야 하기 때문에 다양한 테스트 값이 있는 것이 좋습니다.
- 예상 답과 실제 답이 다른 경우
- 예상 답과 실제 답의 길이가 다른 경우
- 예상 답의 개수와 실제 답의 개수가 다른 경우

<br/>
<br/>

## 자주 사용하는 Checker
---

![image](https://user-images.githubusercontent.com/79046106/203928804-a65cb590-26c1-42ae-a64c-844d686c601f.png)

- hcmp.cpp : 답이 하나의 숫자인 경우 사용합니다. (ex. Triathlon)
- wcmp.cpp : 답이 여러 개의 숫자를 표현할 때 사용합니다. (ex. 비행기 전시, 장마)
- fcmp.cpp : 문자열 양 끝에 있는 공백까지 포함하여 정답과 완전히 일치하는지 확인합니다. (ex. ' 15' != '15')
- lcmp.cpp : 문자열 양 끝에 있는 공백은 무시하고 비교하여 정답과 완전히 일치하는지 확인합니다. (ex. ' 15' == '15')
- yesno.cpp : yes, YES, yEs와 같이 모두 대문자로 변환시 YES로 인정하고, no, No, nO와 같이 모두 대문자로 변환시 NO로 인정하여 답이 YES 혹은 NO인지 확인합니다.

<br/>
<br/>

## Checker Test
---
![image](https://user-images.githubusercontent.com/79046106/203929715-f5ad7344-094d-4fdc-96ff-600c240968ad.png)

Add Test 클릭

![image](https://user-images.githubusercontent.com/79046106/203929830-2ed0543d-08f1-40f7-957e-9d97252c3591.png)

- Checker test # : 테스트 번호로 자동으로 번호가 생성됩니다.
- Input : 예상 입력값을 작성하면 됩니다.
- Output : 예상 입력값에 대한 정답을 작성하면 됩니다.
- Answer : 예상 입력값에 대한 실제 정답을 작성하면 됩니다.
- Verdict : OK (정답), WRONG ANSWER (오답)

<br/>
<br/>

![image](https://user-images.githubusercontent.com/79046106/203931038-1ffea430-44aa-43ea-adca-82a25d4b3a2e.png)

데이터가 생성되고 확인을 하고 싶다면 Run tests를 클릭하면 됩니다.  
이후 새로고침을 하면 테스트 결과를 알 수 있습니다.  
예상한 값과 틀린 데이터가 나오면 빨간색으로 표시가 되고, 에러가 나오는 이유는 Checker comment에서 확인이 가능합니다.
