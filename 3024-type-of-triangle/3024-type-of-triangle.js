function triangleType(nums) {
    const [a, b, c] = nums;

    if (a + b <= c || a + c <= b || b + c <= a) {
        return "none";
    }

    if (a === b && b === c) {
        return "equilateral";
    } else if (a === b || a === c || b === c) {
        return "isosceles";
    } else {
        return "scalene";
    }
}
triangleType([3, 3, 3])
triangleType([3, 4, 5])  