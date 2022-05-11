from hi import TicToc, FindE

if __name__ == "__main__":
    tt = TicToc()
    tt.tic()
    finding_e = FindE()
    finding_e.generating_numbers(10000)
    e = finding_e.value_of_e()
    print("E = %12.8f "%(e))
    print("TIME = %.6f seconds"%(tt.toc()))
    
##  HÜSNA İBİŞ 180315033