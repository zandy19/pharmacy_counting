import sys
def main():
    script = sys.argv[0]
    input= sys.argv[1]
    output=sys.argv[2]
    
    with open(input,'r') as input:
        line=input.readline().replace('\n','')
        
        drug_name=[]
        drug_cost=[]
        while line:
            line=input.readline().replace('\n','')
            words=line.split(',')
            try:
                drug_name.append(words[3])
            except:
                continue
            try:
                drug_cost.append(float(words[-1]))
            except:
                drug_cost.append(0)
                print ('incorrect drug cost for line %s',line)

    drug_summary={}
    for i, name in enumerate(drug_name):
        if name in drug_summary.keys():
            drug_summary[name][0]+=1
            drug_summary[name][1]+=drug_cost[i]
        else:
            drug_summary[name]=[0,0]
            drug_summary[name][0]=1
            drug_summary[name][1]=drug_cost[i]
        
    drug_summary_sorted=sorted(drug_summary.items(), key=lambda x: x[0])

    drug_summary_sorted=sorted(drug_summary_sorted, key=lambda x: x[1][1],reverse=True)


    title_line='drug_name,num_prescriber,total_cost\n'

    with open (output,'w+') as out:
        out.write(title_line)
        for item in drug_summary_sorted:
            line= item[0]+','+ str(item[1][0])+','+ str(item[1][1])+'\n'
            out.write(line)



main()
