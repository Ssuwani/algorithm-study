

<div align="center">
    <h1>
        Algorithm Study
    </h1>
    <img src='logo.png'/ width='20%'>
</div>



우연히 알게된 [coding-test-study](https://github.com/boostcamp-ai-tech-4/coding-test-study)를 참고하여 페이지를 구성하셨습니다!! 또한 문제는 [tony9402/backjoon](https://github.com/tony9402/baekjoon)에서 제공하는 추천 문제들을 풀겠습니다. 감사합니다.



 ![memo](https://github.githubassets.com/images/icons/emoji/unicode/1f4dd.png) **스터디 계획 & 일지**

---

### **자료구조**

| 날짜 | 문제 이름                                             | 난이도                                                       | 체크 | 한줄평                                                       | 풀이링크                                   |
| ---- | ----------------------------------------------------- | ------------------------------------------------------------ | ---- | ------------------------------------------------------------ | ------------------------------------------ |
| 8/23 | [요세푸스 문제](https://www.acmicpc.net/problem/1158) | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/6.svg"/> | ✅    | 간단한 문제지만 필요한 Index를 찾아가는 과정이 헤깔렸다.     | [링크](DataStructure/1158_요세푸스문제.py) |
| 8/23 | [스택](https://www.acmicpc.net/problem/10828)         | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> | ✅    | 파이써닉하게 코드를 작성하고자 노력했지만 뭔가 만족스럽지 않다. | [링크](DataStructure/10828_스택.py)        |
| 8/24 | [괄호](https://www.acmicpc.net/problem/9012)          | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> | ✅    | replace를 잘 활용하니 엄청 간단하게 코드를 작성할 수 있었다. | [링크](DataStructure/9012_괄호.py)         |
| 8/24 | [큐 2](https://www.acmicpc.net/problem/18258)         | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> | ✅    | 앞의 '스택' 문제와 비슷하다.                                 | [링크](DataStructure/18258_큐2.py)         |
| 8/25 | [카드 2](https://www.acmicpc.net/problem/2164)        | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> | ✅    | deque를 통해 추가, 삭제를 효율적으로 처리할 수 있다!! (시간이 중요한데 앞뒤가 헷갈리면 deque를 사용하자) | [링크](DataStructure/2164_카드2.py)        |
| 8/25 | [덱](https://www.acmicpc.net/problem/10866)           | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> | ✅    | 앞의 '스택', '큐2' 문제와 비슷하다. 다만 여기선 Deque로 구현 | [링크](DataStructure/10866_덱.py)          |
| 8/26 | [스택 수열](https://www.acmicpc.net/problem/1874)     | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> | ✅    | 시간초과가 떠서 계속 코드를 단순화 하도록 시도만 했는데 if 문의 차이로 시간초과없이 통과했다. 이유를 도통 모르겠다 ㅠㅠ | [링크](DataStructure/1874_스택수열.py)     |
| 8/26 | [후위 표기식2](https://www.acmicpc.net/problem/1935)  | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> | ✅    | 리스트에 값들을 적절한 위치에 추가하고 계산하면 되는건데.. 너무 잘 안풀렸다 ㅠㅠㅠ 공부를 많이 해야겠다!! | [링크](DataStructure/1935_후위표기식2.py)  |
| 8/27 | [쇠막대기](https://www.acmicpc.net/problem/10799)     | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> | ✅    | 나머지라는 개념이 바로 나지않아 생각보다 시간을 잡았는데, 떠올린다면 어렵지 않은 문제였다. | [링크](DataStructure/10799_쇠막대기.py)    |
| 8/27 | [프린터 큐](https://www.acmicpc.net/problem/1966)     | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> | ✅    | 한번의 처리보다 반복되는 일로 과정을 눈에보기에 하는것도 중요하다는 생각을 했다. | [링크](DataStructure/1966_프린터큐.py)     |
| 8/28 | [풍선 터뜨리기](https://www.acmicpc.net/problem/2346) | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> | ✅    | 배열을 돌려야 할때 queue를 사용하면 빠르고 쉽게 할 수 있다고 한다. queue에서 rotate는 편리했다. | [링크](DataStructure/2346_풍선터뜨리기.py) |
| 8/28 | [괄호의 값](https://www.acmicpc.net/problem/2504)     | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> | ✅    | 문자열을 처리하는 문제인데, 정규표현식을 이용하면 훨씬 쉬울 것 같다는 생각을 했지만 그렇게 하지 못했다. 정규표현식을 미리미리 공부해두자. | [링크](DataStructure/2504_괄호의값.py)     |
| 8/30 | [괄호 제거](https://www.acmicpc.net/problem/2800)     | ![img](https://d2gd6pc034wcta.cloudfront.net/tier/11.svg)    | ✅    | 괄호들의 쌍을 일단 찾은 다음 다시 조합하는 방식으로 가능한 정답을 찾아냈다. 이러한 아이디어가 없었다면 정말 어렵게 풀었을 것 같다. | [링크](DataStructure/2800_괄호제거.py)     |
| 8/30 | [탑](https://www.acmicpc.net/problem/2493)            | ![img](https://d2gd6pc034wcta.cloudfront.net/tier/11.svg)    | ✅    | 오른쪽에서 왼쪽으로 stack에 추가하며 진행한다. 자신보다 큰 탑이 나오면 스택에 있는 탑을 수를 센다. | [링크](DataStructure/2493_탑.py)           |

### **자료구조2**

| 날짜 | 문제 이름                                                    | 난이도                                                       | 체크 | 한줄평                                                       | 풀이링크                                                     |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 8/31 | [나는야 포켓몬 마스터 이다솜](https://www.acmicpc.net/problem/1620) | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> | ✅    | 딕셔너리에 쌍을 넣고 잘 조회할 수 있는지 확인하는 간단한 문제였다. | [링크](DataStructure2/1620_나는야포켓몬마스터이다솜.py)      |
| 8/31 | [문자열 집합](https://www.acmicpc.net/problem/14425)         | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> | ✅    | 문자열 집합안에 문자열에 있는 확인하는 정말 간단한 문제.. 난이도가 의심된다. | [링크](DataStructure2/14425_문자열집합.py)                   |
| 9/1  | [최대 힙](https://www.acmicpc.net/problem/11279)             | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> | ✅    | 힙이라는 개념에 대해 배울 수 있었다.  [여기](https://www.daleseo.com/python-heapq/) 정말 잘 정리가 되어있다. | [링크](DataStructure2/11279_최대힙.py)                       |
| 9/1  | [절댓값 힙](https://www.acmicpc.net/problem/11286)           | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> | ✅    | 위의 문제를 풀고나니 너무 쉬운문제였다!! ㅎㅎ                | [링크](DataStructure2/11286_절대값힙.py)                     |
| 9/2  | [이중 우선순위 큐](https://www.acmicpc.net/problem/7662)     | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> | ✅    | 최소힙, 최대힙만 정의하고 합치면 될듯 보였으나 동기화를 위해 식별자가 필요했다. 너무 어려운문제 ㅠㅠ | [블로그 링크](https://neomindstd.github.io/%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4/boj7662/) |
| 9/2  | [N번째 큰 수](https://www.acmicpc.net/problem/2075)          | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> | ✅    | 메모리 문제로 큐의 길이는 N으로 유지하는것이 중요했다. 힙의 특성을 잘 이용하자. | [링크](DataStructure2/2075_N번째큰수.py)                     |



**트리**

| 날짜 | 문제 이름                                                 | 난이도                                                       | 체크 | 한줄평                                                       | 풀이링크                                                     |
| ---- | --------------------------------------------------------- | ------------------------------------------------------------ | ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 9/3  | [트리의 부모 찾기](https://www.acmicpc.net/problem/11725) | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> | ✅    | BFS를 통해 간단히 이진 트리를 순회할 수 있었다.              | [링크](Tree/11725_트리의부모찾기.py)                         |
| 9/3  | [트리 순회](https://www.acmicpc.net/problem/1991)         | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> | ✅    | 전위 순회, 중위 순회, 후위 순회를 구현해야 하는데 서로간의 연관성을 위해 Class를 정의하고 왼쪽 오른쪽 노드를 이전에 정의한 클래스로 연결하는 접근이 재밌었다. | [링크](Tree/1991_트리순회.py) [참고한 사이트](https://lgphone.tistory.com/93) |

