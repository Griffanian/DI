const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

secret_name = ""

for (const element of names) {
    secret_name += element[0]
}

console.log(secret_name)