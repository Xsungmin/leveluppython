#  15650  N과 M (2)

## 문제 

자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

- 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
- 고른 수열은 오름차순이어야 한다.

## 입력

첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

## 출력

- 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

- 수열은 사전 순으로 증가하는 순서로 출력해야 한다.

## 목표 
재귀와 백트래킹의 활용

### 개인 : ksm
#### 한것

15649를 이용해 수정해보고자 했다. 정렬해서 같은것만 빼면 빠르게 풀릴거라 생각했다.
하지만 리스트 카피부터 문제가 생겨서 deepcopy를 위해 import 까지 사용하게 되었다 &
sort를 함으로써 앞의 함수에 변화를 야기했고 deepcopy를 두번이나 사용하게 되었다.

#### 보완할점

전 함수를 보완하는것 보다는 새 함수를 처음부터 짜는게 낫지않을까 생각했다.
교수님이 말했던것처럼 덧대는 코딩이 안좋다는 의미를 다시한번 되새기게 되었다.


### 개인 : juhye
#### 한것
이전의 순열 코드를 활용해서 dfs, 백트래킹을 이용해 구현해보고자 했다. 

#### 보완할점
아직도 dfs, 백트래킹에 대한 이해가 부족하다고 느꼈다. 이전에 배운 코드를 활용해 작성하는 것에는 한계가 있다는 점을 또 다시 깨닫게 되었다. 새로 발전된 문제가 나와도 풀 수 있게끔 알고리즘 원리에 대한 깊이있는 이해가 필요하다는 것을 절실히 깨달았다.

### 개인 :lgh
#### 한것
N과 M(1) 번과 유사한 문제라고 생각하여 비슷하게 방법을 떠올려 생각해봄.
(1)번과는 달리 (2)번은 중복 없이 M개를 고른 수열임과 동시에 고른 수열은 오름차순이어야 한다. 그렇다는 말은 (1, 2), (2, 1)와 같은 중복을 없앰과 동시에 오름차순으로 해결해야 한다고 생각.
(1)번 코드와 비슷하게 구상을 하면 되겠다라고 생각했는데, 이해를 잘 하지 못한상태에서 끼워맞추다가 맞춘 문제..

방법

 visited 배열을 사용해, 중복 값을 사용 못하게 한 상태에서 for문을 통해 증가시키는 방식. 저장 된 배열이 문제에서 주어진 길이만큼이 된다면 리턴을 하게되고, 종료조건에 마지막 값을 pop해줌으로써 그 다음 숫자가 들어갈 수 있게 해준다.

초기 호출 시 dfs(0, 0) -> 인자 2개 사용
def dfs(cnt, next_i) -> (최종 출력 될 배열의 개수를 셀 매개변수, result[0]보다 큰 범위부터 시작할 수 있게 할 매개변수) 를 통해 호출하여 이후 for i in range(next_i, N): 을 통해 중복 순열을 방지 해준다.



#### 보완할점
큰 틀을 보는게 아닌 재귀의 한 부분을 보고 코드를 짤 줄 알아야 된다고 생각은 하지만 아직 그 방법에 익숙치가 않아 많은 실수를 하게 된다. 재귀의 호출부분과 재귀가 종료 됐을 때, 그 둘의 구분에 대해 더 공부해서 알고리즘으로 구현을 할 때 버벅임 없도록 해야겠다. 