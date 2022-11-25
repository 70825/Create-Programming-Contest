# Validator

Validator는 입력 형식에 맞게 입력값이 제대로 들어오는지 확인하는 기능입니다.  
Validator는 입력, Checker는 출력이라고 생각하면 됩니다.  

![image](https://user-images.githubusercontent.com/79046106/204006042-9777bb05-1f49-42ab-ab83-03b41528385f.png)

Validator는 문제마다 입력 형식이 다르기 때문에 직접 코드를 작성해야 합니다.  
코드 파일을 이미 작성하였다면 ```파일 선택``` 버튼을 클릭하면 되고, 아니라면 ```New file``` 버튼을 클릭하여 ```validator.cpp```, ```val.cpp```와 같이 Validator임을 표시해주는 이름을 설정해주면 됩니다.  

</br>
</br>

## Validator 코드 작성
---

Validator 코드는 Triathlon을 기준으로 설명하겠습니다.

```
#include <bits/stdc++.h>
#include "testlib.h"                                               // 필수
using namespace std;
 
int main(int argc, char* argv[]) {                                 // 필수
  registerValidation(argc, argv);                                  // 필수
 
  int N = inf.readInt(1, 1000, "N");                               // N 변수에 1 이상 1'000 이하의 수가 들어오는지 확인한다.
  inf.readEoln();                                                  // 줄바꿈이 입력으로 들어와야 한다.
  ensuref(1 <= N && N <= 1000, "N must be 1 ~ 1,000 Integer");     // N의 값이 범위를 벗어나면 "N must 1 ~ 1,000 Integer"를 출력한다.
 
  for (int i = 0; i < N; i++) {
    int d = inf.readInt(0, 10000, "d");                            // d 변수에 0 이상 10'000 이하의 수가 들어오는지 확인한다.
    inf.readSpace();                                               // 공백이 입력으로 들어와야 한다.
    int g = inf.readInt(0, 10000, "g");
    inf.readSpace();
    int p = inf.readInt(0, 10000, "p");
    inf.readEoln();
 
    ensuref(0 <= d && d <= 10000, "d must be 0 ~ 10,000 Integer");
    ensuref(0 <= g && g <= 10000, "g must be 0 ~ 10,000 Integer");
    ensuref(0 <= p && p <= 10000, "p must be 0 ~ 10,000 Integer");
  }
	
  inf.readEof();                                                   // 입력값의 끝을 알린다.
  
  return 0;
}
  
```  
문자열의 경우에는 정규표현식을 사용하는 것이 좋습니다.  
다음은 자바의 형변환 문제 Validator의 일부입니다.  
```text
a = inf.readToken("[a-z]{2,50}", "s");                            // 길이가 2 ~ 50인 알파벳 소문자가 들어오는지 확인한다.
inf.readSpace();
b = inf.readToken("[a-z]{2,50}", "s");
inf.readEoln();
ensuref(a.compare(b) != 0, "duplicated name");                    // a와 b가 같으면 "duplicated name"을 출력한다.
```  

테스트를 다 작성했으면 Create 버튼을 누른 뒤, Select에서 Validator 코드를 선택하고 Set validator 버튼을 누르면 됩니다.

</br>
</br>

## Validator 테스트
---

Validator도 Checker와 마찬가지로 최대한 모든 경우의 수를 테스트하는 것이 좋습니다.  

![image](https://user-images.githubusercontent.com/79046106/204009261-b0d1e653-3fa7-4546-ac8b-ca28bd222c00.png)

Add test를 클릭하여 테스트를 생성하면 됩니다.  

![image](https://user-images.githubusercontent.com/79046106/204010050-4f395a8f-6ab3-408a-be58-24e3bc139272.png)

- Validator test # : 테스트 번호입니다.
- Use testset and group : 사용해보지 않아서 모름
- Multiple tests : 한 번에 여러 개의 테스트를 생성하는 방법입니다.  
  - ```Input(s)```에는 ```===```로 입력값을 구분하고, ```Verdicts(s)```는 줄바꿈으로 VALID/INVALID를 작성하면 됩니다.  
- Input(s) : 테스트할 입력값입니다.
- Verdicts(s) : 입력 형식이 맞는 데이터이면 ```VALID``` 혹은 ```1```을 작성하고, 틀린 데이터라면 ```INVALID``` 혹은 ```0```을 작성합니다.
