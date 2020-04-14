def painHouse(costs):
    dp = [costs[0]]
    for row in costs[1:]:
        new_dp_row = []
        for idx in range(len(row)):
            new_dp_row.append(min(dp[-1][0:idx] + dp[-1][idx + 1:]) + row[idx])
        dp.append(new_dp_row)
    return min(dp[-1])


costsMatrix = [[17, 2, 17],
               [8, 4, 10],
               [6, 3, 19],
               [4, 8, 12]]

print(painHouse(costsMatrix))
