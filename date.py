def is_leap_year(y):
    return (y%400==0) or (y%4==0 and y%100!=0)
def get_day_of_the_week(m,d,y):
    c={1:1,2:4,3:4,4:0,5:2,6:5,7:0,8:3,9:6,10:1,11:4,12:6}
    l=y%100
    a=l//12
    b=l%12
    k=b//4
    o=0
    if m in (1,2) and is_leap_year(y): o+=6
    if 1600<=y<=1699: o+=6
    elif 1700<=y<=1799: o+=4
    elif 1800<=y<=1899: o+=2
    elif 2000<=y<=2099: o+=6
    elif 2100<=y<=2199: o+=4
    t=a+b+k+d+c[m]+o
    return {0:"Saturday",1:"Sunday",2:"Monday",3:"Tuesday",4:"Wednesday",5:"Thursday",6:"Friday"}[t % 7]
def main():
    print("Sunday"==get_day_of_the_week(12,25,2022))
    print("Friday"==get_day_of_the_week(8,26,2022))
if __name__ == "__main__":
    main()
