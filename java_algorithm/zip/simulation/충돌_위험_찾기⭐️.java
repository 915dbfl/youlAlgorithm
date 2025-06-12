package java_algorithm.zip.simulation;

import java.util.*;

public class 충돌_위험_찾기 {

    private static class TimeCoordinate {
        int x;
        int y;
        int time;

        public TimeCoordinate(int x, int y, int time) {
            this.x = x;
            this.y = y;
            this.time = time;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            TimeCoordinate that = (TimeCoordinate) o;
            return x == that.x && y == that.y && time == that.time;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y, time);
        }
    }

    private List<TimeCoordinate> getPath(int[] route, int[][] points) {
        List<TimeCoordinate> path = new ArrayList<>();
        int currentTime = 0;

        // 로봇의 현재 위치를 추적할 변수
        int currentX = points[route[0] - 1][0]; // 경로의 시작 지점
        int currentY = points[route[0] - 1][1]; // 경로의 시작 지점

        for (int i = 0; i < route.length - 1; i++) {
            // 각 세그먼트의 시작점은 로봇의 현재 위치
            int endPointIndex = route[i + 1] - 1;

            int ex = points[endPointIndex][0];   // 목표 x
            int ey = points[endPointIndex][1];   // 목표 y

            // x 좌표 맞추기
            while (currentX != ex) {
                path.add(new TimeCoordinate(currentX, currentY, currentTime));
                if (currentX < ex) {
                    currentX += 1;
                } else {
                    currentX -= 1;
                }
                currentTime += 1;
            }

            // y 좌표 맞추기
            while (currentY != ey) {
                path.add(new TimeCoordinate(currentX, currentY, currentTime));
                if (currentY < ey) {
                    currentY += 1;
                } else {
                    currentY -= 1;
                }
                currentTime += 1;
            }
        }
        // 최종 목적지에 도달한 로봇의 위치를 마지막으로 한 번 추가
        // 이 시점의 currentX, currentY는 최종 목적지 좌표입니다.
        path.add(new TimeCoordinate(currentX, currentY, currentTime));
        
        return path;
    }

    public int solution(int[][] points, int[][] routes) {
        List<TimeCoordinate> allRobotMovements = new ArrayList<>();

        for (int[] route : routes) {
            allRobotMovements.addAll(getPath(route, points));
        }

        Map<TimeCoordinate, Integer> movementCounts = new HashMap<>();
        for (TimeCoordinate tc : allRobotMovements) {
            movementCounts.put(tc, movementCounts.getOrDefault(tc, 0) + 1);
        }

        int collisionPositionsCount = 0;
        for (Integer count : movementCounts.values()) {
            if (count >= 2) {
                collisionPositionsCount += 1;
            }
        }

        return collisionPositionsCount;
    }
}