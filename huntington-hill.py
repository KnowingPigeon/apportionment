import csv
import math

def total_apportioned(apportionments):
    total = 0
    for state in apportionments:
        total += apportionments[state]
    return total

def get_state_from_name(name, states):
    for state in states:
        if state[0] == name:
            return state
    return None

#
def apportion(inputs,number_of_seats):
    states = []
    output = ''
    for input in inputs:
        output += input[:-4] + '+'
        states_csv_file = open(input, "r")
        states_csv = csv.reader(states_csv_file)
        for state in states_csv:
            states.append(state)
    output = output[:-1] + str(number_of_seats) + '.txt'

    apportionments = {}
    a_n_values = {}
    for state in states:
        apportionments[state[0]] = 1
        a_n_values[state[0]] = [0,1]
        a_n_values[state[0]][0] = (int)(state[2]) / math.sqrt(a_n_values[state[0]][1] * (a_n_values[state[0]][1] + 1))

    seats_left = number_of_seats - total_apportioned(apportionments)
    while seats_left > 0:
        next_apportionment = ['', 0]
        for state in states:
            if a_n_values[state[0]][0] > next_apportionment[1]:
                next_apportionment = [state[0], a_n_values[state[0]][0]]
        state = get_state_from_name(next_apportionment[0], states)
        apportionments[state[0]] += 1
        a_n_values[state[0]][1] += 1
        a_n_values[state[0]][0] = (int)(state[2]) / math.sqrt(a_n_values[state[0]][1] *  \
                                                            (a_n_values[state[0]][1] + 1))
        seats_left -= 1

    bin = open(output, 'w')
    for state in apportionments:
        bin.write(state + ',' + str(apportionments[state]) + '\n')

apportion(['50states.csv'], 435)
#apportion()