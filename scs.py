from recursion_viz import recursion_visualizer as rv
 
@rv
def SCS_DP(s: str, t: str, lookup: dict = {}) -> str:
    if len(s) == 0 or len(t) == 0:  
        return s+t

    key = (s,t)

    if not key in lookup:                 
        if s[-1] == t[-1]:              
            lookup[key] = SCS_DP(s=s[0:-1], t=t[0:-1], lookup=lookup) + s[-1]
        else:
            lookup[key] = min(SCS_DP(s[0:-1], t=t, lookup=lookup)+s[-1], SCS_DP(s=s, t=t[0:-1], lookup=lookup)+t[-1])

    return lookup[key]
    

if __name__ == "__main__":
    # Call function
    s = "ABCBDAB"
    t = "BDCABA"
    scs = SCS_DP(s,t)

    print(rv.graph)

    rv.graph.render('test-output/round-table.gv', view=True)

    # print("Edges:")
    # print(RV.graph.get_edge_list())


    print(scs)