# Tests

```Tests```는 채점 데이터를 만드는 곳입니다.  

채점 데이터를 만드는 기준은 아래와 같습니다.

- 입력값 범위의 최솟값/최댓값이 확인 가능한 데이터 만들기
- 의도하지 않은 단순한 풀이가 통과하지 않도록 저격 데이터 만들기
- 랜덤 데이터 만들기

</br>

첫 번째와 두 번째의 경우에는 직접 테스트를 만드는 것이고, 세 번째는 랜덤 데이터를 만드는 코드를 작성해야 합니다.  

</br>
</br>

## Test 제작하기
---

먼저 ```Add Test``` 버튼을 클릭합니다.  

![image](https://user-images.githubusercontent.com/79046106/204013675-d4302b87-1334-4f88-9801-5f6d538ae429.png)

- ```Test #``` : 테스트 번호입니다.
- ```Type``` : Manual (직접 데이터 제작), Script (이미 만들어진 랜덤 데이터 생성 코드 사용)
- ```Data``` : Manual을 선택시 나오는 창으로 직접 입력값을 작성합니다.
- ```Script line``` : Script를 선택시 나오는 창으로 랜덤 데이터 생성 코드를 사용하면 ```파일이름 테스트번호```로 작성하면 됩니다. (ex. ```gen 66```)
- ```Use in statements``` : 문제 예제로 공개하는 데이터인 경우 체크하면 됩니다.
- ```Description``` : 어떤 데이터인지 설명을 작성할 수 있는 곳입니다.

참고로 ```Script```는 거의 사용하지 않고, 아래처럼 사용하는 편입니다.  

</br>
</br>

## 랜덤 데이터 생성 코드 작성하기
---
```Files``` → ```Source Files```의 ```New File``` 버튼 클릭 → ```gen.cpp```처럼 랜덤 데이터 생성 코드임을 알 수 있도록 파일명을 작성한 후 ```Create File``` 버튼 클릭

이것도 ```Triathlon``` 기준으로 설명하겠습니다.
```
#include "testlib.h"			// 필수
#include <iostream>
 
using namespace std;
 
int main(int argc, char* argv[]){	// 필수
  registerGen(argc, argv, 1);		// 필수
  
  int N = rnd.next(1, 1000);		// N의 값을 1 이상 1'000 이하의 랜덤 값으로 설정합니다. 
  printf("%d\n", N);			// N을 출력합니다. 출력하지 않으면 데이터에 나오지 않습니다.
	
  for(int i=0; i<N; i++){
    int A = rnd.next(0, 10000);
    int B = rnd.next(0, 10000);
    int C = rnd.next(0, 10000);
    printf("%d %d %d\n", A, B, C);
  }
}
```

- 랜덤 트리를 만들고 싶으면 MST 알고리즘을 만들어서 랜덤 트리 데이터를 만들 수 있습니다.
- 랜덤 문자열의 경우에는 정규표현식을 입력하면 됩니다. (ex. ```rnd.next("[a-z]{2,50}")```)

파일을 다 만들었으면 스크롤을 맨 아래로 내려서 ```Script``` 창에 코드를 작성하면 됩니다.  
(현재 만든 파일을 ```max_gen.cpp```로 하면 됩니다.)  

![image](https://user-images.githubusercontent.com/79046106/204015857-ed7eab07-273a-4881-9f39-7c23f5335967.png)

이렇게 반복문 코드를 실행하여 출력문을 복사 - 붙여넣기를 해도 됩니다.  

```
int n = opt<int>(1);
int t = opt<int>(2);
```

혹은 아래 코드는 자바의 형변환 ```generator``` 코드처럼 ```n```과 ```t```를 ```Script```에 설정할 수 있게 만들어서 아래와 같이 설정할 수도 있습니다.  

![image](https://user-images.githubusercontent.com/79046106/204016353-1935e573-27fc-4bfd-a7a3-f10cd713533f.png)

이후엔 ```main solution``` 코드를 작성한 뒤에는 ```Preview Tests```를 통해 결과를 확인할 수 있습니다.  
이때 ```Validator```와 ```Checker```를 통해 입력/출력을 확인하게 됩니다.
