/*
해설
- 초침과 시침 혹은 분침이 겹칠 떄 -> 알람 울림
- 1분이 지난 후 시침/ 분침 / 초침의 이동
    - 시침 -> 0.5도 이동
    - 분침 -> 6도 이동
    - 초침 -> 제자리
- 1초가 지난 후 시침/분침/초침의 이동
    - 시침 -> 0.5 / 60 이동
    - 분침 -> 0.1 이동
    - 초침 -> 1 이동
- 00:00:00에서 시작과 끝 알림 count
    - 매분마다 시침/ 분침 2번이 겹침
        - 59~60분 되는 시점에는 분침이 겹치지 않음 -> 시 만큼 count - 진행
        - 00시와 12시에는 시침/분침/초침이 일직선 -> 1번만 겹침 -> -2 진행
    - 따라서 편리하게 계산하기 위해서 00:00:00에서 시작과 끝 알림 count
*/

public class 아날로그_시계 {

    public int solution(int h1, int m1, int s1, int h2, int m2, int s2) {
        // 00:00:00에서 시작과 끝 알람 개수 count
        int countUntilT2 = getCountFromMidnight(h2, m2, s2);
        int countUntilT1 = getCountFromMidnight(h1, m1, s1);
        System.out.println(countUntilT2 + ", " + countUntilT1);

        // 그 차가 시작~끝 사이 치는 알람의 개수
        int result = countUntilT2 - countUntilT1;

        // 겹쳐있는 상태에서 시작한 경우, count
        if ((h1 == 0 || h1 == 12) && m1 == 0 && s1 == 0) {
            result += 1;
        }

        return result;
    }

    private int getCountFromMidnight(int h, int m, int s) {
        double hDegree = (h % 12) * 30 + m * 0.5 + s * (0.5 / 60.0);
        double mDegree = m * 6 + s * 0.1;
        double sDegree = s * 6;

        // 마무리 상태에서의 알람 count
        int count = 0;
        if (sDegree >= mDegree) {
            count += 1;
        }
        if (sDegree >= hDegree) {
            count += 1;
        }

        // 분만큼 시침/분침 2번의 알람
        count += (h * 60 + m) * 2;

        // 분침의 경우, 59 -> 00으로 넘어갈 때 시침과 겹치지 않음
        count -= h;

        // 시침의 경우, 00시와 12시에 시침과 겹치지 않음
        if (h >= 12) {
            count -= 2;
        }

        return count;
    }
}