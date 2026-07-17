"""You are given an integer money denoting the amount of money 
(in dollars) that you have and another integer children denoting 
the number of children that you must distribute the money to.

You have to distribute the money according to the following rules:

All money must be distributed.
Everyone must receive at least 1 dollar.
Nobody receives 4 dollars.
Return the maximum number of children who may receive exactly 
8 dollars if you distribute the money according to the aforementioned rules.
 If there is no way to distribute the money, return -1."""

class Solution(object):
    def distMoney(self, money, children):
        """
        :type money: int
        :type children: int
        :rtype: int
        """
        if money < children: return -1
        money -= children

        eights = min(money // 7, children)
        money -= eights*7
        if eights == children and money > 0: eights -= 1
        elif eights == children-1 and money == 3: eights -= 1
             
        return eights