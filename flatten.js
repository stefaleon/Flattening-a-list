function flatten(anArr){
  var flatArray = [];

  function makeFlatArray(someArr){
    someArr.forEach(function(element){
        if (Array.isArray(element)){
          makeFlatArray(element);
        } else {
          flatArray.push(element);
        }
    });
  }

  makeFlatArray(anArr);
  return flatArray;
}
