## 아아 java 코테 기본 문법 지금부터 정리하겠습니다.

## tip 나열
- 1초에 1억 번의 연산 진행
- 백준에서는 class명이 Main이어야 함
- bufferedReader/Writer를 쓰려면 IOException을 처리해줘야 함
- return; -> 해당 함수만 종료(단, main에서 쓰이면 프로그램 전체 중지)
- System.exit(0) -> 0(정상적인 종료), 그 외(비정상적인 종료)
- char[] str = br.readeLine().toCharArray
- System.out.println(String.format("%d %d", a, b))
- queue는 LinkedList를 활용해 생성함
- int[] memory = Arrays.stream(br.readLine().split(" "))
    .mapToInt(Integer::parseInt)
    .toArray();
- buf.write(String.valueOf(array[i]));
- int tmpL = (int)l/3;
- linkedList vs arrayList
    - 조회가 많다면? arrayList, 배열로 구현, index로 한 번에 조회
    - 삽입/삭제가 많다면? linkedList, 노드로 구현, 주소값만 변경해주면 됨
- java의 max_value = 2147483647, 따라서 해당 범위를 넘어가면 Long으로 선언해줘야 함(overflow도 그냥 틀렸다고 나옴)
- return의 차이(1: throw exception, 2: return special value - null)
    - add / offer
    - remove / poll
    - element / peek
- Boolean(null(default)/true/false) vs boolean(true/false(default))

## 입력&출력
```java
BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
String input = br.readLine();
int a = Integer.parseInt(br.readLine());
String str = br.readLine().split(" "); // 10 10

StringTokenizer st = new StringTokenizer(br.readLine()); // 10 20, split()보다 빠른 방법
int a = Integer.parseInt(st.nextToken()); // 10
int b = Integer.parseInt(st.next) // 20
```

```java
BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
bw.write("hello bf!"); // 버퍼에 값 저장
bw.newLine(); // 줄바꿈
bw.flush(); // 버퍼에 남아있는 데이터를 비운 후, 해당 데이터를 출력
bw.close(); // flush와 동일 + 마지막에 stream을 닫음
```

- 입출력 시, 필요한 `import` 모음

```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.io.IOException;
```