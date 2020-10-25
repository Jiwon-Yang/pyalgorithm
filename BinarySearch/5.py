# -*- coding: utf-8 -*- 
import sys
sys.stdin = open("input.txt", "r")

n = int(input())
meetings = []
for i in range(n):
    s, e = map(int, input().split())
    meetings.append((s, e))

# 끝나는 시간 순서대로 정렬
meetings.sort(key=lambda x: (x[1], x[0]))

endTime = 0
cnt = 0
for s, e in meetings:
    if s >= endTime:
        cnt += 1
        endTime = e
