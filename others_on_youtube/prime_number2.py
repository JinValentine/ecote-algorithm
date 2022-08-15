# 9. 코딩 테스트에서 자주 출제되는 기타 알고리즘
# 개선된 소수의 판별
# 모든 약수가 가운데 약수를 기준으로 곱셈 연산에 대해 대칭을 이룬다.
# 특정한 자연수의 모든 약수를 찾을 때 가운데 약수(제곱근)까지만 확인하면 된다.
# ex) 16이 2로 나누어떨어진다는 것은 8로도 나누어떨어진다는 것을 의미한다.

import math
# 소수 판별 함수 (2이상의 자연수에 대하여)
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

print(is_prime_number(4))
print(is_prime_number(7))
