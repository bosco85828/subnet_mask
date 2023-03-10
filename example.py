
import network
import os 
import sys


def get_devops_waf():
    f=os.popen(""" 
            curl "google doc" -Ls | tr -d ' ' |  sort -V | uniq
            """)

    wafl=f.read().strip().split('\n')


    wafl=[ x if "/" in x else x+"/32" for x in wafl ]
    wafip=[ x.split('.') for x in wafl if x ]
    return wafip    


def get_same_bclass(wafip):
    waf_b_list=[]
    i=0
    j=1
    while i < len(wafip) : 
        if j >= len(wafip):
            waf_b_list.append(wafip[i:j])
            break
        if wafip[i][0:2] != wafip[j][0:2]:
            waf_b_list.append(wafip[i:j])
            i=j        
        j+=1
    
    return waf_b_list

def main(waf_b_list,num=20):
    num=int(num)
    # print(num)
    # print(type(num))
    final_wafl=[]
    num=2**(24-num)
    count_=0
    for bip in waf_b_list:
        i=1
        while i <= 256/num:
            same_wafl=[ ".".join(x) for x in bip if int(x[2]) < num*i ]
            bip=[ x for x in bip if ".".join(x) not in same_wafl ]
            if not same_wafl :
                i+=1
                continue        
            count_ += len(same_wafl)
            subnets = network.Subnets(same_wafl)
            supernet = subnets.get_smallest_supernet()
            final_wafl+=[supernet.to_string()]
            i+=1

    print(count_)
    print(len(final_wafl))
    return final_wafl
    
if __name__ == "__main__":
    try:
        mask=sys.argv[1]
        if 16 <= int(sys.argv[1]) <= 24:
            print("\n".join(main(get_same_bclass(get_devops_waf()),mask)))
        else : 
            print("please input subnet mask between 16-24")
    except IndexError :
        print("\n".join(main(get_same_bclass(get_devops_waf()))))
    
