outletSales = ([0,0,0,0] for i in range(50)).list()

quarter = int(input("Quarter to total: "))
total = Outlet1Sales[quarter-1]+Outlet2Sales[quarter-1]+Outlet3Sales[quarter-1]
print(f"Total for quarter {quarter}: {total}")