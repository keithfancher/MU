#!/usr/bin/env python


MAX_ITERATIONS = 10
START = "MI"
#END = "MIIUIIU"
#END = "MI"
END = "MU" # never finds it? aha!


# TODO: add exceptions for malformed input


# Performs the acutal test
#   start -- starting string
#   goal -- ending string
#   max_iterations -- how long to try before giving up
#   show_results -- show output along the way?
#
#   returns True if the goal is reached, False otherwise
def mu_test(start, goal, max_iterations, show_results=False):
    current_list = [start.upper()]
    steps = 0

    if show_results:
        print "Start:\t", start.upper()
        print "Goal:\t", goal.upper()
        print

    # just GTFO if start == goal
    if start == goal:
        if show_results:
            print "Hey silly, those are both the same!"
        return True

    # otherwise try to reach the goal
    for i in xrange(0, max_iterations):
        current_list = next_theorem_list(current_list)
        steps += 1
        if show_results:
            print str(steps), current_list

        # whooopdee doo!
        if goal.upper() in current_list:
            if show_results:
                print "Got it! (in %d steps)" % steps
            return True

    # if we get here, it means we've failed!
    if show_results:
        print "Failed to reach %s in %d steps :(" % (goal.upper(),
                                                     max_iterations)
    return False


# Following are the definitions of the 4 different rules. If a particular rule
# doesn't apply, the function simply returns the string unchanged.


# If last letter of string is I, add U to the end (eg MI => MIU)
def rule1(s):
    s_ret = s
    if s_ret[-1:] == "I":
        s_ret = s + "U"
    return s_ret


# Can always double the tail of the string (eg Mx => Mxx)
def rule2(s):
    return s + s[1:]


# Can replace III with U (eg MIIIx => MUx)
def rule3(s):
    s_ret = s
    position = s.find("III")
    if position > 0:
        s_ret = s[:position] + "U" + s[position + 3:]
    return s_ret


# Can drop 2 consecutive U's (eg MUUU => MU)
def rule4(s):
    s_ret = s
    position = s.find("UU")
    if position > 0:
        s_ret = s[:position] + s[position + 2:]
    return s_ret


# Builds the list of next possible strings, given a starting list
def next_theorem_list(start_list):
    new_list = []

    for item in start_list:
        if rule1(item) != item:
            new_list.append(rule1(item))
        if rule2(item) != item:
            new_list.append(rule2(item))
        if rule3(item) != item:
            new_list.append(rule3(item))
        if rule4(item) != item:
            new_list.append(rule4(item))

    return new_list


def main():
    # give 'er a whirl!
    mu_test(START, END, MAX_ITERATIONS, True)


if __name__ == "__main__":
    main()
