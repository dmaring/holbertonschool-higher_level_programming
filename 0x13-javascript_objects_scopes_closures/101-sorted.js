const myDict = require('./101-data').dict;

const newDict = {};
for (const key of Object.keys(myDict)) {
  const newList = [];
  const value = myDict[key];
  newDict[value] = newList;
  for (const key of Object.keys(myDict)) {
    if (myDict[key] === value) {
      newList.push(key);
    }
  }
}

console.log(newDict);
