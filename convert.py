import sys
sys.path.append("./include/")
import PyBool_public_interface as Bool
import PyBool_builder as BoolBld


master_formula=""

def main():

    #build the formula representation
    f = open("test.txt","r")
    clauses = build_clauses(f);
    f.close();

    #write the formula to a temporary file
    f = open("tmp.txt","w");

    #Some stuff for PBL
    write_header(f); #problem specific, sort of
    write_props(f,clauses);
    write_main(f,len(clauses));
    
    f.write(master_formula);
    f.close();

    #build an expression from the tmp file
    expr = Bool.parse_std("tmp.txt");


def write_main(f,n):
	f.write("Main_Exp : ");
	for i in range(n):
		if i < n-1:
			f.write(" P"+str(i)+"&");
		else:
			f.write(" P"+str(i));

def write_props(f,clauses):
	for i in range(len(clauses)):
		f.write("P"+str(i)+" = " + clauses[i]+"\n");

def write_header(f):
    f.write("Var_Order : ");
    for i in range(10,161):
        f.write("x"+str(i)+" ");
    f.write("\n");
        

def cprint(st):
    global master_formula;
    #sys.stdout.write(str(st))
    master_formula += st
    
def get_var_array(guess):
    a = []
    for i in range(len(guess)):
        a.append((str(i+1)+str(guess[i])));
    return a

def build_formula(guess,num):
    f = ""
    
    var_array = get_var_array(guess);

    f+=("(")
    if num==0:
        f+=("(")
        for l in range(len(var_array)):
            f+=(" ")
            f+=("~x"+var_array[l])
            f+=(" ")
            if not l==len(var_array)-1:
                   f+=(" &")
        f+=(")")
 

        
    elif num==1:
        for i in range(len(var_array)):
                f+=("(")
                for l in range(len(var_array)):
                    f+=(" ")
                    if l==i:
                        f+=("x"+var_array[l]);
                    else:
                        f+=("~x"+var_array[l]);
                    if not l==len(var_array)-1:
                        f+=(" &")
                    f+=(" ")
                f+=(")");
                f+=(" |")
        f = f[:-1];
                
    elif num==2:
        for i in range(len(var_array)):
            for j in range(len(var_array)):
                f+=("(")
                for l in range(len(var_array)):
                    f+=(" ")
                    if l==i or l==j:
                        f+=("x"+var_array[l]+" ");
                    else:
                        f+=("~x"+var_array[l]);
                    if not l==len(var_array)-1:
                        f+=(" &")
                    f+=(" ")
                f+=(")");
                f+=(" |")
        f = f[:-1];
                
    elif num==3:
        for i in range(len(var_array)):
            for j in range(len(var_array)):

                for k in range(len(var_array)):
                    f+=("(")
                    for l in range(len(var_array)):
                        f+=(" ")
                        if l==i or l==j or l==k:
                            f+=("x"+var_array[k]);
                        else:
                            f+=("~x"+var_array[k]);
                        if not l==len(var_array)-1:
                            f+=(" &")
                        f+=(" ")
                    f+=(")")
                    f+=("|")
        f = f[:-1];
    f+=(")")
    return f;

def build_clauses(f):
    clauses = []
    for line in f:
        parts = line.split(" ")
        guess = parts[0]
        num = int(parts[1])
#        print "\n\n\n\nNEW LINE\n\n\n\n"
        clauses.append(build_formula(guess,num));
#    print clauses;
    return clauses;


main();
    
