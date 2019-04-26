def decode(self, sequence):
    # sequence : O
    # sequence_length : T
    sequence_length = len(sequence)
    if sequence_length == 0:
        return []

    # delta : 비터비 확률 v
    # Dynamic Programming : 중간 계산값 저장해 활용
    delta = {}

    # 시작 지점의 delta값 계산
    for state in self._states:
        # start_prob(state) : p(cold\|start) or p(hot\|start)
        # sequence[0] : 관측 시퀀스의 첫번째 요소, o_1, '3'
        # emit_prob(state, sequence[0]) : p(3\|cold) or p(3\|hot)
        delta[state] = self.start_prob(state) * self.emit_prob(state, sequence[0])

    # pre : backtrace
    pre = []

    # sequence의 두번째 값부터 마지막까지 delta, backtrace 모두 계산
    # index : 위 수식에서 t
    for index in range(1, sequence_length):
        # delta_bar : t번째 관측치의 비터비 확률들
        # index가 거듭될수록 그 요소가 늘어남
        # 다 돌면 sequence_length 길이
        delta_bar = {}
        # pre_state : t번째 관측치의 backtrace들
        # index가 거듭될수록 그 요소가 늘어남
        # 다 돌면 sequence_length 길이
        pre_state = {}
        for state_to in self._states:
            max_prob = 0
            max_state = None  # backtrace 변수
            for state_from in self._states:
                # state_from : 위 수식에서 i
                # state_to : 위 수식에서 j
                # delta[state_from] : 직전 상태의 비터비 확률(저장된 값 불러와 계산량 줄임)
                # trans_prob : 위 수식에서 a
                prob = delta[state_from] * self.trans_prob(state_from, state_to)
                # 비터비 확률 수식에서 i에 대해 최대값을 구하는데,
                # 방출확률 b는 i에 대해 무관하므로 최대값 연산에서 제외
                if prob > max_prob:
                    # 최대값 저장 : 현재 상태의 비터비 확률
                    max_prob = prob
                    # 최대값의 위치 저장 : 현재 상태의 backtrace
                    max_state = state_from
            delta_bar[state_to] = max_prob * self.emit_prob(state_to, sequence[index])
            pre_state[state_to] = max_state
        # o_2까지의 비터비 확률을 구했다면 o_1 이전의 비터비 확률은 불필요
        # o_2의 비터비 확률들의 모음인 delta_bar를 전체 delta에 덮어씌움
        delta = delta_bar
        # o_2까지의 backtrace를 구했다 하더라도 o_3은 달라질 수 있음
        # pre에 pre_state를 append
        pre.append(pre_state)

    # 전체 시퀀스를 대상으로 최대 비터비확률과
    # 최대 비터비 확률을 내는 state 찾기
    # 현재 delta에는 시퀀스의 마지막 요소(O_T)에
    # 해당하는 비터비 확률들이 저장돼 있기 때문
    # (state로만 구분되어 있음)
    max_state = None
    max_prob = 0
    for state in self._states:
        if delta[state] > max_prob:
            max_prob = delta[state]
            max_state = state

    if max_state is None:
        return []

    # 최대 비터비 확률을 내는 state가 backtrace의 첫번째 요소
    result = [max_state]
    # index를 시퀀스의 역방향으로 후진하면서
    for index in range(sequence_length - 1, 0, -1):
        # index에 해당하는 max_state들을 뽑아내기
        # 이는 저 위쪽에서 이미 max_state들을 저장해두었기 때문에 가능
        max_state = pre[index - 1][max_state]
        # 뽑아낸 max_state들을 result의 첫번째 위치에 저장
        result.insert(0, max_state)

    return result