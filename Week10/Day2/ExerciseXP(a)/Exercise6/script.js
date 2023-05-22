let bankAmount = 0
const save = (num) => parseInt(num)*1.17
const details = ["+200", "-100", "+146", "+167", "-290"]

for (item of details) {
    itemVat = save(item)
    bankAmount += itemVat
}
bankAmount = Math.round(bankAmount * 100) / 100
console.log(bankAmount)


