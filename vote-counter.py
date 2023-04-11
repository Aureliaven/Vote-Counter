with open("./votes.csv") as f:
    f.readline()
    votes = [i.strip() for i in f.readlines() if i != '\n']
    national_candidates = {}
    local_candidates = {}
    state_winners = {}
    for v in votes:
        v_list = v.split(",")
        voter_number = v_list[0]
        state = v_list[1]
        national_choice = v_list[2]
        local_choice = v_list[3]
        reserve_national_choice = v_list[4]
        if state not in state_winners.keys():
            state_winners[state] = ""
        if national_choice not in national_candidates.keys():
            national_candidates[national_choice] = 1
        else:
            national_candidates[national_choice] += 1
        if (local_choice, state) not in local_candidates.keys():
            local_candidates[(local_choice, state)] = 1
        else:
            local_candidates[(local_choice, state)] += 1
    national_winner = max(national_candidates, key=national_candidates.get)
    for state in state_winners.keys():
        state_candidates = [i[0] for i in local_candidates.keys() if i[1] == state]
        state_candidates_votes = {}
        for c in state_candidates:
            state_candidates_votes[c] = local_candidates[(c,state)]
        state_winners[state] = max(state_candidates_votes, key=state_candidates_votes.get)
        print(f"{state} winner: {state_winners[state]}")
    print(f"National winner: {national_winner}")