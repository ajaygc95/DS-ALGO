"""
Jump Game

Given a list of maximum jump lengths from different houses, determine if you can reach the last house in one or more jumps starting from the first one.

Maximum jump length of 2 from a house, for example, means that you can either jump to the next house or to the one after next.

Example One

{

"maximum_jump_lengths": [2, 3, 1, 0, 4, 7]

}

Output:

1

You can reach the last house in the following way:



Example Two

{

"maximum_jump_lengths": [3, 1, 1, 0, 2, 4]

}

Output:

0

You cannot make it past house at index 3. Maximum jump length of 0 from that house means that you cannot jump further from it.

"""

# seems like counting problems

input = [3, 1, 1, 0, 2, 4]