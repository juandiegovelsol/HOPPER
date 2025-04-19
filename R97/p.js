const isSafeReport = (report) => {
  let isAscending = report[1] > report[0];
  for (let i = 1; i < report.length; i++) {
    const difference = report[i] - report[i - 1];
    if (Math.abs(difference) < 1 || Math.abs(difference) > 3) {
      return false;
    }
    if ((isAscending && difference < 0) || (!isAscending && difference > 0)) {
      return false;
    }
  }
  return true;
};

console.log(isSafeReport([14, 11, 20]));

console.log(isSafeReport([10, 12, 14, 16]));

console.log(isSafeReport(false));

console.log(isSafeReport());
