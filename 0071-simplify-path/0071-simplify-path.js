/**
 * @param {string} path
 * @return {string}
 */
var simplifyPath = function(path) {
    answer = []
    splitedpath = path.split("/")
    for(p of splitedpath){
        if(p == '' || p == "."){
            continue;
        }else if(p == ".."){
            if(answer.length > 0){
                answer.pop();
            }
        }else{
            answer.push(p);
        }
    }
    return "/" + answer.join('/')
}