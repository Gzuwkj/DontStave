export function deepSearch(arr, call, pre = '') {
  if(!Array.isArray(arr)) return undefined;
  for(let item of arr.values()){
    if(call(item)) return pre + item.path;
    else if(item && item.hasOwnProperty('children')){
      let ret = deepSearch(item.children, call, pre + item.path);
      if(ret) return ret;
    }
  }
}

export function deepFilter(arr, call) {
  let ret = [];
  if(!Array.isArray(arr)) return undefined;
  for (let item of arr.values()){
    if(call(item)) ret.push(item);
    if(item && item.hasOwnProperty('children')){
      let t = deepFilter(item.children, call);
      if(Array.isArray(t)) ret[ret.length - 1].children = t;
    }
  }
  return ret.length > 0 ? ret : undefined;
}
