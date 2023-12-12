Outlet1Sales = [10,12,15,10]
Outlet2Sales = [5,8,3,6]
Outlet3Sales = [10,12,15,10]

quarter = int(input("Quarter to total: "))
total = Outlet1Sales[quarter-1]+Outlet2Sales[quarter-1]+Outlet3Sales[quarter-1]
print(f"Total for quarter {quarter}: {total}")