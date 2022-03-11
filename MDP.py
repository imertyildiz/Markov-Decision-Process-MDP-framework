def max_action(action_noise, environment, state, x, y, obsclate_states):
    max_value = -99999999.0
    way = ">"
    for i in ['>', 'V', '<', '^']:
        if i == '>':
            if state[1] == y or ((state[0], state[1] + 1) in obsclate_states):
                noise2 = environment[state] * action_noise[1]
            else:
                noise2 = environment[state[0], state[1] + 1] * action_noise[1]
            if state[0] == 0 or ((state[0] - 1, state[1]) in obsclate_states):
                noise1 = environment[state] * action_noise[0]
            else:
                noise1 = environment[state[0] - 1, state[1]] * action_noise[0]
            if state[0] == x or ((state[0] + 1, state[1]) in obsclate_states):
                noise3 = environment[state] * action_noise[2]
            else:
                noise3 = environment[state[0] + 1, state[1]] * action_noise[2]
            val = noise1 + noise2 + noise3
            if val > max_value:
                max_value = val
                way = i
        elif i == 'V':
            if state[0] == x or ((state[0] + 1, state[1]) in obsclate_states):
                noise2 = environment[state] * action_noise[1]
            else:
                noise2 = environment[state[0] + 1, state[1]] * action_noise[1]
            if state[1] == y or ((state[0], state[1] + 1) in obsclate_states):
                noise1 = environment[state] * action_noise[0]
            else:
                noise1 = environment[state[0], state[1] + 1] * action_noise[0]
            if state[1] == 0 or ((state[0], state[1] - 1) in obsclate_states):
                noise3 = environment[state] * action_noise[2]
            else:
                noise3 = environment[state[0], state[1] - 1] * action_noise[2]
            val = noise1 + noise2 + noise3
            if val > max_value:
                max_value = val
                way = i
        elif i == '<':
            if state[1] == 0 or ((state[0], state[1] - 1) in obsclate_states):
                noise2 = environment[state] * action_noise[1]
            else:
                noise2 = environment[state[0], state[1] - 1] * action_noise[1]
            if state[0] == x or ((state[0] + 1, state[1]) in obsclate_states):
                noise1 = environment[state] * action_noise[0]
            else:
                noise1 = environment[state[0] + 1, state[1]] * action_noise[0]
            if state[0] == 0 or ((state[0] - 1, state[1]) in obsclate_states):
                noise3 = environment[state] * action_noise[2]
            else:
                noise3 = environment[state[0] - 1, state[1]] * action_noise[2]
            val = noise1 + noise2 + noise3
            if val > max_value:
                max_value = val
                way = i
        else:
            if state[0] == 0 or ((state[0] - 1, state[1]) in obsclate_states):
                noise2 = environment[state] * action_noise[1]
            else:
                noise2 = environment[state[0] - 1, state[1]] * action_noise[1]
            if state[1] == 0 or ((state[0], state[1] - 1) in obsclate_states):
                noise1 = environment[state] * action_noise[0]
            else:
                noise1 = environment[state[0], state[1] - 1] * action_noise[0]
            if state[1] == y or ((state[0], state[1] + 1) in obsclate_states):
                noise3 = environment[state] * action_noise[2]
            else:
                noise3 = environment[state[0], state[1] + 1] * action_noise[2]
            val = noise1 + noise2 + noise3
            if val > max_value:
                max_value = val
                way = i
    return max_value, way


def value_iteration(environment, reward, gamma, epsilon, iteration, goal_states, action_noise, x, y, obsclate_states):
    omega = 999999999999.0
    policy = {}
    environment_copy = environment.copy()
    for i in environment_copy:
        if (i not in goal_states) and (i not in obsclate_states):
            policy[i] = ""
    environmentV1 = None
    while omega >= (epsilon * (1 - gamma) / gamma):
        omega = 0
        environmentV1 = environment_copy.copy()
        for i in policy:
            temp = max_action(action_noise, environmentV1, i, x, y, obsclate_states)
            environment_copy[i] = reward + gamma * temp[0]
            policy[i] = temp[1]
            if abs(environmentV1[i] - environment_copy[i]) > omega:
                omega = abs(environmentV1[i] - environment_copy[i])
    for i in environmentV1:
        environmentV1[i] = round(environmentV1[i], 2)
    return environmentV1, policy


def policy_helper(action_noise, environment, state, x, y, obsclate_states, inp_way):
    if inp_way == '>':
        if state[1] == y or ((state[0], state[1] + 1) in obsclate_states):
            noise2 = environment[state] * action_noise[1]
        else:
            noise2 = environment[state[0], state[1] + 1] * action_noise[1]
        if state[0] == 0 or ((state[0] - 1, state[1]) in obsclate_states):
            noise1 = environment[state] * action_noise[0]
        else:
            noise1 = environment[state[0] - 1, state[1]] * action_noise[0]
        if state[0] == x or ((state[0] + 1, state[1]) in obsclate_states):
            noise3 = environment[state] * action_noise[2]
        else:
            noise3 = environment[state[0] + 1, state[1]] * action_noise[2]
        val = noise1 + noise2 + noise3
    elif inp_way == 'V':
        if state[0] == x or ((state[0] + 1, state[1]) in obsclate_states):
            noise2 = environment[state] * action_noise[1]
        else:
            noise2 = environment[state[0] + 1, state[1]] * action_noise[1]
        if state[1] == y or ((state[0], state[1] + 1) in obsclate_states):
            noise1 = environment[state] * action_noise[0]
        else:
            noise1 = environment[state[0], state[1] + 1] * action_noise[0]
        if state[1] == 0 or ((state[0], state[1] - 1) in obsclate_states):
            noise3 = environment[state] * action_noise[2]
        else:
            noise3 = environment[state[0], state[1] - 1] * action_noise[2]
        val = noise1 + noise2 + noise3
    elif inp_way == '<':
        if state[1] == 0 or ((state[0], state[1] - 1) in obsclate_states):
            noise2 = environment[state] * action_noise[1]
        else:
            noise2 = environment[state[0], state[1] - 1] * action_noise[1]
        if state[0] == x or ((state[0] + 1, state[1]) in obsclate_states):
            noise1 = environment[state] * action_noise[0]
        else:
            noise1 = environment[state[0] + 1, state[1]] * action_noise[0]
        if state[0] == 0 or ((state[0] - 1, state[1]) in obsclate_states):
            noise3 = environment[state] * action_noise[2]
        else:
            noise3 = environment[state[0] - 1, state[1]] * action_noise[2]
        val = noise1 + noise2 + noise3
    else:
        if state[0] == 0 or ((state[0] - 1, state[1]) in obsclate_states):
            noise2 = environment[state] * action_noise[1]
        else:
            noise2 = environment[state[0] - 1, state[1]] * action_noise[1]
        if state[1] == 0 or ((state[0], state[1] - 1) in obsclate_states):
            noise1 = environment[state] * action_noise[0]
        else:
            noise1 = environment[state[0], state[1] - 1] * action_noise[0]
        if state[1] == y or ((state[0], state[1] + 1) in obsclate_states):
            noise3 = environment[state] * action_noise[2]
        else:
            noise3 = environment[state[0], state[1] + 1] * action_noise[2]
        val = noise1 + noise2 + noise3
    return val


def policy_evaluation(environment, reward, gamma, epsilon, iteration, goal_states, action_noise, x, y, obsclate_states,
                      policy):
    environmentV1 = environment.copy()
    environmentV2 = environment.copy()
    for i in range(0, iteration):
        environmentV2 = environmentV1.copy()
        for state in policy:
            environmentV1[state] = reward + gamma * policy_helper(action_noise, environmentV2, state, x, y,
                                                                  obsclate_states, policy[state])
    return environmentV1


def policy_iteration(environment, reward, gamma, epsilon, iteration, goal_states, action_noise, x, y, obsclate_states):
    policy = {}
    for i in environment:
        if (i not in goal_states) and (i not in obsclate_states):
            policy[i] = ">"
    unchanged = True
    env = environment.copy()
    while unchanged:
        env = policy_evaluation(env.copy(), reward, gamma, epsilon, iteration, goal_states, action_noise, x, y,
                                obsclate_states, policy)
        unchanged = False
        for i in policy:
            temp = max_action(action_noise, env, i, x, y, obsclate_states)
            if temp[0] > policy_helper(action_noise, env, i, x, y, obsclate_states, policy[i]):
                policy[i] = temp[1]
                unchanged = True
    for i in env:
        env[i] = round(env[i], 2)
    return env, policy


def SolveMDP(method_name, problem_file_name):
    with open(problem_file_name) as f:
        lines = f.read().splitlines()
    environment = {}
    lines.pop(0)
    size = lines.pop(0).split(" ")
    size_x = int(size[0])
    size_y = int(size[1])
    for i in range(0, size_x):
        for j in range(0, size_y):
            environment[(i, j)] = 0.0
    lines.pop(0)
    line = lines.pop(0).split("|")
    obsclate_states = []
    for i in line:
        x = i.replace("(", "").replace(")", "").split(",")
        obsclate_states.append(tuple((int(x[0]), int(x[1]))))
    lines.pop(0)
    line = lines.pop(0).split("|")
    goal_states = []
    for i in line:
        y = i.split(":")
        x = y[0].replace("(", "").replace(")", "").split(",")
        environment[(int(x[0]), int(x[1]))] = float(y[1])
        goal_states.append(tuple((int(x[0]), int(x[1]))))
    lines.pop(0)
    reward = float(lines.pop(0))
    lines.pop(0)
    action_noise = []
    x = float(lines.pop(0))
    action_noise.append(float(lines.pop(0)))  # b - a - c
    action_noise.append(x)  # b - a - c
    action_noise.append(float(lines.pop(0)))  # b - a - c
    lines.pop(0)
    gamma = float(lines.pop(0))
    lines.pop(0)
    epsilon = float(lines.pop(0))
    lines.pop(0)
    iteration = int(lines.pop(0))

    if method_name == "ValueIteration":
        return value_iteration(environment, reward, gamma, epsilon, iteration, goal_states, action_noise, size_x - 1,
                               size_y - 1, obsclate_states)
    elif method_name == "PolicyIteration":
        return policy_iteration(environment, reward, gamma, epsilon, iteration, goal_states, action_noise, size_x - 1,
                                size_y - 1, obsclate_states)
