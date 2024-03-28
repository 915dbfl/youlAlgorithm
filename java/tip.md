## 아아 java 코테 기본 문법 지금부터 정리하겠습니다.

## tip 나열
- 백준에서는 class명이 Main이어야 함.
- bufferedReader/Writer를 쓰려면 IOException을 처리해줘야 함

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
