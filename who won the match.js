function main() {
    var goalsTeam1 = parseInt(readLine(), 10);
    var goalsTeam2 = parseInt(readLine(), 10);
    // function call
    finalResult(goalsTeam1, goalsTeam2)
    
}
//complete the function
function finalResult (goalsTeam1,goalsTeam2 ) { if(goalsTeam1  > goalsTeam2)
{ 

console.log("Team 1 won");
}
else if(goalsTeam1 < goalsTeam2)
{ 

console.log("Team 2 won");
}

else if(goalsTeam1===goalsTeam2){  console.log("Draw");
}
};
